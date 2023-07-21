import pytest

from llmnet import LlmNetwork

prepared_text = ["test1", "test2", "test3"]

ob = LlmNetwork(set_input=prepared_text)

# check default values


def test_get_worker_jobs():
    assert ob.get_worker_jobs == 3


def test_get_worker_objective():
    assert ob.get_worker_objective == ""


def test_get_worker_answers():
    assert ob.get_worker_answers == ""


def test_get_worker_consensus():
    assert ob.get_worker_consensus == ""
