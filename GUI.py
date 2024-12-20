import tkinter as tk
import datetime as dt
class ProgressTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Progress tracker")
        self.root.geometry('350x200')

    def main_menu(self):
        self.var = tk.IntVar()
        checkButton = tk.Checkbutton(self.root, text = "Press Button", variable=self.var, onvalue=1, offvalue=0, command=self.on_button_toggle)
        checkButton.pack()
    def on_button_toggle(self):
        if self.var.get() == 1:
            print("ticked innit")
        else:
            print("Unticked")

in1 = ProgressTracker()
in1.main_menu()
in1.root.mainloop()


