# Import the required libraries
from tkinter import *
import webbrowser


class AboutWindow:
    # constructor
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
        if not self.about_what:
            text = "Sorry... We have a problem..."
            if self.url:
                text += f"\nIn the meantime you can read about {self.about_what} on the site:\n{self.url}"
        else:
            with open(for_about_file, 'r') as about_file:
                text = about_file.read()
            text_label = Label(label_about, text=text, background="#34A2FE", font=("black", 12))
            text_label.grid(row=0, sticky="e")
            text_label_for_url = Label(label_about, text=self.url, background="#34A2FE", fg="blue", cursor="hand2", font=12)
            text_label_for_url.grid(row=1)
            text_label_for_url.bind("<Button-1>", lambda e: webbrowser.open_new(self.url))


class AboutMe(AboutWindow):
    # constructor
    def __init__(self):
        url = "www.linkedin.com/in/fridi-taichman"
        text_title = "This is me:"
        super(AboutMe, self).__init__("Me", text_title, url)


class AboutSheferApproach(AboutWindow):
    # constructor
    def __init__(self):
        url = "https://merkaz-shefer.org/english/"
        text_title = "What is the Shefer approach?"
        super(AboutSheferApproach, self).__init__("Shefer Approach", text_title, url)


class AboutThisProject(AboutWindow):
    # constructor
    def __init__(self):
        text_title = "This is a story of this project:"
        super(AboutThisProject, self).__init__("This Project", text_title)
