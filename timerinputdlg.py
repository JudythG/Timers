import tkinter as tk
from tkinter import simpledialog

# simpledialog documentation: https://docs.python.org/3/library/dialog.html
# example code I followed: https://code-maven.com/slides/python/tk-customized-simple-dialog


class TimerInputDialog(tk.simpledialog.Dialog):
    """ Modal dialog that allows user to input label and how long, in hours and minutes, to set the timer. """
    def __init__(self, parent, title):
        self.label = None
        self.label_box = None
        self.hours = None
        self.hours_box = None
        self.minutes = None
        self.minutes_box = None
        self.name = None
        super().__init__(parent, title)

    def body(self, frame):
        """ Create the dialog body. """
        label = tk.Label(frame, width=25, text="Label")
        label.grid(row=0, column=0)
        self.label_box = tk.Entry(frame, width=25)
        self.label_box.grid(row=0, column=1)

        hours_label = tk.Label(frame, width=25, text="Hours")
        hours_label.grid(row=1, column=0)
        self.hours_box = tk.Entry(frame, width=25)
        self.hours_box.grid(row=1, column=1)

        minutes_label = tk.Label(frame, width=25, text="Minutes")
        minutes_label.grid(row=2, column=0)
        self.minutes_box = tk.Entry(frame, width=25)
        self.minutes_box.grid(row=2, column=1)

        # return item that will have focus
        return self.label_box

    def validate(self):
        """ Validate data. No fields may be empty. Hours and minutes must be integers.
        Returns True if data is valid, false otherwise. """
        self.name = self.label_box.get()
        if not len(self.name):
            tk.messagebox.showerror(title="Empty Field", message="Recipe title may not be empty")
            return False

        try:
            self.hours = int(self.hours_box.get())
            self.minutes = int(self.minutes_box.get())
        except ValueError:
            tk.messagebox.showerror(title="Type Error", message="Hours and minutes must be integers")
            return False

        return True



