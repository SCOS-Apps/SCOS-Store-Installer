#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
import time

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "scos.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class rootUI:
    def __init__(self, master=None):
        self.master = master
        self.builder = pygubu.Builder()
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: tk.Tk = self.builder.get_object("tk1", master)
        # Main menu
        _main_menu = self.builder.get_object("menu1", self.mainwindow)
        self.mainwindow.configure(menu=_main_menu)
        self.builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def on_button1_click(self):
        pass

    def on_checkbox(self):
        pass

    def on_command1_click(self):
        pass


if __name__ == "__main__":
    app = rootUI()
    app.run()
