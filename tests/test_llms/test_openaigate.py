from unittest.mock import patch

from llmnet.llms.openaigate import openaillmbot


def test_openaillmbot():
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

        assert answer == expected_answer
