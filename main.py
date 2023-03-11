# imports
import platform
import os
import tkinter as tk

# file imports
from cli import CLI

# vars
folder_name = "ModMate"
saved_store_path = "" # path to store all mods
mc_path = "" # minecraft's system path
saved_config_path = "" # program's config path

def main(mode):
    if mode == "gui":
        window = tk.Tk()
        greeting = tk.Label(
            text="Hello World!",
            bg="black",
            fg="white",
            width=100,
            height=10,
        )
        greeting.pack()
        window.mainloop()
    elif mode == "cli":
        cli = CLI
        mc_path = cli.get_mc_path() #init mc_path, cannot be empty
        saved_config_path = config_path()
        saved_store_path = store_path()

def config_path() -> str :
    return os.path.join(mc_path, folder_name, "config.json")

def store_path() -> str :
    return os.path.join(mc_path, folder_name, "Mods")


main("cli")