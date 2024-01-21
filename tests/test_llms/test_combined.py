from unittest.mock import patch

from llmnet.llms.combined import randomllmbot

config = {"openaillmbot": {"param1": [1, 2, 3], "param2": ["a", "b", "c"]}}


def test_randomllmbot():
    with patch("llmnet.llms.combined.random.choice") as mock_random_choice, patch(
        "llmnet.llms.combined.openaillmbot"
    ) as mock_openaillmbot:
        mock_random_choice.return_value = mock_openaillmbot
        mock_openaillmbot.__name__ = "openaillmbot"

        result = randomllmbot("test", config)

        assert result == mock_openaillmbot.return_value
