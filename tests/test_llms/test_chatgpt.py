import io
import logging
import os
import sys
from unittest.mock import patch

import openai
import pytest

from llmnet.llms.chatgpt import (openaillmbot, overwrite_openai_key,
                                 set_openai_key)
from llmnet.observer.tracker import track


@pytest.fixture
def captured_output():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    yield captured_output
    sys.stdout = sys.__stdout__


def test_set_openai_key_with_api_key():
    with patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"}):
        set_openai_key()
        assert openai.api_key == "test_key"
        assert "OPENAI_API_KEY" in os.environ


def test_set_openai_key_without_api_key(captured_output):
    handler = logging.StreamHandler(captured_output)
    track.addHandler(handler)
    with patch("os.environ.get") as import_module_mock:
        import_module_mock.side_effect = Exception
        set_openai_key()
        output = captured_output.getvalue().strip()
        assert "OPENAI_API_KEY not found" in output


def test_overwrite_openai_key():
    with patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"}):
        overwrite_openai_key("new_key")
        assert os.environ["OPENAI_API_KEY"] == "new_key"


def test_overwrite_openai_key_error():
    with pytest.raises(
        Exception, match="Invalid key format. OPENAI_API_KEY not overwritten."
    ):
        overwrite_openai_key(23)


def test_openaillmbot():
    model = "test_model"
    temperature = 0.5
    set_prompt = "test_prompt"
    expected_answer = "llmbot response"

    with patch(
        "llmnet.llms.chatgpt.openai.ChatCompletion.create"
    ) as mock_completion_create:

        mock_completion_create.return_value = {
            "choices": [{"message": {"content": "llmbot response"}}]
        }

        answer = openaillmbot(
            model=model, temperature=temperature, set_prompt=set_prompt
        )

        assert answer == expected_answer
