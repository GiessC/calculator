from Calculation import Calculation
from Operation import Operation


class Calculator:
    current_calculation: Calculation | None
    entered_value: str
    calculation_str: str
    touched: bool
    
    def __init__(self):
        self.current_calculation = None
        self.entered_value = '0'
        self.calculation_str = ''
        self.touched = False
        
    def calculate(self):
        if self.current_calculation is None:
            self.calculation_str = f'{self.entered_value} ='
            return
        self.calculation_str = f'{self.calculation_str} {self.entered_value} ='
        self.entered_value = str(self.current_calculation.perform(float(self.entered_value)))
        self.current_calculation = None
        self.touched = False
        
    def add_calculation(self, operation: Operation):
        if self.current_calculation is not None and self.touched:
            self.entered_value = str(self.current_calculation.perform(float(self.entered_value)))
        self.touched = False
        self.current_calculation = Calculation(float(self.entered_value), operation)
        self.calculation_str = str(self.current_calculation)
    
    def clear_entry(self):
        self.entered_value = '0'
        self.touched = False
    
    def clear_all(self):
        self.current_calculation = None
        self.entered_value = '0'
        self.calculation_str = ''
        self.touched = False
        
    def delete(self):
        self.entered_value = self.entered_value[:-1]
        if len(self.entered_value) == 0:
            self.entered_value = '0'
            
    def percent(self):
        self.touched = True
        parsed_value = float(self.entered_value)
        self.entered_value = str(parsed_value / 100.0)
        if self.current_calculation is not None:
            self.calculation_str = f'{self.current_calculation} {self.entered_value}'

    def inverse(self):
        self.touched = True
        parsed_value = float(self.entered_value)
        self.entered_value = str(1.0 / parsed_value)
        if self.current_calculation is not None:
            self.calculation_str = f'{self.current_calculation} (1/{self.entered_value})'
            
    def square(self):
        self.touched = True
        parsed_value = float(self.entered_value)
        self.entered_value = str(parsed_value ** 2)
        if self.current_calculation is not None:
            self.calculation_str = f'{self.current_calculation} ({self.entered_value}^2)'
            
    def square_root(self):
        self.touched = True
        parsed_value = float(self.entered_value)
        self.entered_value = str(parsed_value ** 0.5)
        if self.current_calculation is not None:
            self.calculation_str = f'{self.current_calculation} √({self.entered_value})'
            
    def decimal(self):
        if '.' not in self.entered_value:
            self.touched = True
            self.entered_value += '.'

    def negate(self):
        self.touched = True
        parsed_value = float(self.entered_value)
        if parsed_value < 0:
            self.entered_value = str(abs(parsed_value))
        elif parsed_value > 0:
            self.entered_value = f'-{self.entered_value}'
            
    def number(self, value: int):
        self.touched = True
        if self.entered_value == '0':
            self.entered_value = str(value)
        else:
            self.entered_value += str(value)
            
    def __str__(self):
        return f'Current Calculation: {self.current_calculation}\n' + \
            f'Entered Value: {self.entered_value}\n' + \
            f'Calculation String: {self.calculation_str}\n' + \
            f'Touched: {self.touched}'
