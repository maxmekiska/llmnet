__version__ = "0.0.1"

from abc import ABC, abstractmethod
from typing import List

from llmnet.llms.chatgpt import llmbot, set_openai_key
from llmnet.observer.tracker import track
from llmnet.process.multi import process_prompts

LLMBOTS = {
    "llmbot": llmbot,
}


class BotNetwork(ABC):
    @abstractmethod
    def __init__(self, set_input: List[str] = []):
        pass

    @property
    @abstractmethod
    def get_worker_jobs(self) -> int:
        pass

    @property
    @abstractmethod
    def get_worker_objective(self) -> str:
        pass

    @property
    @abstractmethod
    def get_worker_answers(self) -> str:
        pass

    @property
    @abstractmethod
    def get_worker_consensus(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def consensus_worker(cls, worker, *args, **kwargs) -> str:
        pass

    @abstractmethod
    def create_network(self, objective: str, worker: str, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def apply_consensus(self, worker: str, *args, **kwargs) -> str:
        pass


class LlmNetwork(BotNetwork):
    def __init__(self, set_input: List[str] = []):

        set_openai_key()

        self.set_input = set_input

        self.worker_jobs = len(set_input)

        self.worker_objective = ""
        self.worker_answers = ""
        self.worker_consensus = ""

    @property
    def get_worker_jobs(self) -> int:
        return self.worker_jobs

    @property
    def get_worker_objective(self) -> str:
        return self.worker_objective

    @property
    def get_worker_answers(self) -> str:
        return self.worker_answers

    @property
    def get_worker_consensus(self) -> str:
        return self.worker_consensus

    @classmethod
    def consensus_worker(cls, worker, *args, **kwargs) -> str:
        answer = LLMBOTS[worker](*args, **kwargs)
        return answer

    def create_network(
        self, objective: str, worker: str, max_concurrent_worker: int, *args, **kwargs
    ) -> None:
        self.worker_objective = objective

        kwargs["set_prompts"] = [
            objective
            + " Base your answer strictly on the following information: "
            + prompt
            for prompt in self.set_input
        ]

        answers = process_prompts(
            worker=LLMBOTS[worker], max_worker=max_concurrent_worker, *args, **kwargs
        )
        self.worker_answers = " ".join(answers)

    def apply_consensus(self, worker: str, *args, **kwargs) -> str:
        kwargs["set_prompt"] = (
            f"You are the final evaluator in a network of large language models. "
            f"Your task is to strictly use only the other models output and provide a final conclusion. "
            f"The orignal request was: {self.worker_objective}. The other models concluded the following: "
            f"{self.worker_answers}"
        )

        consensus = LlmNetwork.consensus_worker(worker=worker, *args, **kwargs)
        self.worker_consensus = consensus

        return consensus
