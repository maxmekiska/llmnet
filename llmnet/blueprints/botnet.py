from abc import ABC, abstractmethod
from typing import Any, Dict, List


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
    def consensus_worker(worker, *args, **kwargs) -> Dict[Any, Any]:
        pass

    @abstractmethod
    def create_network(
        self,
        instruct: List[Dict[str, str]],  # Dict: {"objective": , "context": }
        worker: str,
        max_concurrent_worker: int,
        connect: str,
        **kwargs
    ) -> None:
        pass

    @abstractmethod
    def apply_consensus(self, worker: str, set_prompt: str, *args, **kwargs) -> str:
        pass
