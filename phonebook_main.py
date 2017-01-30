"""Python 3.6.0
Georgia Barnes
Phonobook Drill demonstrating OOP, tkinter GUI module, using parent child relationships"""

from tkinter import *
import tkinter as tk

#import other modules
import phonebook_gui
import phonebook_func

#frame tkinter class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame config
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        #center app on user's screen
        phonebook_func.center_window(self, 500,300)
        self.master.title("The Tkinter Phonebook Drill")
        self.master.configure(bg = '#f0f0f0')
        #exit window
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load gui widgets
        phonebook_gui.load_gui(self)

if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
                 


