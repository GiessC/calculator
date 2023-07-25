import os
import sys
from tkinter import Tk

from CalculatorUI import CalculatorUI

root = Tk()
root.title('Calculator')
try:
    base_path = getattr(sys, '_MEIPASS', os.getcwd())
except Exception:
    base_path = os.path.abspath('.')
filepath = os.path.join(base_path, 'assets', 'icon.ico')
root.iconbitmap(filepath)
root.resizable(False, False)

calculator = CalculatorUI()

frame = calculator.render(root)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
    
root.mainloop()
