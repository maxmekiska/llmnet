import uuid
from typing import Dict, Optional

import google.generativeai as genai

from llmnet.observer.tracker import track


def googlellmbot(
    set_prompt: str,
    model: str = "gemini-pro",
    max_output_tokens: int = 2024,
    temperature: float = 0.1,
    top_p: Optional[float] = None,
    top_k: Optional[int] = None,
    candidate_count: Optional[int] = 1,
    stop_sequences: Optional[str] = None,
) -> Dict[str, Dict[str, str]]:
    meta = {
        "llmbot": "googlellmbot",
        "model": model,
        "id": uuid.uuid4().hex,
        "prompt": set_prompt,
        "max_tokens": max_output_tokens,
        "temperature": temperature,
        "candidate_count": candidate_count,
        "stop": stop_sequences,
        "top_p": top_p,
        "top_k": top_k,
    }
    try:
        track.info(
            f"API REQUEST to {model} - Temperature: {temperature} - Max Tokens: {max_output_tokens} - candidate_count: {candidate_count} - Stop: {stop_sequences}"
        )
        model_ = genai.GenerativeModel(model)
        response = model_.generate_content(
            set_prompt,
            generation_config=genai.types.GenerationConfig(
                candidate_count=candidate_count,
                stop_sequences=stop_sequences,
                max_output_tokens=max_output_tokens,
                temperature=temperature,
                top_k=top_k,
                top_p=top_p,
            ),
        )
        track.info(f"Received response from Google: {response.text}")

        answer = response.text

        output = {"answer": answer, "meta": meta}

        return output
    except Exception as e:
        track.error(f"Error in Google request: {e}")

        error_message = f"Google request failed. Error: {str(e)}"

        output = {"answer": error_message, "meta": meta}
        return output
