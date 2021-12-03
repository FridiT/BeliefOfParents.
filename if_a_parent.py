# Import the required library and classes
from tkinter import *


class IfAParent:
    def __init__(self, master):
        self.question = "Do you have a child?"
        self.master = master

    # Auxiliary functions
    def ask_user(self):
        ask_window = Toplevel()
        ask_window.grab_set()
        ask_window.geometry("350x120")
        ask_window.resizable(False, False)
        ask_window.title("Please click your choice:")
        Frame(ask_window, background="#34A2FE", width=350, height=60, pady=3).grid(row=0, sticky="ewn", columnspan=2)
        Label(ask_window, text=self.question, background="#34A2FE", font=("black", 14)).grid(row=0, sticky="ew")

        def answer():
            ask_window.destroy()
            ans = Toplevel()
            ans.grab_set()
            ans.geometry("250x227")
            ans.resizable(False, False)
            ans.title("Bye")
            ans.configure(bg="#34A2FE")
            text_bye = "\nOK. You really don't need this \nheadache now (: " \
                       "\nWe will be happy to help you when\n you will need us.\n\nGoodbye!!\n\n\n\n"
            label1 = LabelFrame(ans, text="So...", width=350, height=120, background="#34A2FE", font=("black", 14))
            label1.grid(sticky="enws")
            label2 = Label(label1, text=text_bye, background="#34A2FE", font=("black", 11))
            label2.grid(sticky="enws")
            label2.after(6000, ans.destroy)

        def beginning():
            self.master.status = "a_parent"
            ask_window.destroy()
            self.master.ch.gender_and_name()

        Label(ask_window, text="").grid(row=1, columnspan=2)
        Button(ask_window, text="Yes", font=('Helvetica bold', 11), padx=35, pady=1,
               command=beginning).grid(row=2, column=0)
        Button(ask_window, text="No", font=('Helvetica bold', 11), padx=35, pady=1, command=answer).grid(row=2,
                                                                                                         column=1)

