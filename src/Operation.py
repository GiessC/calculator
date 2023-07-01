from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def perform(self, first_value: float, second_value: float) -> float:
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        pass