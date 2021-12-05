# Import the required libraries and classes.
from tkinter import *
from idlelib.tooltip import Hovertip


class Reminder:
    # constructor
    def __init__(self, master, status):
        self.master = master
        self.status = status

    def reminder(self, ch):
        rem = Toplevel()
        rem.grab_set()
        if ch.gender == "my child":
            rem.geometry("292x225")
        else:
            rem.geometry("250x227")
        rem.configure(bg="#34A2FE")
        rem.resizable(False, False)
        rem.title("It all starts in your head")
        if self.status == "from_beginning":
            all_title = "Repeat the following calmly \nuntil you believe the statements:"
        else:
            all_title = "Here's the reminder, memorize \nthe following calmly \nuntil you believe the statements:"

        all_text = f"{ch.name}'s tired."
        all_label1 = LabelFrame(rem, text=all_title, padx=15, pady=6, width=350, height=120, background="#34A2FE",
                                font=("black", 11))
        all_label1.grid(row=0, column=0, padx=15, pady=10, sticky="ew")
        all_label2 = Label(all_label1, text=all_text, background="#34A2FE", font=("black", 15))
        all_label2.grid(row=0)

        want_title = f"{ch.gender_first} wants to sleep."
        want_text = f"{ch.gender_first}'s tired, {ch.gender} wants\nto sleep, " \
                    f"{ch.belong} body wants to sleep.\n{ch.gender_first} just wants to sleep."
        want_label2 = Label(all_label1, text=want_title, background="#34A2FE", font=("black", 15))
        want_label2.grid(row=1)
        Hovertip(want_label2, want_text)

        can_title = f"{ch.gender_first} can sleep."
        can_text = f"Everything is fine, comfortable for\n{ch.to_}, the lighting is fine, also the\ntemperature - " \
                   f"{ch.name} has the good conditions \nfor sleeping."
        can_label2 = Label(all_label1, text=can_title, background="#34A2FE", font=("black", 15))
        can_label2.grid(row=2)
        Hovertip(can_label2, can_text)

        need_title = f"{ch.gender_first} needs to sleep."
        need_text = f"{ch.name} is tired, now it's {ch.belong} bedtime!"
        need_label2 = Label(all_label1, text=need_title, background="#34A2FE", font=("black", 15))
        need_label2.grid(row=3)
        Hovertip(need_label2, need_text)

        last_text = f"{ch.gender_first} sleeps!!"
        last2_text = "Finally!!"
        last_label2 = Label(all_label1, text=last_text, background="#34A2FE", font=("black", 15))
        last_label2.grid(row=4)
        Hovertip(last_label2, last2_text)
