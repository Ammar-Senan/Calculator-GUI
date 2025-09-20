import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __int__(self, root):
        self.root = root
        self.root.title("Calulator")
        self.root.geometry("300X400")
        self.root.resizable(True, True)

        self.expression = ""

        #Create a string variable to display the resalt or text
        self.display_text = tk.StringVar()
