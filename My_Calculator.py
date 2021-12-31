######################################################################
# Author: Kyle Drummonds
# Username: drummondsk
#
# Assignment: Calculator Application
#
# Purpose: Create an interactive calculator app using appropriate object-oriented programming
# Acknowledgements:
#https://github.com/misha-pyshark/python-calculator/blob/master/calculator.py
#https://www.studytonight.com/tkinter/calculator-application-using-tkinter
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

from tkinter import *
import tkinter as tk

bg_color = "#91A8E7"
fg_color = "#F5F10F"
entry_bg_color = '#B6F7F1'
entry_fg_color = '#114206'

def main():
    """
    Creates an instance of the calculator class
    :return:
    """
    calc = Calculator()
    calc.window.mainloop()


class Calculator:
    """
    A class to represent the Calculator Application
    """

    def __init__(self):
        """
        Creates an instance of the Calculator class
        """
        self.window = tk.Tk()
        self.window.title("Calculator")  # Sets the title of the window
        self.window.geometry("330x450")  # Sets the size of the window
        self.window.resizable(0, 0)        # Prevents the window from being resized
        self.entry_label = self.create_entry_label()
        self.input_buttons = self.create_input_buttons()


    def create_entry_label(self):
        """
        Creates the Entry box to display user input for the calculator
        :return: self.entry_label: Entry box
        """

        self.entry_label=tk.Entry(self.window, textvariable="stringvar", borderwidth=10, justify="right", width=48, bg=entry_bg_color, fg=entry_fg_color, )
        self.entry_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        return self.entry_label

    def create_input_buttons(self):
        """
        Creates the input buttons and assigns the buttons a position on the grid for graphical display
        :return:None
        """

        # Row 1
        b0 = tk.Button(self.window, text="0", width=10, height=3,state="active", activebackground=entry_bg_color,cursor='hand2', command=lambda: self.clickButton(0))
        b0.grid(row=1, column=0, columnspan=1, sticky=NSEW)

        b1 = tk.Button(self.window, text="1", width=10, height=3, state="active", activebackground=entry_bg_color,  cursor='hand2', command=lambda: self.clickButton(1))
        b1.grid(row=1, column=1, columnspan=1, sticky=NSEW)

        b2 = tk.Button(self.window, text="2", width=10, height=3, state="active", activebackground=entry_bg_color,  cursor='hand2', command=lambda: self.clickButton(2))
        b2.grid(row=1, column=2, columnspan=1, sticky=NSEW)
        # Row 2
        b3 = tk.Button(self.window, text="3", width=10, height=3, state="active", activebackground=entry_bg_color, cursor='hand2', command=lambda: self.clickButton(3))
        b3.grid(row=2, column=0, columnspan=1, sticky=NSEW)

        b4 = tk.Button(self.window, text="4", width=10, height=3, state="active", activebackground=entry_bg_color,  cursor='hand2', command=lambda: self.clickButton(4))
        b4.grid(row=2, column=1, columnspan=1, sticky=NSEW)

        b5 = tk.Button(self.window, text="5", width=10, height=3, state="active", activebackground=entry_bg_color,  cursor='hand2', command=lambda: self.clickButton(5))
        b5.grid(row=2, column=2, columnspan=1, sticky=NSEW)
        # Row 3
        b6 = tk.Button(self.window, text="6", width=10, height=3, state="active", activebackground=entry_bg_color,  cursor='hand2', command=lambda: self.clickButton(6))
        b6.grid(row=3, column=0, columnspan=1, sticky=NSEW)

        b7 = tk.Button(self.window, text="7", width=10, height=3, state="active", activebackground=entry_bg_color, cursor='hand2', command=lambda: self.clickButton(7))
        b7.grid(row=3, column=1, columnspan=1, sticky=NSEW)

        b8 = tk.Button(self.window, text="8", width=10, height=3, state="active", activebackground=entry_bg_color, cursor='hand2', command=lambda: self.clickButton(8))
        b8.grid(row=3, column=2, columnspan=1, sticky=NSEW)
        # Row 4
        b9 = tk.Button(self.window, text="9", width=10, height=3, state="active", activebackground=entry_bg_color, cursor='hand2', command=lambda: self.clickButton(9))
        b9.grid(row=4, column=0, columnspan=1, sticky=NSEW)

        b_add = tk.Button(self.window, text="+", width=10, height=3, state="active", activebackground=entry_bg_color, cursor='hand2', command=lambda: self.clickButton('+'))
        b_add.grid(row=4, column=1, columnspan=1, sticky=NSEW)

        b_minus = tk.Button(self.window, text="-", width=10, height=3, state="active", activebackground=entry_bg_color,  cursor='hand2', command=lambda: self.clickButton('-'))
        b_minus.grid(row=4, column=2, columnspan=1, sticky=NSEW)
        # Row 5
        b_multiply = tk.Button(self.window, text="*", width=10, height=3, state="active", activebackground=entry_bg_color,  cursor='hand2', command=lambda: self.clickButton('*'))
        b_multiply.grid(row=5, column=0, columnspan=1, sticky=NSEW)

        b_divide = tk.Button(self.window, text="/", width=10, height=3, state="active", activebackground=entry_bg_color, cursor='hand2', command=lambda: self.clickButton('/'))
        b_divide.grid(row=5, column=1, columnspan=1, sticky=NSEW)

        b_equal = tk.Button(self.window, text="=", width=10, height=3, state="active",
                            activebackground=entry_bg_color, cursor='hand2', command=lambda: self.clickButton('='))
        b_equal.grid(row=5, column=2, columnspan=1, rowspan=2, sticky=NSEW)
        # Row 6
        b_clear = tk.Button(self.window, text="C", height=3, state="active",
                            activebackground=entry_bg_color, cursor='hand2', command=lambda: self.clickButton('C'))
        b_clear.grid(row=6, column=0, columnspan=2, sticky=EW)

    def clickButton(self, value):

        """
        Updates the Entry box input field whenever a button is pressed.
        :param value: The character that was pressed
        :return: None
        """


        input_equation = str(self.entry_label.get()) # Retrieves the characters pressed by the user and creates an equation where operations can be done

        # Displays the final answer after calculations if the user presses the '='
        if value == '=':
            final = str(eval(input_equation))
            self.entry_label.delete(-1, END)  # Clears the entry box input field
            self.entry_label.insert(0, final)  # Displays the final equation

        # Clears the input field if the user presses 'C'
        elif value == 'C':
            self.entry_label.delete(-1, END)  # Clears the entry box input field

        else:
            self.entry_label.delete('0', END)  # Clears the entry box input field
            self.entry_label.insert(0, input_equation + str(value))  # Displays the series of characters in the entry box input field

if __name__ == "__main__":
    main()