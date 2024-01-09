from unittest.mock import Mock, patch

import pytest

from llmnet.llms.googlegate import googlellmbot


@pytest.fixture
def mock_generative_model():
    with patch("llmnet.llms.googlegate.genai.GenerativeModel") as mock_model:
        yield mock_model


@pytest.fixture
def mock_track_warning():
    with patch("llmnet.llms.googlegate.track.warning") as mock_warning:
        yield mock_warning


def test_request_google_model(mock_generative_model, mock_track_warning):
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

    mock_track_warning.assert_called_once_with(
        f"API REQUEST to {model} - Temperature: {temperature} - Max Tokens: {max_output_tokens} - candidate_count: {candidate_count} - Stop: {stop_sequences}"
    )

    mock_generative_model.assert_called_once_with(model)

    assert result == "Test response"
