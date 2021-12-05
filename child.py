# Import the required libraries and classes
from tkinter import *
from reminder import Reminder
from a_parent import Parent


class Child:
    # implementation a Singleton design pattern on Child Class
    _the_gander = "gender"

    # constructor
    def __init__(self, main_win):
        self.master = main_win
        self._name = ""
        self.the_gender = ""
        self.gender, self.gender_first = "your child", ""
        self.belong, self.to_ = "his", "him"
        self.get_gender = self.get_name = self.finish = False
        self.bu = Button()

    # Using @property decorator for an important variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = (value.lower()).capitalize()
        self._name = value

    @property
    def the_gender(self):
        return Child._the_gander

    @the_gender.setter
    def the_gender(self, value):
        Child._the_gander = value

    @staticmethod
    def is_boy():
        if Child._the_gander == "boy":
            return True
        else:
            return False

    @staticmethod
    def is_girl():
        if Child._the_gander == "girl":
            return True
        else:
            return False

    @staticmethod
    def is_a_binary():
        if Child._the_gander == "child":
            return True
        else:
            return False

    # implementation a Singleton design pattern on Child Class
    """       
                if Child._the_gander not in {"gender", ""}:
                    text = f'''This class is a singleton class!\nTherefore, we already have the child gender details saved,
                    you can proceed to the next step'''
                    from tkinter import messagebox
                    messagebox.showinfo('Singleton', text)
                    raise Exception("")
                else:
        """

    def attribute_of_gender(self):
        # gender first, improve to use with capitalize
        if self.is_boy():
            self.gender, self.gender_first, self.belong, self.to_ = "he", "He", "his", "him"
        elif self.is_girl():
            self.gender_first, self.gender = "She", "she"
            self.belong = self.to_ = "her"
        elif self.is_a_binary():
            self.gender_first, self.gender = "My child", "my child"

    def gender_and_name(self):
        def select_gander():
            if str(v.get()) != "chil":
                self.the_gender = str(v.get())
                self.attribute_of_gender()
                self.get_gender = True
                if self.get_name is True and self.get_gender is True:
                    Button(gender_window, text="I finished", background="#34A2FE", font=('Helvetica bold', 11), padx=35,
                           pady=1, command=fin).grid(row=5, column=0, columnspan=2, sticky="we")
                    self.finish = True
                else:
                    if len(entry_name.get()) != 0 and self.get_name:
                        check_name()
            else:
                self.attribute_of_gender()

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
                    msg = f'{self.name} is a valid name'
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

        self.get_name = False
        gender_window = Toplevel()
        gender_window.grab_set()
        gender_window.geometry("333x245")
        gender_window.resizable(False, False)
        gender_window.title("Some technical details:")
        Label(gender_window, text="Do you have a girl or a boy?", font=('Helvetica bold', 14), padx=50, pady=13,
              background="#34A2FE", borderwidth=5).grid(row=0, column=0, columnspan=2)

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
