__version__ = "0.0.3"

from typing import List

from llmnet.blueprints.botnet import BotNetwork
from llmnet.blueprints.constants import LLMBOTS
from llmnet.observer.tracker import track
from llmnet.process.multi import process_prompts


class LlmNetwork(BotNetwork):
    def __init__(self, set_input: List[str] = []):
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

    @staticmethod
    def set_default_consensus_worker_prompt(
        worker_objective: str, worker_answers: str
    ) -> str:
        prompt = (
            f"You are the final evaluator in a network of large language models. "
            f"Your task is to strictly use only the other models output and provide a final conclusion. "
            f"The orignal request was: {worker_objective}. The other models concluded the following: "
            f"{worker_answers}"
        )
        return prompt

    @staticmethod
    def consensus_worker(worker: str, *args, **kwargs) -> str:
        answer = LLMBOTS[worker](*args, **kwargs)
        return answer

    def create_network(
        self, objective: str, worker: str, max_concurrent_worker: int, *args, **kwargs
    ) -> None:
        self.worker_objective = objective

        kwargs["set_prompts"] = [
            objective
            + " Base your answer strictly on the following information: "
            + context
            for context in self.set_input
        ]

        answers = process_prompts(
            **kwargs,
            llmbot=LLMBOTS[worker],
            max_concurrent_worker=max_concurrent_worker,
        )
        self.worker_answers = " ".join(answers)

    def apply_consensus(
        self, worker: str, set_prompt: str = "", *args, **kwargs
    ) -> str:
        if set_prompt == "":
            kwargs["set_prompt"] = self.set_default_consensus_worker_prompt(
                self.worker_objective, self.worker_answers
            )
            track.info(
                f"No prompt provided. Using default prompt: {kwargs['set_prompt']}"
            )
        else:
            track.info(f"Prompt provided: {set_prompt}")
            kwargs["set_prompt"] = set_prompt

        consensus = LlmNetwork.consensus_worker(worker, *args, **kwargs)
        self.worker_consensus = consensus

        return consensus
