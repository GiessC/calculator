from tkinter import StringVar
from Calculation import Calculation
from Operation import Operation


class Calculator:
    current_calculation: Calculation | None
    entered_value: StringVar
    calculation_str: StringVar
    touched: bool
    error: bool
    
    def __init__(self):
        self.current_calculation = None
        self.entered_value = StringVar()
        self.entered_value.set('0')
        self.calculation_str = StringVar()
        self.touched = False
        self.error = False
        
    def calculate(self):
        if self.error:
            self.clear_entry()
        if self.current_calculation is None:
            self.calculation_str.set(f'{self.entered_value.get()} =')
            return
        if str(self.current_calculation.operation) == '/' and self.entered_value.get() == '0':
            self.calculation_str.set('')
            self.entered_value.set('Cannot divide by zero')
            self.error = True
            self.current_calculation = None
            self.touched = False
            return
        self.calculation_str.set(f'{self.calculation_str.get()} {self.entered_value.get()} =')
        self.entered_value.set(str(self.current_calculation.perform(float(self.entered_value.get()))))
        self.current_calculation = None
        self.touched = False
        
    def add_calculation(self, operation: Operation):
        if self.error:
            self.clear_entry()
        self.calculate()
        if self.current_calculation is not None and not self.touched:
            return
        if self.current_calculation is not None and self.touched:
            self.entered_value.set(str(self.current_calculation.perform(float(self.entered_value.get()))))
            self.entered_value.set('0')
        self.touched = False
        self.current_calculation = Calculation(float(self.entered_value.get()), operation)
        self.calculation_str.set(str(self.current_calculation))
        self.entered_value.set('0')
    
    def clear_entry(self):
        self.entered_value.set('0')
        self.touched = False
        self.error = False
    
    def clear_all(self):
        self.current_calculation = None
        self.entered_value.set('0')
        self.calculation_str.set('')
        self.touched = False
        self.error = False
        
    def delete(self):
        if self.error:
            self.clear_entry()
        self.entered_value.set(self.entered_value.get()[:-1])
        if len(self.entered_value.get()) == 0:
            self.entered_value.set('0')
            
    def percent(self):
        if self.error:
            self.clear_entry()
        self.touched = True
        parsed_value = float(self.entered_value.get())
        self.entered_value.set(str(parsed_value / 100.0))
        if self.current_calculation is not None:
            self.calculation_str.set(f'{self.current_calculation} {self.entered_value}')

    def inverse(self):
        if self.error:
            self.clear_entry()
        self.touched = True
        parsed_value = float(self.entered_value.get())
        self.entered_value.set(str(1.0 / parsed_value))
        if self.current_calculation is not None:
            self.calculation_str.set(f'{self.current_calculation} (1/{self.entered_value})')
            
    def square(self):
        if self.error:
            self.clear_entry()
        self.touched = True
        parsed_value = float(self.entered_value.get())
        self.entered_value.set(str(parsed_value ** 2))
        if self.current_calculation is not None:
            self.calculation_str.set(f'{self.current_calculation} ({self.entered_value}^2)')
            
    def square_root(self):
        if self.error:
            self.clear_entry()
        self.touched = True
        parsed_value = float(self.entered_value.get())
        self.entered_value.set(str(parsed_value ** 0.5))
        if self.current_calculation is not None:
            self.calculation_str.set(f'{self.current_calculation} √({self.entered_value})')
            
    def decimal(self):
        if self.error:
            self.clear_entry()
        if '.' not in self.entered_value.get():
            self.touched = True
            self.entered_value.set(f'{self.entered_value.get()}.')

    def negate(self):
        if self.error:
            self.clear_entry()
        self.touched = True
        parsed_value = float(self.entered_value.get())
        if parsed_value < 0:
            self.entered_value.set(str(abs(parsed_value)))
        elif parsed_value > 0:
            self.entered_value.set(f'-{self.entered_value}')
            
    def number(self, value: int):
        if self.error:
            self.clear_entry()
        self.touched = True
        if self.entered_value.get() == '0':
            self.entered_value.set(str(value))
        else:
            self.entered_value.set(f'{self.entered_value.get()}{str(value)}')
            
    def __str__(self):
        return f'Current Calculation: {self.current_calculation}\n' + \
            f'Entered Value: {self.entered_value}\n' + \
            f'Calculation String: {self.calculation_str}\n' + \
            f'Touched: {self.touched}'
