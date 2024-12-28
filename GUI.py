import tkinter as tk
import datetime as dt
import os

class ProgressTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Progress Tracker")
        self.root.geometry('350x200')

        self.streak_file = "streak_data.txt"
        self.streak = 0
        self.last_date = None

        self.load_streak_data()
        self.main_menu()

    def load_streak_data(self):
        if os.path.exists(self.streak_file):
            with open(self.streak_file, "r") as file:
                data = file.read().strip().split("\n")
                if len(data) == 2:
                    self.streak = int(data[0])
                    self.last_date = dt.datetime.strptime(data[1], "%Y-%m-%d").date()

        today = dt.date.today()
        if self.last_date and (today - self.last_date).days > 1:
            self.streak = 0  # Reset streak if missed a day
        elif self.last_date and self.last_date != today:
            self.last_date = today

    def save_streak_data(self):
        with open(self.streak_file, "w") as file:
            file.write(f"{self.streak}\n{self.last_date}")

    def main_menu(self):
        self.var = tk.IntVar()

        self.streak_label = tk.Label(self.root, text=f"Current Streak: {self.streak}", font=("Arial", 14))
        self.streak_label.pack(pady=10)

        check_button = tk.Checkbutton(self.root, text="Press Button", variable=self.var, command=self.on_button_toggle)
        check_button.pack(pady=10)

    def on_button_toggle(self):
        if self.var.get() == 1:
            today = dt.date.today()
            if self.last_date != today:
                self.streak += 1
                self.last_date = today
                self.save_streak_data()
            self.streak_label.config(text=f"Current Streak: {self.streak}")
        self.var.set(0)  # Reset the button to un-ticked after clicking

# Run the application
if __name__ == "__main__":
    tracker = ProgressTracker()
    tracker.root.mainloop()
