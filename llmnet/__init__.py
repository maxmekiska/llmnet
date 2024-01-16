__version__ = "0.0.4"

from typing import List

from llmnet.blueprints.botnet import BotNetwork
from llmnet.blueprints.constants import LLMBOTS
from llmnet.observer.tracker import track
from llmnet.process.multi import process_prompts


class LlmNetwork(BotNetwork):
    def __init__(self):
        self.worker_answers: str = ""
        self.worker_consensus: str = ""

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
        self,
        instruct: List[tuple[str, str]],
        worker: str,
        max_concurrent_worker: int,
        connect: str = "Base your answer strictly on the following context and infromation:",
        **kwargs,
    ) -> None:
        prompts = []
        for pair in instruct:
            if pair[1] == "":
                prompt = pair[0]
            else:
                prompt = pair[0] + " " + connect + " " + pair[1]

            prompts.append(prompt)

        kwargs["set_prompts"] = prompts

        answers = process_prompts(
            **kwargs,
            llmbot=LLMBOTS[worker],
            max_concurrent_worker=max_concurrent_worker,
        )
        self.worker_answers = ";\n".join(answers)

    def apply_consensus(
        self,
        worker: str,
        set_prompt: str = "",
        set_objective: str = "",
        *args,
        **kwargs,
    ) -> str:
        if set_prompt == "":
            kwargs["set_prompt"] = self.set_default_consensus_worker_prompt(
                set_objective, self.worker_answers
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
