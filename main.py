# imports
import platform
import os
import tkinter as tk
import ModMate

# file imports
from cli import CLI

# more like consts
folder_name = "ModMate"
saved_profiles_name  = "Profiles" # path where all profiles are saved

# .minecraft/
# ├─ Modmate/ #folder name
# │  ├─ config.json #saved_config_path
# │  ├─ Mods/ #saved_store_path
# │  │  ├─ OptiFine_1.17.1_HD_U_H1.jar
# │  ├─ Profiles/ #saved_profiles_name
# │     ├─ profile.json


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
        try:
            mc_path = cli.init_f(cli, folder_name)
        except Exception as e:
            print(f"An Exception occured while init'ing \n Error : {e}")
            exit()
        # mc_path = cli.get_mc_path() #init mc_path, cannot be empty
        saved_config_path = config_path(mc_path, folder_name)
        saved_store_path = store_path(mc_path, folder_name)
        cli.print_all_profiles(mc_path, folder_name, saved_profiles_name)
        # just testing
        try: 
            json = cli.select_profile(mc_path, folder_name)
            desc = json['desc']
            mods = json['mods']
        except Exception as e:
            desc = str(e).replace('\\\\', '\\')
            mods = []
            pass
        print(f"Profile description : {desc}")
        ModMate.copy_from_list(mods, saved_store_path, os.path.join(mc_path, "Mods"))

def config_path(mc_path, folder_name) -> str :
    return os.path.join(mc_path, folder_name, "config.json")

def store_path(mc_path, folder_name) -> str :
    return os.path.join(mc_path, folder_name, "Mods")

main("cli")