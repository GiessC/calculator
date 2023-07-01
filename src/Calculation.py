from Operation import Operation


class Calculation:
    first_value: float
    operation: Operation
    
    def __init__(self, first_value: float, operation: Operation):
        self.first_value = first_value
        self.operation = operation
        
    def perform(self, second_value: float) -> float:
        return self.operation.perform(self.first_value, second_value)

    def __str__(self) -> str:
        return f'{self.first_value} {self.operation}'
