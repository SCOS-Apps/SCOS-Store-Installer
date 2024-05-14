import pathlib
import tkinter as tk
import pygubu
import requests
from __installer__ui import rootUI
import time

class root(rootUI):
    global checkbox
    global install_button
    global copy
    install_button = 0
    checkbox = 1
    def __init__(self, master=None):
        self.builder = pygubu.Builder()
        self.master = master
        super().__init__(master)
    
    def copy(self):
        pass

    def on_button1_click(self):
        self.mainwindow.destroy()
        self.mainwindow: tk.Tk = self.builder.get_object("tk2", self.master)

    def on_checkbox(self):
        global checkbox
        if checkbox == 0:
            print(self.builder.get_object("button1").state())
            self.builder.get_object("button1").configure(state='disabled')
            checkbox = 1
        else:
            print(self.builder.get_object("button1").state())
            self.builder.get_object("button1").configure(state='normal')
            checkbox = 0

    def on_command1_click(self):
        exit()


if __name__ == "__main__":
    app = root()
    app.run()
