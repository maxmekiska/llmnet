import pytest

from llmnet.process.multi import process_prompts, process_single_prompt


def mock_worker(set_prompt: str, *args, **kwargs) -> str:
    return f"Processed: {set_prompt}"


def test_process_single_prompt():
    set_prompt = "Prompt 1"
    args = ()
    kwargs = {"param": "value"}
    expected_result = "Processed: Prompt 1"

    result = process_single_prompt(set_prompt, mock_worker, args, kwargs)

    assert result == expected_result


def test_process_prompts():
    pass
