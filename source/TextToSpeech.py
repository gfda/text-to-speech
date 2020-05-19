#! /usr/bin/python3
#
#@author Gustavo Dias A.

import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from gtts import gTTS 


"""Background, text color and language"""
BG_COLOR = "#33334d"
TXT_COLOR = "#d9d9d9"
LANGUAGE = 'en'

class Application:

    def __init__(self, master=None):
        
        root.title("Text to Speech")
        
        self.main_window = LabelFrame(master, text="Text to Speech in Python", bg=BG_COLOR, fg=TXT_COLOR)
        self.main_window.pack(fill="both", expand="yes")
        
        """FIRST CONTAINER"""
        self.first_container = Frame(self.main_window, pady=10, bg=BG_COLOR)
        self.first_container.pack()

        self.lbl_title = Label(self.first_container, text="Text to Speec - Using gTTS ", font="impact 16", bg=BG_COLOR, fg=TXT_COLOR)
        self.lbl_title.pack()

        """SECOND CONTAINER"""
        self.second_container = Frame(self.main_window, padx=20, bg=BG_COLOR)
        self.second_container.pack()

        self.lbl_input_text = Label(self.second_container, text="Input text", bg=BG_COLOR, fg=TXT_COLOR)
        self.lbl_input_text.pack(side=LEFT)

        self.entry_input_text = Entry(self.second_container)
        self.entry_input_text.pack(side=RIGHT)

        """THIRD CONTAINER"""
        self.third_container = Frame(self.main_window, pady=20, bg=BG_COLOR)
        self.third_container.pack()

        self.btn_exit = ttk.Button(self.third_container, text="Exit", command=self.main_window.quit)
        self.btn_exit.pack(side=RIGHT, anchor="s") 

        self.btn_select = ttk.Button(self.third_container, text='Speech', command=self.speak_text)
        self.btn_select.pack(side=LEFT, anchor="s") 

    def speak_text(self):
        """Gets the text from entry_input_text, converts it using gTTS (Google Text To Speech)
         and reproduces using the operating system command"""
        typed_text = self.entry_input_text.get()
        
        if typed_text:
            output_audio = gTTS(text=typed_text, lang=LANGUAGE, slow=False)
            output_audio.save("sound/output.mp3")
       
            try:
                os.system("afplay sound/output.mp3")
            except OSError as err:
                messagebox.showerror("Error", "Please, check if your play command is right. OS Error: {0}".format(err))
        else:
            messagebox.showerror("Error", "This field cannot be empty!")
        
root = Tk()
Application(root)
root.mainloop()
