import os
from typing import List, Optional, Union

import openai

from llmnet.observer.tracker import track


def openaillmbot(
    set_prompt: str,
    model: str = "gpt-3.5-turbo",
    max_tokens: int = 2024,
    temperature: float = 0.1,
    n: int = 1,
    stop: Optional[Union[str, List[str]]] = None,
) -> str:
    track.info(
        f"API REQUEST to {model} - Temperature: {temperature} - Max Tokens: {max_tokens}"
    )
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
