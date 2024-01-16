from abc import ABC, abstractmethod
from typing import List


class BotNetwork(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def get_worker_answers(self) -> str:
        pass

    @property
    @abstractmethod
    def get_worker_consensus(self) -> str:
        pass

    @staticmethod
    @abstractmethod
    def set_default_consensus_worker_prompt(
        worker_objective: str, worker_answers: str
    ) -> str:
        pass

    @staticmethod
    @abstractmethod
    def consensus_worker(worker, *args, **kwargs) -> str:
        pass

    @abstractmethod
    def create_network(
        self,
        instruct: List[tuple[str, str]],  # tuple: (objective, context)
        worker: str,
        max_concurrent_worker: int,
        connect: str,
        **kwargs
    ) -> None:
        pass

    @abstractmethod
    def apply_consensus(self, worker: str, *args, **kwargs) -> str:
        pass
