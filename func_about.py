from tkinter import *
from idlelib.tooltip import Hovertip

def about(self):
    about_window = Toplevel()
    about_window.grab_set()
    about_window.geometry("680x320")
    about_window.configure(background="#34A2FE")
    about_window.resizable(False, False)
    about_window.title("About " + self.about_what)
    # text_title = ""
    url = ""
    if self.about_what == "Shefer Approach":
        text_title = "What is the Shefer approach?"
        url = "https://merkaz-shefer.org/english/"
    elif self.about_what == "Me":
        text_title = "This is me:"
        url = "www.linkedin.com/in/fridi-taichman"
    else:
        text_title = "This is a story of this project:"
    label_about = LabelFrame(about_window, text=text_title, padx=15, pady=6, width=680, height=320,
                             background="#34A2FE", font=("black", 14))
    label_about.grid(row=0, column=0, sticky="ewsn")
    about_file = open(self.about_what + ".txt", "r")
    text = "Sorry... We have a problem\nIn the meantime you can read about " \
           + self.about_what + " on the site:\n" + url
    if (about_file.readable()):
        text = about_file.read()
    text_label = Label(label_about, text=text, background="#34A2FE", font=("black", 12))
    text_label.grid(row=0, sticky="e")
    text_label2 = Label(label_about, text=url, background="#34A2FE", fg="blue", cursor="hand2", font=12)
    text_label2.grid(row=1)
    text_label2.bind("<Button-1>", lambda e: webbrowser.open_new(url))
    about_file.close()

