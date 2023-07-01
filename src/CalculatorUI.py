from tkinter import ttk
from Operation import Operation
from Add import Add
from Subtract import Subtract
from Multiply import Multiply
from Divide import Divide


class CalculatorUI:
    add: Operation
    subtract: Operation
    multiply: Operation
    divide: Operation

    def __init__(self):
        self.add = Add()
        self.subtract = Subtract()
        self.multiply = Multiply()
        self.divide = Divide()
        
    def render(self, root) -> ttk.Frame:
        frame = ttk.Frame(root, padding='3 3 12 12')
        
        return frame