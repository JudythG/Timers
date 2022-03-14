from tkinter import Canvas, Label, Button, messagebox
import math

NUM_SEC_IN_HOUR = 3600
NUM_SEC_IN_MINUTE = 60
TIMER_FONT = ("Arial", 16, "bold")
TEXT_FONT = ("Arial", 16)
TIMER_COLOR = "black"
TIMER_ALERT_COLOR = "red"
BUTTON_WIDTH = 15


def beep():
    """ if successful, beeps """
    try:
        import winsound
        winsound.Beep(400, 1000)
    except RuntimeError:
        messagebox.showerror(title="Runtime Error", message="The system is not able to beep the speaker")
        print("The system is not able to beep the speaker")
    except ImportError:
        messagebox.showerror(title="System Error", message="Cannot import sound module.")
        print("Can't import winsound module")


class Timer:
    """ Displays a label and associated timer along with start, stop, and delete buttons. """
    def __init__(self, parent, label_value, hours=0, minutes=0):
        self.window = parent
        self.timer = Canvas(parent, height=300, width=300, highlightbackground="blue", highlightthickness=2)
        self.timer.pack(padx=(20, 20), pady=(20, 20))

        self.label = Label(self.timer, text=label_value, font=TEXT_FONT)
        self.label.grid(row=0, column=0, padx=5, pady=5)
        self.timer_text = Label(self.timer, text="00:00", font=TIMER_FONT)
        self.timer_text.grid(row=0, column=1, padx=5, pady=5)
        self.start_button = Button(self.timer, text="Start", width=BUTTON_WIDTH, command=self.start_timer)
        self.start_button.grid(row=1, column=0, padx=5, pady=5)
        self.start_button.bind("<Return>", self.start_timer)
        self.stop_button = Button(self.timer, text="Stop", width=BUTTON_WIDTH, command=self.stop_timer)
        self.stop_button.grid(row=1, column=1, padx=5, pady=5)
        self.stop_button["state"] = "disabled"
        self.stop_button.bind("<Return>", self.stop_timer)
        self.delete_button = Button(self.timer, text="Delete", width=BUTTON_WIDTH, command=self.delete_timer)
        self.delete_button.grid(row=1, column=2, padx=5, pady=5)
        self.delete_button.bind("<Return>", self.delete_timer)
        self.time_in_seconds = hours * NUM_SEC_IN_HOUR + minutes * NUM_SEC_IN_MINUTE
        self.display_time()

        # is_paused used to continue beeping until the user hits the Stop button
        self.is_paused = False

    def start_timer(self, event=None):
        """ Starts the timer. """
        self.is_paused = False
        self.countdown()
        self.stop_button["state"] = "normal"
        self.start_button["state"] = "disabled"

    def stop_timer(self, event=None):
        """ Stops the timer. """
        self.is_paused = True
        self.timer_text.config(fg=TIMER_COLOR)
        self.stop_button["state"] = "disabled"
        self.start_button["state"] = "normal"

    def delete_timer(self, event=None):
        """ Deletes the timer and removes it from the main screen. """
        self.timer.destroy()

    def display_time(self):
        """ Converts time, which is in seconds, to hours and minutes and displays them. """
        hours = math.floor(self.time_in_seconds / NUM_SEC_IN_HOUR)
        minutes = math.floor((self.time_in_seconds - (hours * NUM_SEC_IN_HOUR)) / NUM_SEC_IN_MINUTE)
        seconds = self.time_in_seconds - (hours * NUM_SEC_IN_HOUR) - (minutes * NUM_SEC_IN_MINUTE)
        self.timer_text.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def countdown(self):
        """ Pauses self for a second. If time left in countdown, calls self again. Otherwise calls countdown_done. """
        if self.time_in_seconds >= 0:
            if not self.is_paused:
                self.display_time()
                timer = self.window.after(1000, self.countdown)
                self.time_in_seconds -= 1
        else:
            self.countdown_done()

    def countdown_done(self):
        """ Set font for hours and minutes to alert color. Calls function to beep alert. """
        self.timer_text.config(fg=TIMER_ALERT_COLOR)
        self.beep_until_stopped()

    def beep_until_stopped(self):
        """ Keeps beeping until user hits the Stop button. """
        if not self.is_paused:
            beep()
            self.window.after(5000, self.beep_until_stopped)
