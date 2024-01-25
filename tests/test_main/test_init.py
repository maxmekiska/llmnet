from unittest.mock import patch

import pytest

from llmnet import LlmNetwork


@pytest.fixture
def llm_network_instance():
    return LlmNetwork()


def test_get_worker_answers(llm_network_instance):
    llm_network_instance.worker_answers = "Answer 1;\nAnswer 2;\n"
    assert llm_network_instance.get_worker_answers == "Answer 1;\nAnswer 2;\n"


def test_get_worker_consensus(llm_network_instance):
    llm_network_instance.worker_consensus = "Consensus Answer"
    assert llm_network_instance.get_worker_consensus == "Consensus Answer"


def test_get_worker_answers_messages(llm_network_instance):
    llm_network_instance.worker_answers_messages = [
        {"answer": "Answer 1"},
        {"answer": "Answer 2"},
    ]
    assert llm_network_instance.get_worker_answers_messages == [
        {"answer": "Answer 1"},
        {"answer": "Answer 2"},
    ]


def test_get_worker_consensus_messages(llm_network_instance):
    llm_network_instance.worker_consensus_messages = [
        {"answer": "Consensus 1"},
        {"answer": "Consensus 2"},
    ]
    assert llm_network_instance.get_worker_consensus_messages == [
        {"answer": "Consensus 1"},
        {"answer": "Consensus 2"},
    ]


def test_create_network(llm_network_instance):
    with patch("llmnet.process_prompts") as mock_process_prompts:
        mock_process_prompts.return_value = [{"answer": "Mocked Answer"}]

        instruct = [
            {"objective": "Objective 1", "context": "Context 1"},
            {"objective": "Objective 2", "context": "Context 2"},
        ]

        llm_network_instance.create_network(
            instruct=instruct,
            worker="openaillmbot",
            max_concurrent_worker=3,
            connect="Base your answer strictly on the following context and information:",
        )

        assert llm_network_instance.worker_answer_messages == [
            {"answer": "Mocked Answer"}
        ]


def test_apply_consensus(llm_network_instance):
    with patch("llmnet.LlmNetwork.consensus_worker") as mock_consensus_worker:
        mock_consensus_worker.return_value = {"answer": "Mocked Consensus"}

        llm_network_instance.worker_answers = "Answer 1;\nAnswer 2;\n"

        consensus_answer = llm_network_instance.apply_consensus(
            worker="worker_1",
            set_prompt="Objective for Consensus",
        )

        assert consensus_answer == "Mocked Consensus"
        assert llm_network_instance.worker_consensus == "Mocked Consensus"
        assert llm_network_instance.worker_consensus_messages == [
            {"answer": "Mocked Consensus"}
        ]
