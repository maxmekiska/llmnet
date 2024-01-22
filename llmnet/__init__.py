__version__ = "0.1.0"

from typing import Any, Dict, List

from llmnet.blueprints.botnet import BotNetwork
from llmnet.blueprints.constants import LLMBOTS
from llmnet.process.multi import process_prompts


class LlmNetwork(BotNetwork):
    def __init__(self):
        self.worker_answers: str = ""
        self.worker_consensus: str = ""

        self.worker_answer_messages: List = []
        self.worker_consensus_messages: List = []

    @property
    def get_worker_answers(self) -> str:
        return self.worker_answers

    @property
    def get_worker_consensus(self) -> str:
        return self.worker_consensus

    @property
    def get_worker_answer_messages(self) -> List:
        return self.worker_answer_messages

    @property
    def get_worker_consensus_messages(self) -> List:
        return self.worker_consensus_messages

    @staticmethod
    def consensus_worker(worker: str, *args, **kwargs) -> Dict[Any, Any]:
        answer = LLMBOTS[worker](*args, **kwargs)
        return answer

    def create_network(
        self,
        instruct: List[Dict[str, str]],
        worker: str,
        max_concurrent_worker: int,
        connect: str = "Base your answer strictly on the following context and infromation:",
        **kwargs,
    ) -> None:
        prompts = []
        for pair in instruct:
            if pair.get("context"):
                prompt = (
                    pair.get("objective", "No objective")
                    + " "
                    + connect
                    + " "
                    + pair.get("context", "No context")
                )
            else:
                prompt = pair.get("objective", "no objective")

            prompts.append(prompt)

        kwargs["set_prompts"] = prompts

        answers = process_prompts(
            **kwargs,
            llmbot=LLMBOTS[worker],
            max_concurrent_worker=max_concurrent_worker,
        )
        for llmanswer in answers:
            self.worker_answers + llmanswer["answer"] + ";\n"

        self.worker_answer_messages = answers

    def apply_consensus(
        self,
        worker: str,
        set_prompt: str,
        *args,
        **kwargs,
    ) -> str:
        kwargs["set_prompt"] = set_prompt

        consensus = LlmNetwork.consensus_worker(worker, *args, **kwargs)
        self.worker_consensus = consensus["answer"]
        self.worker_consensus_messages.append(consensus)

        return consensus["answer"]
