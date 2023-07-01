from Operation import Operation

class Divide(Operation):
    def perform(self, first_value: float, second_value: float) -> float:
        return first_value / second_value
    
    def __str__(self) -> str:
        return '/'
