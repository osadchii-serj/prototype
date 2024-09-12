from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(init=False)
class IPrototype(ABC):

    @abstractmethod
    def clone(self):
        pass
