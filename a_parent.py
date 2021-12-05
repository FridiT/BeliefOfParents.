# Import the required libraries and classes
from tkinter import *
from reminder import Reminder


class Parent:
    # constructor. Setting the parent attributes
    def __init__(self, master, ga):
        self.master = master
        self.ga = ga
        self.hungry = self.dirty = self.thirst = False
        self.get_dirty = self.get_thirst = self.get_hungry = False
        self.optionalProblemAndSolution = ["hungry", "thirsty", "dirty"]
        self.select_check_b = False
        self.get_hungry = False
        self.get_thirst = False
        self.get_dirty = False
        self.ready = False
        self.hungry = False
        self.thirst = False
        self.dirty = False
        self.check_b = Checkbutton()

    def a_parent(self):
        self.hungry = self.dirty = self.thirst = False
        self.get_dirty = self.get_thirst = self.get_hungry = False
        self.check_b.deselect()
        par = Toplevel()
        par.grab_set()
        par.geometry("580x270")
        par.configure(bg="#34A2FE")
        par.resizable(False, False)
        par.title("It all starts in your head")
        text_title = "Here are some questions to better understand the situation.\
        \nIn the following questions, please choose Yes or No:"
        label0 = LabelFrame(par, text=text_title, width=800, height=200, background="#34A2FE", font=("black", 14))
        label0.grid()
        index = 0
        len_of_problem = int(len(self.optionalProblemAndSolution))
        while index < len_of_problem:
            the_problem = self.optionalProblemAndSolution[index]
            problem = f"Is {self.ga.name} {the_problem}?"
            Label(label0, text=problem, pady=7, padx=5, background="#34A2FE",
                  font=("black", 11)).grid(row=index, column=0, sticky="W")
            index += 1
        # parameter for radioButton
        hun = par.var = StringVar()
        thi = par.var = StringVar()
        dirt = par.var = StringVar()
        hun.set(value="a")
        thi.set(value="a")
        dirt.set(value="a")

        # Check if the user changed the options
        def check_change():
            if self.select_check_b:
                self.select_check_b = self.ready = False
                self.check_b.deselect()

        # Check if is child hungry
        def hun1():
            self.get_hungry = True
            check_change()
            self.hungry = True if hun.get() == "True" else False
            self.ready_conclusion(label0, label1, par)

        # Check if is child thirst
        def thi1():
            self.get_thirst = True
            check_change()
            self.thirst = True if thi.get() == "True" else False
            self.ready_conclusion(label0, label1, par)

        # Check if is child dirty
        def dir1():
            self.get_dirty = True
            check_change()
            self.dirty = True if dirt.get() == "True" else False
            self.ready_conclusion(label0, label1, par)

        Radiobutton(label0, text="Yes", value="True", variable=hun, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=hun1).grid(row=0, column=1)
        Radiobutton(label0, text="No", value="False", variable=hun, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=hun1).grid(row=0, column=2)
        Radiobutton(label0, text="Yes", value="True", variable=thi, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=thi1).grid(row=1, column=1)
        Radiobutton(label0, text="No", value="False", variable=thi, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=thi1).grid(row=1, column=2)
        Radiobutton(label0, text="Yes", value="True", variable=dirt, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=dir1).grid(row=2, column=1)
        Radiobutton(label0, text="No", value="False", variable=dirt, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=dir1).grid(row=2, column=2)

        label1 = LabelFrame(label0, text="Here will be our recommendation:)", width=400, height=100,
                            background="#34A2FE",
                            font=("black", 14))
        label1.grid(sticky="enws", row=3, column=1, columnspan=2)

    # Setting the conclusion from the user answer about child needs
    def ready_conclusion(self, label0, label1, par):
        # Its True when a user choose V in a checkbutton
        def fin1():
            self.select_check_b = True if self.ready else False
            return

        # Finish the window of 'parent' and continue to the window of a reminder
        def fin():
            if self.select_check_b:
                self.master.status = "from_beginning"
                par.destroy()
                re = Reminder(self.ga, self.master.status)
                re.reminder(self.ga)

        self.check_b.deselect()
        if self.get_thirst is True and self.get_hungry is True and self.get_dirty is True:
            self.ready = True
            if self.hungry is False and self.dirty is False and self.thirst is False:
                text_conclusion = f"WOW. {self.ga.name} really ready to sleep!!"
                text_finish = "I'm ready to the next level"
            elif self.hungry is True and self.dirty is True and self.thirst is True:
                text_finish = f"I took care of {self.ga.name}, {self.ga.gender} is ready for sleep!"
                text_conclusion = f"Hemm, you should check again if {self.ga.name} is ready to sleep..."
            else:
                text_finish = f"I followed the recommendations, {self.ga.name} is ready for sleep!"
                text_conclusion = "OK. Here is the answer: "
                if self.hungry is True:
                    text_conclusion += f"Give {self.ga.to_} to eat"
                    if self.thirst is True:
                        text_conclusion += " and drink"
                    elif self.dirty is True:
                        text_conclusion = f"OK, give {self.ga.to_} to eat and clean {self.ga.to_}"
                elif self.dirty is True:
                    text_conclusion = f"Please clean {self.ga.to_}"
                    if self.thirst is True:
                        text_conclusion += f" and give {self.ga.to_} to drink"
                elif self.thirst is True:
                    text_conclusion += f"give {self.ga.to_} to drink"
            label1.destroy()
            label_con = LabelFrame(label0, text=text_conclusion, width=400, height=100,
                                   font=("black", 13))
            label_con.grid(sticky="ews", row=3, column=0, columnspan=3)
            self.check_b = Checkbutton(label_con, text=text_finish, command=fin1, font=('Helvetica bold', 9))
            self.check_b.deselect()
            self.check_b.grid(row=0, sticky="w")
            Button(label_con, text="Press here!", background="#34A2FE", font=('Helvetica bold', 11),
                   padx=20, pady=5, command=fin).grid(padx=55, pady=5, row=1)
