from typing import Callable, Dict

from llmnet.llms.combined import randomllmbot
from llmnet.llms.googlegate import googlellmbot
from llmnet.llms.openaigate import openaillmbot

LLMBOTS: Dict[str, Callable[..., str]] = {
    "openaillmbot": openaillmbot,
    "googlellmbot": googlellmbot,
    "randomllmbot": randomllmbot,
}
