import platform
import os
import json

class CLI:
    def get_mc_path() -> str :
        print("Enter Minecraft path (leave blank for default)")
        i = input(">> ")
        if platform.system() == "Windows":
            if i == "":
                return os.path.join(os.environ["USERPROFILE"], "AppData\\Roaming\\.minecraft")
        elif platform.system() == "Linux":
            if i == "":
                return "~/.minecraft"
    # should return json object
    def select_profile(mc_path, folder_name):
        print("Enter selected profile's name")
        i = input(">> ")
        with open(os.path.join(mc_path, folder_name, "Profiles", f"{i}.json"), 'r') as file:
            j = file.read().replace('\n', '')
        return json.loads(j)
