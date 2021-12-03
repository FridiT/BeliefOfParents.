# Import the required libraries
from tkinter import *
import webbrowser


class AboutWindow:
    def __init__(self, about_what, text_title, url=''):
        self.url = url
        self.about_what = about_what
        self.text_title = text_title

    def make_a_window(self):
        about_window = Toplevel()
        about_window.grab_set()
        about_window.geometry("680x320")
        about_window.configure(background="#34A2FE")
        about_window.resizable(False, False)
        about_window.title("About " + self.about_what)
        label_about = LabelFrame(about_window, text=self.text_title, padx=15, pady=6, width=680, height=320,
                                 background="#34A2FE", font=("black", 14))
        label_about.grid(row=0, column=0, sticky="ewsn")
        for_about_file = self.about_what + ".txt"
        if self.about_what:
            about_file = open(for_about_file, "r")
            text = "Sorry... We have a problem\nIn the meantime you can read about " \
                   + self.about_what + " on the site:\n" + self.url
            if about_file.readable():
                text = about_file.read()
            text_label = Label(label_about, text=text, background="#34A2FE", font=("black", 12))
            text_label.grid(row=0, sticky="e")
            text_label2 = Label(label_about, text=self.url, background="#34A2FE", fg="blue", cursor="hand2", font=12)
            text_label2.grid(row=1)
            text_label2.bind("<Button-1>", lambda e: webbrowser.open_new(self.url))
            about_file.close()


class AboutMe(AboutWindow):
    def __init__(self):
        url = "www.linkedin.com/in/fridi-taichman"
        text_title = "This is me:"
        super(AboutMe, self).__init__("Me", text_title, url)


class AboutSheferApproach(AboutWindow):
    def __init__(self):
        url = "https://merkaz-shefer.org/english/"
        text_title = "What is the Shefer approach?"
        super(AboutSheferApproach, self).__init__("Shefer Approach", text_title, url)


class AboutThisProject(AboutWindow):
    def __init__(self):
        text_title = "This is a story of this project:"
        super(AboutThisProject, self).__init__("This Project", text_title)


"""
# Import the required libraries
from tkinter import *
import webbrowser


class About:
    def __init__(self):
        self.url = ""

    def about(self, about_what):
        about_window = Toplevel()
        about_window.grab_set()
        about_window.geometry("680x320")
        about_window.configure(background="#34A2FE")
        about_window.resizable(False, False)
        about_window.title("About " + about_what)
        if about_what == "Shefer Approach":
            text_title = "What is the Shefer approach?"
            self.url = "https://merkaz-shefer.org/english/"
        elif about_what == "Me":
            text_title = "This is me:"
            self.url = "www.linkedin.com/in/fridi-taichman"
        else:
            text_title = "This is a story of this project:"
        label_about = LabelFrame(about_window, text=text_title, padx=15, pady=6, width=680, height=320,
                                 background="#34A2FE", font=("black", 14))
        label_about.grid(row=0, column=0, sticky="ewsn")
        for_about_file = about_what + ".txt"
        if about_what:
            about_file = open(for_about_file, "r")
            text = "Sorry... We have a problem\nIn the meantime you can read about " \
                   + about_what + " on the site:\n" + self.url
            if about_file.readable():
                text = about_file.read()
            text_label = Label(label_about, text=text, background="#34A2FE", font=("black", 12))
            text_label.grid(row=0, sticky="e")
            text_label2 = Label(label_about, text=self.url, background="#34A2FE", fg="blue", cursor="hand2", font=12)
            text_label2.grid(row=1)
            text_label2.bind("<Button-1>", lambda e: webbrowser.open_new(self.url))
            about_file.close()
"""
