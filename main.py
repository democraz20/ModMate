# imports
import platform
import os
import tkinter as tk

# file imports
from cli import CLI

# more like consts
folder_name = "ModMate"
saved_profiles_name  = "Profiles" # path where all profiles are saved

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
        saved_config_path = config_path(mc_path, folder_name)
        saved_store_path = store_path(mc_path, folder_name)
        print(get_all_profile(mc_path, folder_name))
        # just testing
        try: 
            json = cli.select_profile(mc_path, folder_name)
            desc = json['desc']
            mods = json['mods']
        except Exception as e:
            desc = str(e).replace('\\\\', '\\')
            mods = []
            pass
        print(f"{desc}, Mods: {mods}")

def config_path(mc_path, folder_name) -> str :
    return os.path.join(mc_path, folder_name, "config.json")

def store_path(mc_path, folder_name) -> str :
    return os.path.join(mc_path, folder_name, "Mods")

def get_all_profile(mc_path, folder_name) -> list[str]:
    res = []
    profiles_path = os.path.join(mc_path, folder_name, saved_profiles_name)
    for i in os.listdir(profiles_path):
        if os.path.isfile(os.path.join(profiles_path, i)):
            res.append(i)
    return res

main("cli")