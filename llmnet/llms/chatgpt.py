import os
from typing import List, Optional, Union

import openai

from llmnet.observer.tracker import track


def set_openai_key():
    track.info("Setting OPENAI_API_KEY")
    try:
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        track.info("OPENAI_API_KEY found in environment variables.")
    except Exception as e:
        track.warning(e)
        track.error("OPENAI_API_KEY not found in environment variables.")


def overwrite_openai_key(key: str):
    if not isinstance(key, str):
        track.error("Invalid key format. OPENAI_API_KEY not overwritten.")
        raise Exception("Invalid key format. OPENAI_API_KEY not overwritten.")
    else:
        os.environ["OPENAI_API_KEY"] = key
        track.warning("OPENAI_API_KEY overwritten.")


def llmbot(
    model: str,
    temperature: float,
    set_prompt: str,
    max_tokens: int = 2024,
    n: int = 1,
    stop: Optional[Union[str, List[str]]] = None,
) -> str:
    track.info(f"Sending prompt to OpenAI: {set_prompt}")
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": set_prompt},
        ],
        max_tokens=max_tokens,
        n=n,
        stop=stop,
        temperature=temperature,
    )
    track.info(f"Received response from OpenAI: {response}")

    answer = response["choices"][0]["message"]["content"].strip()

    return answer
