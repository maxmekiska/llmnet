import os

import openai

from llmnet.observer.tracker import track


def set_openai_key():
    track.warning("Setting OPENAI_API_KEY")
    try:
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        track.warning("OPENAI_API_KEY found in environment variables.")
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


def llmbot(model: str, temperature: float, set_prompt: str) -> str:
    track.warning(f"Sending prompt to OpenAI: {set_prompt}")
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": set_prompt},
        ],
        max_tokens=2024,
        n=1,
        stop=None,
        temperature=temperature,
    )
    track.warning(f"Received response from OpenAI: {response}")

    corrected_function = response["choices"][0]["message"]["content"].strip()

    return corrected_function
