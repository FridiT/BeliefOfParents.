# Import the required libraries and classes
from tkinter import *
from reminder import Reminder
from a_parent import Parent


class GenderName:
    def __init__(self, main_win):
        self.master = main_win
        self._name = ""
        self.the_gender = "gender"
        self.gender = "your child"
        self.gender_first = ""
        self.belong = "his"
        self.to_ = "him"
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

    def attribute_of_gender(self):
        if str(self.the_gender) == "boy":
            self.gender = "he"
            self.gender_first = "He"
            self.belong = "his"
            self.to_ = "him"
        elif str(self.the_gender) == "girl":
            self.gender = "she"
            self.gender_first = "She"
            self.belong = self.to_ = "her"
        else:
            self.gender = "my child"
            self.gender_first = "My child"

    def gender_and_name(self):
        self.get_name = False
        gender_window = Toplevel()
        gender_window.grab_set()
        gender_window.geometry("333x245")
        gender_window.resizable(False, False)
        gender_window.title("Some technical details:")
        Label(gender_window, text="Do you have a girl or a boy?", font=('Helvetica bold', 14), padx=50, pady=13,
              background="#34A2FE", borderwidth=5).grid(row=0, column=0, columnspan=2)

        def select_gander():
            self.attribute_of_gender()
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
            name = entry_name.get()
            try:
                import string
                if len(name) == 0:
                    msg = 'Name can\'t be empty'
                    Label(gender_window, text=msg, font=('Helvetica bold', 14), padx=50, pady=13,
                          background="#34A2FE", borderwidth=7).grid(row=3, column=0, columnspan=2, sticky="we")
                elif any(ch.isdigit() for ch in name) or any(ch in string.punctuation for ch in name):
                    msg = 'Please write a valid name!'
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
            Entry(gender_window, stat=DISABLED).grid(row=4, column=0, columnspan=2)
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
                    value="girl", command=select_gander).grid(row=1, column=0)
        Radiobutton(gender_window, text="Boy", font=('Helvetica bold', 11), variable=v, value="boy",
                    command=select_gander).grid(row=1, column=1)
        Radiobutton(gender_window, text="I am not sure about my child's gender", font=('Helvetica bold', 11),
                    variable=v, value="child", command=select_gander).grid(row=2, column=0, columnspan=2)
        Label(gender_window, text="What is your kid's name?", font=('Helvetica bold', 14),
              padx=50, pady=13, background="#34A2FE", borderwidth=7).grid(row=3, column=0, columnspan=2, sticky="we")
        entry_name = Entry(gender_window)
        entry_name.grid(row=4, column=0, columnspan=2)
        b_check = Button(gender_window, text="Check my child's name", background="#34A2FE",
                         font=('Helvetica bold', 11), padx=35, pady=1, command=check_name)
        b_check.grid(row=5, column=0, columnspan=2, sticky="we")
