import uuid
from typing import Dict, List, Optional, Union

import openai

from llmnet.observer.tracker import track


def openaillmbot(
    set_prompt: str,
    model: str = "gpt-3.5-turbo",
    max_tokens: int = 2024,
    temperature: float = 0.1,
    n: int = 1,
    stop: Optional[Union[str, List[str]]] = None,
) -> Dict[str, Dict[str, str]]:
    meta = {
        "llmbot": "openaillmbot",
        "model": model,
        "id": uuid.uuid4().hex,
        "prompt": set_prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "n": n,
        "stop": stop,
    }
    try:
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

        output = {"answer": answer, "meta": meta}

        return output

    except Exception as e:
        track.error(f"Error in OpenAI request: {e}")

        error_message = f"OpenAI request failed. Error: {str(e)}"

        output = {"answer": error_message, "meta": meta}
        return output
