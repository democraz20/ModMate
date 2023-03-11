import platform
import os

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
