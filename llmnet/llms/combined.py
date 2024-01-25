import random
import typing
from typing import Dict

from llmnet.observer.tracker import track

from .googlegate import googlellmbot
from .openaigate import openaillmbot


@typing.no_type_check
def randomllmbot(set_prompt: str, random_configuration: Dict = {}) -> str:
    model = random.choice([openaillmbot, googlellmbot])

    configuration = random_configuration[model.__name__]
    track.info(f"Calling the following model llm: {model.__name__}")

    chosen_configuration = {
        key: random.choice(value_list) for key, value_list in configuration.items()
    }
    track.info(f"Chosen configuration: {chosen_configuration}")

    answer = model(set_prompt=set_prompt, **chosen_configuration)
    return answer


@typing.no_type_check
def randomopenaillmbot(set_prompt: str, random_configuration: Dict = {}) -> str:
    chosen_configuration = {
        key: random.choice(value_list)
        for key, value_list in random_configuration.items()
    }
    track.info(f"Chosen configuration: {chosen_configuration}")

    answer = openaillmbot(set_prompt=set_prompt, **chosen_configuration)
    return answer


@typing.no_type_check
def randomgooglellmbot(set_prompt: str, random_configuration: Dict = {}) -> str:
    chosen_configuration = {
        key: random.choice(value_list)
        for key, value_list in random_configuration.items()
    }
    track.info(f"Chosen configuration: {chosen_configuration}")

    answer = googlellmbot(set_prompt=set_prompt, **chosen_configuration)
    return answer
