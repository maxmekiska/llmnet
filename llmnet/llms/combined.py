import random
import typing

from llmnet.observer.tracker import track

from .googlegate import googlellmbot
from .openaigate import openaillmbot


@typing.no_type_check
def randomllmbot(set_prompt: str, *args, **kwargs) -> str:
    model = random.choice([openaillmbot, googlellmbot])
    track.info(f"Calling the following model llm: {model.__name__}")
    answer = model(set_prompt=set_prompt, *args, **kwargs)
    return answer
