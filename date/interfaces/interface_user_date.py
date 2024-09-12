from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(init=False)
class IForm(ABC):

    @abstractmethod
    def create_form(self):
        pass
