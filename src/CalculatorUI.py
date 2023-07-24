from tkinter import StringVar, ttk, Tk
from Calculator import Calculator
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
    calculator: Calculator

    def __init__(self):
        self.add = Add()
        self.subtract = Subtract()
        self.multiply = Multiply()
        self.divide = Divide()
        self.calculator = Calculator()
        
    def render(self, root: Tk) -> ttk.Frame:
        frame = ttk.Frame(root, padding='3 3 6 6')
        frame.grid(column=0, row=0, sticky='NSEW')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        calculation_label = ttk.Label(frame, textvariable=self.calculator.calculation_str)
        calculation_label.grid(column=0, row=0, columnspan=4, sticky='EW')
        
        entered_value_label = ttk.Label(frame, textvariable=self.calculator.entered_value)
        entered_value_label.grid(column=0, row=1, columnspan=4, sticky='EW')

        percent_button = ttk.Button(frame, text='%', command=lambda: self.calculator.percent())
        percent_button.grid(column=0, row=2, sticky='EW')
        root.bind('<KeyPress-percent>', lambda _: self.calculator.percent())
        
        clear_entry_button = ttk.Button(frame, text='CE', command=lambda: self.calculator.clear_entry())
        clear_entry_button.grid(column=1, row=2, sticky='EW')
        root.bind('<KeyPress-c>', lambda _: self.calculator.clear_entry())
        
        clear_all_button = ttk.Button(frame, text='C', command=lambda: self.calculator.clear_all())
        clear_all_button.grid(column=2, row=2, sticky='EW')
        root.bind('<KeyPress-Escape>', lambda _: self.calculator.clear_all())
        
        delete_button = ttk.Button(frame, text='⌫', command=lambda: self.calculator.delete())
        delete_button.grid(column=3, row=2, sticky='EW')
        root.bind('<KeyPress-BackSpace>', lambda _: self.calculator.delete())
        
        inverse_button = ttk.Button(frame, text='1/x', command=lambda: self.calculator.inverse())
        inverse_button.grid(column=0, row=3, sticky='EW')
        
        square_button = ttk.Button(frame, text='x²', command=lambda: self.calculator.square())
        square_button.grid(column=1, row=3, sticky='EW')
        
        square_root_button = ttk.Button(frame, text='√x', command=lambda: self.calculator.square_root())
        square_root_button.grid(column=2, row=3, sticky='EW')
        
        divide_button = ttk.Button(frame, text='÷', command=lambda: self.calculator.add_calculation(self.divide))
        divide_button.grid(column=3, row=3, sticky='EW')
        root.bind('<KeyPress-slash>', lambda _: self.calculator.add_calculation(self.divide))
        
        seven_button = ttk.Button(frame, text='7', command=lambda: self.calculator.number(7))
        seven_button.grid(column=0, row=4, sticky='EW')
        root.bind('<KeyPress-7>', lambda _: self.calculator.number(7))

        eight_button = ttk.Button(frame, text='8', command=lambda: self.calculator.number(8))
        eight_button.grid(column=1, row=4, sticky='EW')
        root.bind('<KeyPress-8>', lambda _: self.calculator.number(8))

        nine_button = ttk.Button(frame, text='9', command=lambda: self.calculator.number(9))
        nine_button.grid(column=2, row=4, sticky='EW')
        root.bind('<KeyPress-9>', lambda _: self.calculator.number(9))

        multiply_button = ttk.Button(frame, text='×', command=lambda: self.calculator.add_calculation(self.multiply))
        multiply_button.grid(column=3, row=4, sticky='EW')
        root.bind('<KeyPress-asterisk>', lambda _: self.calculator.add_calculation(self.multiply))
        
        four_button = ttk.Button(frame, text='4', command=lambda: self.calculator.number(4))
        four_button.grid(column=0, row=5, sticky='EW')
        root.bind('<KeyPress-4>', lambda _: self.calculator.number(4))

        five_button = ttk.Button(frame, text='5', command=lambda: self.calculator.number(5))
        five_button.grid(column=1, row=5, sticky='EW')
        root.bind('<KeyPress-5>', lambda _: self.calculator.number(5))

        six_button = ttk.Button(frame, text='6', command=lambda: self.calculator.number(6))
        six_button.grid(column=2, row=5, sticky='EW')
        root.bind('<KeyPress-6>', lambda _: self.calculator.number(6))

        subtract_button = ttk.Button(frame, text='-', command=lambda: self.calculator.add_calculation(self.subtract))
        subtract_button.grid(column=3, row=5, sticky='EW')
        root.bind('<KeyPress-minus>', lambda _: self.calculator.add_calculation(self.subtract))
        
        one_button = ttk.Button(frame, text='1', command=lambda: self.calculator.number(1))
        one_button.grid(column=0, row=6, sticky='EW')
        root.bind('<KeyPress-1>', lambda _: self.calculator.number(1))

        two_button = ttk.Button(frame, text='2', command=lambda: self.calculator.number(2))
        two_button.grid(column=1, row=6, sticky='EW')
        root.bind('<KeyPress-2>', lambda _: self.calculator.number(2))

        three_button = ttk.Button(frame, text='3', command=lambda: self.calculator.number(3))
        three_button.grid(column=2, row=6, sticky='EW')
        root.bind('<KeyPress-3>', lambda _: self.calculator.number(3))

        add_button = ttk.Button(frame, text='+', command=lambda: self.calculator.add_calculation(self.add))
        add_button.grid(column=3, row=6, sticky='EW')
        root.bind('<KeyPress-plus>', lambda _: self.calculator.add_calculation(self.add))

        plus_minus_button = ttk.Button(frame, text='±', command=lambda: self.calculator.negate())
        plus_minus_button.grid(column=0, row=7, sticky='EW')

        zero_button = ttk.Button(frame, text='0', command=lambda: self.calculator.number(0))
        zero_button.grid(column=1, row=7, sticky='EW')
        root.bind('<KeyPress-0>', lambda _: self.calculator.number(0))

        decimal_button = ttk.Button(frame, text='.', command=lambda: self.calculator.decimal())
        decimal_button.grid(column=2, row=7, sticky='EW')
        root.bind('<KeyPress-period>', lambda _: self.calculator.decimal())

        equals_button = ttk.Button(frame, text='=', command=lambda: self.calculator.calculate())
        equals_button.grid(column=3, row=7, sticky='EW')
        root.bind('<KeyPress-Return>', lambda _: self.calculator.calculate())
        
        return frame