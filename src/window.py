import os
from tkinter import PhotoImage, Tk

from CalculatorUI import CalculatorUI

root = Tk()
root.title('Calculator')
filepath = os.path.join(os.path.dirname(__file__), 'assets', 'icon.ico')
root.iconbitmap(filepath)
root.resizable(False, False)

calculator = CalculatorUI()

frame = calculator.render(root)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
    
root.mainloop()
