from unittest.mock import Mock, call, patch

import pytest

from llmnet.llms.googlegate import googlellmbot


@pytest.fixture
def mock_generative_model():
    with patch("llmnet.llms.googlegate.genai.GenerativeModel") as mock_model:
        yield mock_model


@pytest.fixture
def mock_track_info():
    with patch("llmnet.llms.googlegate.track.info") as mock_info:
        yield mock_info


def test_request_google_model(mock_generative_model, mock_track_info):
    set_prompt = "Test prompt"
    model = "gemini-pro"
    candidate_count = 1
    stop_sequences = None
    max_output_tokens = 1024
    temperature = 0.1
    top_p = None
    top_k = None

    mock_response = Mock(text="Test response")
    mock_generative_model.return_value.generate_content.return_value = mock_response

    result = googlellmbot(
        set_prompt=set_prompt,
        model=model,
        candidate_count=candidate_count,
        stop_sequences=stop_sequences,
        max_output_tokens=max_output_tokens,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
    )

    expected_call_prior = call(
        f"API REQUEST to {model} - Temperature: {temperature} - Max Tokens: {max_output_tokens} - candidate_count: {candidate_count} - Stop: {stop_sequences}"
    )
    expected_call_post = call("Received response from Google: Test response")

    expected_calls = [expected_call_prior, expected_call_post]

    mock_track_info.assert_has_calls(expected_calls)
    assert len(mock_track_info.mock_calls) == 2

    mock_generative_model.assert_called_once_with(model)

    assert result == "Test response"
