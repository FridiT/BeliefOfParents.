# Import the required library and classes
from tkinter import *
from about import About
from gender_and_name import GenderName
from a_parent import Parent
from reminder import Reminder
from ask_user import AskUser


class Menu:
    def __init__(self, master):
        # Setting a variables that I use in all the program
        self.master = master
        self._status = ""
        self._about_what = ""
        self.re = Reminder(self, self.status)
        self.ga = GenderName(self)
        self.pa = Parent(master, self.ga)

    # Using @property decorator for an important variables
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        option_of_status = {'from_beginning', 'a_parent', 'reminder'}
        if value not in option_of_status:
            raise ValueError('Error. This name is not in the list of names')
        self._status = value

    @property
    def about_what(self):
        return self._about_what

    @about_what.setter
    def about_what(self, value):
        about_file = {'Me', 'This Project', 'Shefer Approach'}
        if value not in about_file:
            raise ValueError('Error. This name is not in the list of names')
        self._about_what = value

    # Setting the main window
    def open_main_window(self):
        master = self.master
        self.master.resizable(False, False)
        self.master.title("Trust as a sleeping aid for children")
        title_for_label = "How to help your child fall a sleep, using the Shefer Method"
        Label(master, text=title_for_label, font=('Helvetica bold', 18), padx=120, pady=50, background="#34A2FE",
              borderwidth=7).grid(row=0, column=0, columnspan=3)
        Button(master, text="I want to start from the beginning", font=('Helvetica bold', 11), padx=45, pady=30,
               command=self.click_button_starting_parent).grid(row=1, column=0)
        Button(master, text="I'm here again and need you", font=('Helvetica bold', 11), padx=45, pady=30,
               command=self.begin).grid(row=1, column=1)
        Button(master, text="I just need a little reminder", font=('Helvetica bold', 11), padx=52, pady=30,
               command=self.click_button_to_reminder).grid(row=1, column=2)
        Button(master, text="About Shefer Approach", font=('Helvetica bold', 11), padx=75, pady=30,
               command=self.click_button_about_shefer_approach).grid(row=2, column=0)
        Button(master, text="About this project", font=('Helvetica bold', 11), padx=79, pady=30,
               command=self.click_button_about_project).grid(row=2, column=1)
        Button(master, text="About me", font=('Helvetica bold', 11), padx=106, pady=30,
               command=self.click_button_about_me).grid(row=2, column=2)

    # Setting the click function
    def click_button_starting_parent(self):
        self.status = "from_beginning"
        a = AskUser(self)
        a.ask_user()

    def begin(self):
        self.status = "a_parent"
        self.ga.gender_and_name()

    def click_button_to_reminder(self):
        self.status = "reminder"
        self.ga.gender_and_name()

    # Call to class About and open the about window
    def call_about(self):
        ab = About()
        ab.about(self.about_what)

    def click_button_about_shefer_approach(self):
        self.about_what = "Shefer Approach"
        self.call_about()

    def click_button_about_project(self):
        self.about_what = "This Project"
        self.call_about()

    def click_button_about_me(self):
        self.about_what = "Me"
        self.call_about()


# Main
def main():
    main = Tk()
    m = Menu(main)
    m.open_main_window()


if __name__ == '__main__':
    main()
    mainloop()

