from unittest.mock import patch

import pytest

from llmnet.llms.combined import (randomgooglellmbot, randomllmbot,
                                  randomopenaillmbot)

config = {"openaillmbot": {"param1": [1, 2, 3], "param2": ["a", "b", "c"]}}


@pytest.fixture
def mock_openaillmbot():
    with patch("llmnet.llms.combined.openaillmbot") as mock_openaillmbot:
        yield mock_openaillmbot


@pytest.fixture
def mock_googlellmbot():
    with patch("llmnet.llms.combined.googlellmbot") as mock_googlellmbot:
        yield mock_googlellmbot


def test_randomllmbot():
    with patch("llmnet.llms.combined.random.choice") as mock_random_choice, patch(
        "llmnet.llms.combined.openaillmbot"
    ) as mock_openaillmbot:
        mock_random_choice.return_value = mock_openaillmbot
        mock_openaillmbot.__name__ = "openaillmbot"

        result = randomllmbot("test", config)

        assert result == mock_openaillmbot.return_value


def test_randomopenaillmbot(mock_openaillmbot):
    set_prompt = "Test Prompt"
    random_configuration = {
        "param1": ["value1", "value2"],
        "param2": ["value3", "value4"],
    }

    mock_openaillmbot.return_value = "Mocked answer"

    result = randomopenaillmbot(set_prompt, random_configuration)

    mock_openaillmbot.assert_called_once()
    assert result == "Mocked answer"


def test_randomgooglellmbot(mock_googlellmbot):
    set_prompt = "Test Prompt"
    random_configuration = {
        "param1": ["value1", "value2"],
        "param2": ["value3", "value4"],
    }

    mock_googlellmbot.return_value = "Mocked answer"

    result = randomgooglellmbot(set_prompt, random_configuration)

    mock_googlellmbot.assert_called_once()
    assert result == "Mocked answer"
