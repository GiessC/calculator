from tkinter import Tk

from CalculatorUI import CalculatorUI

root = Tk()
root.title('Calculator')

calculator = CalculatorUI()

frame = calculator.render(root)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
    
root.mainloop()
