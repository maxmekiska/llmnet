import os
from typing import List, Optional, Union

import openai

from llmnet.observer.tracker import track


def openaillmbot(
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
