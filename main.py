# Import the required library and classes
from tkinter import *
from about import AboutMe, AboutThisProject, AboutSheferApproach
from child import Child
from a_parent import Parent
from reminder import Reminder
from if_a_parent import IfAParent


class Menu:
    def __init__(self, master):
        # Setting a variables that I use in all the program
        self.master = master
        self._status = ""
        self._about_what = ""
        self.re = Reminder(self, self.status)
        self.ch = Child(self)
        self.pa = Parent(master, self.ch)

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
               command=self.click_button_to_begin).grid(row=1, column=1)
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
        a = IfAParent(self)
        a.ask_user()

    def click_button_to_begin(self):
        self.status = "a_parent"
        self.ch.gender_and_name()

    def click_button_to_reminder(self):
        self.status = "reminder"
        self.ch.gender_and_name()

    # Call to About class and open the about window
    def click_button_about_me(self):
        about = AboutMe()
        about.make_a_window()

    def click_button_about_shefer_approach(self):
        about = AboutSheferApproach()
        about.make_a_window()

    def click_button_about_project(self):
        about = AboutThisProject()
        about.make_a_window()


# Main
def main():
    main = Tk()
    m = Menu(main)
    m.open_main_window()


if __name__ == '__main__':
    main()
    mainloop()
