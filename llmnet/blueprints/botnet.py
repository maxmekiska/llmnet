from abc import ABC, abstractmethod
from typing import List


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

    @staticmethod
    @abstractmethod
    def set_default_consensus_worker_prompt(
        worker_objective: str, worker_answers: str
    ) -> str:
        pass

    @staticmethod
    @abstractmethod
    def consensus_worker(cls, worker, *args, **kwargs) -> str:
        pass

    @abstractmethod
    def create_network(self, objective: str, worker: str, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def apply_consensus(self, worker: str, *args, **kwargs) -> str:
        pass
