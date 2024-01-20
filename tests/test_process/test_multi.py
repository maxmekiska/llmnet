from llmnet.process.multi import process_prompts, process_single_prompt


def mock_worker(set_prompt: str, *args, **kwargs) -> str:
    return {"answer": f"Processed: {set_prompt}", "meta": "metadata dict"}


def test_process_single_prompt():
    set_prompt = "Prompt 1"
    args = ()
    kwargs = {"param": "value"}
    expected_result = "Processed: Prompt 1"

    result = process_single_prompt(set_prompt, mock_worker, args, kwargs)

    assert result["answer"] == expected_result


def test_process_prompts():
    args = ()
    kwargs = {"param": "value"}

    results = process_prompts(
        ["prompt1", "prompt2"], mock_worker, max_concurrent_worker=2, *args, **kwargs
    )

    assert results == [
        {"answer": "Processed: prompt1", "meta": "metadata dict"},
        {"answer": "Processed: prompt2", "meta": "metadata dict"},
    ]
