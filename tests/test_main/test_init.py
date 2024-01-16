from llmnet import LlmNetwork

prepared_text = ["test1", "test2", "test3"]

ob = LlmNetwork()

# check default values


def test_get_worker_answers():
    assert ob.get_worker_answers == ""


def test_get_worker_consensus():
    assert ob.get_worker_consensus == ""
