# Import the required libraries and classes
from tkinter import *
from reminder import Reminder
from a_parent import Parent


class GenderAge:
    def __init__(self, main_win):
        self.master = main_win
        self._name = ""
        self.the_gender = "gender"
        self.only_gander = "child"
        self.gender = "your child"
        self.gender_y = "your child"
        self.gender_first = ""
        self.belong = "his"
        self.to_ = "him"
        self.level = 0
        self.get_gender = False
        self.get_name = False
        self.finish = False
        self.bu = Button()

    # Using @property decorator for an important variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = (value.lower()).capitalize()
        self._name = value

    def gender_and_age(self):
        self.get_name = False
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
                if self.get_name is True and self.get_gender is True:
                    Button(gender_window, text="I finished", background="#34A2FE", font=('Helvetica bold', 11), padx=35,
                           pady=1, command=fin).grid(row=5, column=0, columnspan=2, sticky="we")
                    self.finish = True
                else:
                    check_name()

        def check_name():
            name = na.get()
            msg = ''
            if len(name) == 0:
                msg = 'Name can\'t be empty'
            else:
                try:
                    import string
                    if any(ch.isdigit() for ch in name) or any(ch in string.punctuation for ch in name):
                        msg = 'Please write a valid name!'# ,\nname can\'t have a numbers or a punctuation'
                        Label(gender_window, text=msg, font=('Helvetica bold', 14), padx=50, pady=13,
                              background="#34A2FE", borderwidth=7).grid(row=3, column=0, columnspan=2, sticky="we")
                    elif len(name) < 2:
                        msg = 'Name is too short...'
                        Label(gender_window, text=msg, font=('Helvetica bold', 14), padx=50, pady=13,
                              background="#34A2FE", borderwidth=7).grid(row=3, column=0, columnspan=2, sticky="we")
                    else:
                        self.name = name
                        msg = self.name + ' is a valid name'
                        self.get_name = True
                        Label(gender_window, text=msg, font=('Helvetica bold', 14), padx=50, pady=13,
                              background="#34A2FE", borderwidth=7).grid(row=3, column=0, columnspan=2, sticky="we")
                        Entry(gender_window, stat=DISABLED).grid(row=4, column=0, columnspan=2)
                        if self.get_name is True and self.get_gender is True:
                            self.finish = True
                            Button(gender_window, text="I finished", background="#34A2FE", font=('Helvetica bold', 11),
                                   padx=35, pady=1, command=fin).grid(row=5, column=0, columnspan=2, sticky="we")
                        else:
                            Button(gender_window, text="I finished", stat=DISABLED, background="#34A2FE",
                                   font=('Helvetica bold', 11),
                                   padx=35, pady=1, command=fin).grid(row=5, column=0, columnspan=2, sticky="we")
                except Exception as ep:
                    print('error ', ep)
            mainloop()

        def fin():
            self.gender_f()
            na1 = Entry(gender_window, stat=DISABLED).grid(row=4, column=0, columnspan=2)
            if self.finish:
                gender_window.destroy()
                if self.master.status == "reminder":
                    re = Reminder(self, self.master.status)
                    re.reminder(self)
                elif self.master.status == "a_parent":
                    pa = Parent(self.master, self)
                    pa.a_parent()

        v = gender_window.var = StringVar()
        v.set("chil")
        Radiobutton(gender_window, text="Girl", font=('Helvetica bold', 11), variable=v,
                    value="girl", command=sel).grid(row=1, column=0)
        Radiobutton(gender_window, text="Boy", font=('Helvetica bold', 11), variable=v, value="boy",
                    command=sel).grid(row=1, column=1)
        Radiobutton(gender_window, text="I am not sure about my child's gender", font=('Helvetica bold', 11),
                    variable=v, value="child", command=sel).grid(row=2, column=0, columnspan=2)
        Label(gender_window, text="What is your kid's name?", font=('Helvetica bold', 14),
              padx=50, pady=13, background="#34A2FE", borderwidth=7).grid(row=3, column=0, columnspan=2, sticky="we")

        na = Entry(gender_window)
        na.grid(row=4, column=0, columnspan=2)
        b_check = Button(gender_window, text="Check my child's name", background="#34A2FE",
                         font=('Helvetica bold', 11), padx=35, pady=1, command=check_name)
        b_check.grid(row=5, column=0, columnspan=2, sticky="we")

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



"""
# Import the required libraries and classes
from tkinter import *
from reminder import Reminder
from a_parent import Parent


class GenderAge:
    def __init__(self, main_win):
        self.master = main_win
        self.the_gender = "gender"
        self.only_gander = "child"
        self.gender = "your child"
        self.gender_y = "your child"
        self.gender_first = ""
        self.belong = "his"
        self.to_ = "him"
        self.level = 0
        self.get_gender = False
        self.get_age = False
        self.finish = False

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
            if self.finish:
                gender_window.destroy()
                if self.master.status == "reminder":
                    re = Reminder(self, self.master.status)
                    re.reminder(self)
                elif self.master.status == "a_parent":
                    pa = Parent(self.master, self)
                    pa.a_parent()

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


"""


"""
        def check_name():
            valid = False
            name = na.get()
            while not valid:
                valid = True
                for i in range(len(name)):
                    if not name[i].isalpha():
                        valid = False
                if valid and valid != "":
                    self.name = name
                    self.get_age = True
                    if self.get_age is True and self.get_gender is True:
                        self.finish = True
                        Button(gender_window, text="I finished", background="#34A2FE", font=('Helvetica bold', 11),
                               padx=35, pady=1, command=fin).grid(row=5, column=0, columnspan=2, sticky="we")
                else:
                    na1 = Entry(gender_window, textvariable=entry_str)
                    na1.bind('<KeyRelease>', lambda _: check_name())
                    #na1 = Entry(gender_window, text="Pls write only valid letters")
                    na1.grid(row=4, column=0, columnspan=2)
                    name = na1.get()
                    Button(gender_window, text="Check me again", background="#34A2FE", font=('Helvetica bold', 11),
                           padx=35, pady=1, command=check_name).grid(row=5, column=0, columnspan=2, sticky="we")

        entry_str = StringVar()
        error = StringVar()
        error.set('')
        na = Entry(gender_window, textvariable=entry_str)
        na.bind('<KeyRelease>', lambda _: check_name())
        #self.name = na.get()
        na.grid(row=4, column=0, columnspan=2)
        b_check = Button(gender_window, text="Check my child's name", state=DISABLED, background="#34A2FE",
                font=('Helvetica bold', 11), padx=35, pady=1, command=check_name)
        b_check.grid(row=5, column=0, columnspan=2, sticky="we")
        b_check.wait_variable(entry_str)
        check_name()
        """