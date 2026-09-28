import tkinter as tk
from datetime import datetime

class digital_alarm():
    background_colour = "#000000"

    def set_local_time(self): #setting local time function 
        self.time = datetime.now().strftime("%H:%M:%S") #24hr style 00:00:00
        self.time_label.config(text=self.time)
        self.time_label.after(1000, self.set_local_time) #tkinters .after() used here for updating the clock every 1000ms

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Digital Clock by @digse")
        self.root.configure(bg=self.background_colour)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.time_label = tk.Label(self.root, font=('alarm clock', 70), bg=self.background_colour, fg="#12d600") #alarm style font (free to use) i found on dafont ---> python_projects\digital_clock\alarm clock.ttf
        self.time_label.grid(row=0, column=0, sticky="nsew")
        self.set_local_time()

        self.root.minsize(400, 100)
        self.root.mainloop()

digital_alarm()