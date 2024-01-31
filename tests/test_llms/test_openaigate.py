from unittest.mock import patch

from llmnet.llms.openaigate import openaillmbot


def test_openaillmbot_ok():
    model = "test_model"
    temperature = 0.5
    set_prompt = "test_prompt"
    expected_answer = "llmbot response"

    with patch(
        "llmnet.llms.openaigate.openai.ChatCompletion.create"
    ) as mock_completion_create:
        mock_completion_create.return_value = {
            "choices": [{"message": {"content": "llmbot response"}}]
        }

        answer = openaillmbot(
            model=model, temperature=temperature, set_prompt=set_prompt
        )

        assert answer["answer"] == expected_answer


def test_openaillmbot_error():
    model = "test_model"
    temperature = 0.5
    set_prompt = "test_prompt"

    with patch(
        "llmnet.llms.openaigate.openai.ChatCompletion.create"
    ) as mock_completion_create:
        mock_completion_create.return_value = {
            "choices": [{"message": {"content": "llmbot response"}}]
        }

        mock_completion_create.side_effect = Exception("Test error")

        error_answer = openaillmbot(
            model=model, temperature=temperature, set_prompt=set_prompt
        )

        assert error_answer["answer"] == "OpenAI request failed. Error: Test error"
