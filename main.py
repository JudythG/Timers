import tkinter
from tkinter import Tk, Button
from timer import Timer
from timerinputdlg import TimerInputDialog
import sys


def create_timer(event=None):
    """ Use Timer Input Dialog to get recipe title and amount of time for timer set. When user clicks OK to exit
    dialog, create and display a timer on the main window. """
    dialog = TimerInputDialog(title="Create Timer", parent=window)
    answer = (dialog.name, dialog.hours, dialog.minutes)

    # when Cancel clicked on TimerInputDialog, answer -> (None, None, None)
    # only display a timer when OK clicked
    if not answer == (None, None, None):
        Timer(window, answer[0], hours=answer[1], minutes=answer[2])

    add_timer_button.focus_set()


def close(event):
    """ Close the main window. """
    sys.exit()


window = Tk()
window.config(height=350, width=350)
window.bind('<Escape>', close)
add_timer_button = Button(window, text='Add Timer', width=25, command=create_timer)
add_timer_button.pack(side=tkinter.BOTTOM)
add_timer_button.bind("<Return>", create_timer)
add_timer_button.focus_set()

window.mainloop()
