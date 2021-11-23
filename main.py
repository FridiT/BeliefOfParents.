# Import the required libraries
from tkinter import *
from idlelib.tooltip import Hovertip
import webbrowser

import func_about
from func_about import *

class Menu:
    # Setting the main window
    def __init__(self, master):
        self.master = master
        master.title("Trust as a sleeping aid for children")
        self.title_of_main = Label(master, text="How to help your child fall a sleep, using the Shefer Method",
                                   font=('Helvetica bold', 18),
                                   padx=120, pady=50, background="#34A2FE", borderwidth=7).grid(row=0, column=0,
                                                                                                columnspan=3)

        self.button_starting_parent = Button(master, text="I want to start from the beginning",
                                             font=('Helvetica bold', 11), padx=45, pady=30,
                                             command=self.click_button_starting_parent).grid(row=1, column=0)
        self.button_practiced_parent = Button(master, text="I'm here again and need you", font=('Helvetica bold', 11),
                                              padx=45, pady=30, command=self.begin).grid(row=1, column=1)
        self.button_for_reminder = Button(master, text="I'm just need a little reminder", font=('Helvetica bold', 11),
                                          padx=45, pady=30, command=self.click_button_to_reminder).grid(row=1, column=2)
        self.button_about_shefer_approach = Button(master, text="About Shefer Approach", font=('Helvetica bold', 11),
                                                   padx=75, pady=30,
                                                   command=self.click_button_about_shefer_approach).grid(row=2,
                                                                                                         column=0)
        self.button_about_this_project = Button(master, text="About this project", font=('Helvetica bold', 11), padx=79,
                                                pady=30, command=self.click_button_about_project).grid(row=2, column=1)
        self.button_about_me = Button(master, text="About me", font=('Helvetica bold', 11), padx=106, pady=30,
                                      command=self.click_button_about_me).grid(
            row=2, column=2)

    # Setting a 'global' variables
    about_what = ""
    status = ""
    optionalProblemAndSolution = ["hungry", "thirsty", "dirty"]
    the_gender = "gender"
    only_gander = "child"
    gender = "your child"
    gender_y = "your child"
    gender_first = ""
    belong = "his"
    to_ = "him"
    level = 0
    select_check_b = False
    get_hungry = False
    get_thirst = False
    get_dirty = False
    ready = False
    hungry = False
    thirst = False
    dirty = False

    get_gender = False
    get_age = False
    finish = False

    # Setting the click function
    def click_button_starting_parent(self):
        self.ask_user("Do you have a child?")

    def begin(self):
        self.status = "a parent"
        self.gender_and_age()

    def click_button_to_reminder(self):
        self.status = "reminder"
        self.gender_and_age()

    def click_button_about_shefer_approach(self):
        self.about_what = "Shefer Approach"
        func_about.about(self)
        #self.about()

    def click_button_about_project(self):
        self.about_what = "This Project"
        func_about.about(self)
        #self.about()

    def click_button_about_me(self):
        self.about_what = "Me"
        func_about.about(self)
        #self.about()

    # Auxiliary functions
    def ask_user(self, question):
        ask_window = Toplevel()
        ask_window.grab_set()
        ask_window.geometry("350x120")
        ask_window.resizable(False, False)
        ask_window.title("Please click your choice:")
        Frame(ask_window, background="#34A2FE", width=350, height=60, pady=3).grid(row=0, sticky="ewn", columnspan=2)
        Label(ask_window, text=question, background="#34A2FE", font=("black", 14)).grid(row=0, sticky="ew")

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
            main.after(10000, main.destroy)

        def beginning():
            self.status = "a parent"
            ask_window.destroy()
            self.gender_and_age()

        Label(ask_window, text="", ).grid(row=1, columnspan=2)
        Button(ask_window, text="Yes", font=('Helvetica bold', 11), padx=35, pady=1,
               command=beginning).grid(row=2, column=0)
        Button(ask_window, text="No", font=('Helvetica bold', 11), padx=35, pady=1, command=answer).grid(row=2,
                                                                                                         column=1)

    def a_parent(self):
        par = Toplevel()
        self.hungry = self.dirty = self.thirst = False
        self.get_dirty = self.get_thirst = self.get_hungry = False
        par.grab_set()
        par.geometry("580x270")
        par.configure(bg="#34A2FE")
        par.resizable(False, False)
        par.title("It all starts in your head")
        text_title = "Here are some questions to better understand your situation.\
        \nIn the following questions, please choose Yes or No:"
        label0 = LabelFrame(par, text=text_title, width=800, height=200, background="#34A2FE", font=("black", 14))
        label0.grid()
        index = 0
        len_of_problem = int(len(self.optionalProblemAndSolution))
        while index < len_of_problem:
            the_problem = self.optionalProblemAndSolution[index]
            problem = "My " + self.only_gander + " is " + the_problem + "?"
            Label(label0, text=problem, pady=7, padx=5, background="#34A2FE", font=("black", 11)).grid(row=index,
                                                                                                       column=0,
                                                                                                       sticky="W")
            index += 1
        # parameter for radioButton
        hun = par.var = StringVar()
        thi = par.var = StringVar()
        ddir = par.var = StringVar()
        hun.set(value="a")
        thi.set(value="a")
        ddir.set(value="a")

        # Setting the conclusion from the user answer
        def ready_conclusion():
            if self.get_thirst is True and self.get_hungry is True and self.get_dirty is True:
                self.ready = True
                if self.hungry is False and self.dirty is False and self.thirst is False:
                    text_conclusion = " WOW. " + self.gender_first + " really ready to sleep!!"
                    text_finish = "Your are ready to the next level"
                elif self.hungry is True and self.dirty is True and self.thirst is True:
                    text_finish = "I took care of my kid\n" + self.gender + " is ready for sleep!"
                    text_conclusion = "Hemm, you should check again if " + self.gender_y + " is ready to sleep..."

                else:
                    text_finish = "I followed the recommendations, " + self.gender + " is ready for sleep!"
                    text_conclusion = "OK. Here is the answer: "
                    if self.hungry is True:
                        text_conclusion += "Give " + self.to_ + " to eat"
                        if self.thirst is True:
                            text_conclusion += " and drink"
                        elif self.dirty is True:
                            text_conclusion = "OK, give " + self.to_ + " to eat and clean " + self.to_
                    elif self.dirty is True:
                        text_conclusion = "Please clean " + self.to_
                        if self.thirst is True:
                            text_conclusion += " and give " + self.to_ + " to drink"
                    elif self.thirst is True:
                        text_conclusion += "give " + self.to_ + " to drink"
                label1.destroy()
                label_con = LabelFrame(label0, text=text_conclusion, width=400, height=100,
                                       font=("black", 13))
                label_con.grid(sticky="ews", row=3, column=0, columnspan=3)
                check_b = Checkbutton(label_con, text=text_finish, command=fin1, font=('Helvetica bold', 9))
                check_b.grid(row=0, sticky="w")
                Button(label_con, text="Press here!", background="#34A2FE", font=('Helvetica bold', 11),
                       padx=20, pady=5, command=fin).grid(padx=55, pady=5, row=1)

        def fin1():
            self.select_check_b = True
            return

        def fin():
            self.status = "from_beginning"
            par.destroy()
            self.reminder()

        def hun1():
            self.get_hungry = True
            if hun.get() == "True":
                self.hungry = True
            ready_conclusion()

        def thi1():
            self.get_thirst = True
            if thi.get() == "True":
                self.thirst = True
            ready_conclusion()

        def ddir1():
            self.get_dirty = True
            if ddir.get() == "True":
                self.dirty = True
            ready_conclusion()

        Radiobutton(label0, text="Yes", value="True", variable=hun, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=hun1).grid(row=0, column=1)
        Radiobutton(label0, text="No", value="False", variable=hun, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=hun1).grid(row=0, column=2)
        Radiobutton(label0, text="Yes", value="True", variable=thi, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=thi1).grid(row=1, column=1)
        Radiobutton(label0, text="No", value="False", variable=thi, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=thi1).grid(row=1, column=2)
        Radiobutton(label0, text="Yes", value="True", variable=ddir, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=ddir1).grid(row=2, column=1)
        Radiobutton(label0, text="No", value="False", variable=ddir, pady=7, padx=5, background="#34A2FE",
                    font=("black", 11), command=ddir1).grid(row=2, column=2)

        label1 = LabelFrame(label0, text="Here will be our recommendation:)", width=400, height=100,
                            background="#34A2FE",
                            font=("black", 14))
        label1.grid(sticky="enws", row=3, column=1, columnspan=2)

    def gender_and_age(self):
        gender_window = Toplevel()
        gender_window.grab_set()
        gender_window.geometry("333x245")
        gender_window.resizable(False, False)
        gender_window.title("Some technical details:")
        Label(gender_window, text="Do you have a girl or a boy?", font=('Helvetica bold', 14), padx=50, pady=13,
              background="#34A2FE", borderwidth=5).grid(row=0, column=0, columnspan=2)

        def sel():
            if str(v.get()) != "chil":
                self.the_gender = str(v.get())
                self.get_gender = True

                if self.get_age is True and self.get_gender is True:
                    Button(gender_window, text="I finished", background="#34A2FE", font=('Helvetica bold', 11), padx=35,
                           pady=1, command=fin).grid(row=5, column=0, columnspan=2)
                    self.finish = True

        def age(x):
            self.level = a.get()
            self.get_age = True
            self.finish = True
            if self.get_age is True and self.get_gender is True:
                self.finish = True
                Button(gender_window, text="I finished", background="#34A2FE", font=('Helvetica bold', 11),
                       padx=35, pady=1, command=fin).grid(row=5, column=0, columnspan=2)

        def fin():
            self.gender_f()
            if self.finish is True:
                gender_window.destroy()
                if self.status == "reminder":
                    self.reminder()
                elif self.status == "a parent":
                    self.a_parent()

        v = gender_window.var = StringVar()
        v.set("chil")
        Radiobutton(gender_window, text="Girl", font=('Helvetica bold', 11), variable=v,
                    value="girl", command=sel).grid(row=1, column=0)
        Radiobutton(gender_window, text="Boy", font=('Helvetica bold', 11), variable=v, value="boy",
                    command=sel).grid(row=1, column=1)
        Radiobutton(gender_window, text="I am not sure about my child's gender",
                    font=('Helvetica bold', 11), variable=v, value="child", command=sel).grid(row=2,
                                                                                              column=0,
                                                                                              columnspan=2)
        Label(gender_window, text="What is your kid's age?", font=('Helvetica bold', 14),
              padx=50, pady=13, background="#34A2FE", borderwidth=7).grid(row=3, column=0,
                                                                          columnspan=2, sticky="we")
        a = gender_window.var = IntVar()
        a.set(0)
        option_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        OptionMenu(gender_window, a, *option_tuple, command=age).grid(row=4, column=0, columnspan=2)
        Button(gender_window, text="I finished", state=DISABLED, background="#34A2FE",
               font=('Helvetica bold', 11), padx=35, pady=1, command=fin).grid(row=5, column=0, columnspan=2)

    def gender_f(self):
        if str(self.the_gender) == "boy":
            self.gender = "he"
            self.gender_first = "He"
            self.belong = "his"
            self.to_ = "him"
        elif str(self.the_gender) == "girl":
            self.gender = "she"
            self.gender_first = "She"
            self.belong = self.to_ = "her"
        elif self.level < 3:
            self.gender = "my baby"
            self.gender_first = "My baby"
        else:
            self.gender = "my child"
            self.gender_y = "your child"
            self.gender_first = "My child"

    def reminder(self):
        rem = Toplevel()
        rem.grab_set()
        if self.gender == "my child" or self.gender == "my baby":
            rem.geometry("333x225")
        else:
            rem.geometry("250x227")
        rem.configure(bg="#34A2FE")
        rem.resizable(False, False)
        rem.title("It all starts in your head")
        if self.status == "from_beginning":
            all_title = "Repeat the following calmly \nuntil you believe the statements:"
        else:
            all_title = "Here's the reminder, memorize \nthe following calmly \nuntil you believe the statements:"

        all_text = self.gender_first + "'s tired."
        all_label1 = LabelFrame(rem, text=all_title, padx=15, pady=6, width=350, height=120, background="#34A2FE",
                                font=("black", 11))
        all_label1.grid(row=0, column=0, padx=15, pady=10, sticky="ew")
        all_label2 = Label(all_label1, text=all_text, background="#34A2FE", font=("black", 15))
        all_label2.grid(row=0)

        want_title = self.gender_first + " wants to sleep."
        want_text = self.gender_first + "'s tired, " + self.gender + " wants\
        \nto sleep, " + self.belong + " body wants to sleep.\n" + self.gender_first + " just wants to sleep."
        want_label2 = Label(all_label1, text=want_title, background="#34A2FE", font=("black", 15))
        want_label2.grid(row=1)
        Hovertip(want_label2, want_text)

        can_title = self.gender_first + " can sleep."
        can_text = "Everything is fine, comfortable for\n" \
                   + self.to_ + ", the lighting is fine, also the\ntemperature - " \
                   + self.gender + " has the good conditions \nfor sleeping."
        can_label2 = Label(all_label1, text=can_title, background="#34A2FE", font=("black", 15))
        can_label2.grid(row=2)
        Hovertip(can_label2, can_text)

        need_title = self.gender_first + " needs to sleep."
        need_text = self.gender_first + "'s tired, now it's " + self.belong + " bedtime!"
        need_label2 = Label(all_label1, text=need_title, background="#34A2FE", font=("black", 15))
        need_label2.grid(row=3)
        Hovertip(need_label2, need_text)

        last_text = self.gender_first + " sleeps!!"
        last2_text = "Finally!!"
        last_label2 = Label(all_label1, text=last_text, background="#34A2FE", font=("black", 15))
        last_label2.grid(row=4)
        Hovertip(last_label2, last2_text)


# Main
main = Tk()
main.resizable(False, False)
main.title("How to think that the child will fall asleep?")
my_gui = Menu(main)
main.mainloop()
