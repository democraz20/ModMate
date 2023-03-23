import os
import PySimpleGUI as sg

class GUI:
        # true if valid false if invalid
    def validate_mcpath(mc_path) -> bool:
        return os.path.exists(mc_path)
    
    def validate_modmate(mc_path, foldername) -> bool:
        return os.path.exists(os.path.join(mc_path, foldername))
    
    def init_modmate(mc_path, foldername) :
        modmatepath = os.path.join(mc_path, foldername)
        os.mkdir(modmatepath)
        os.mkdir(os.path.join(modmatepath, "Mods"))
        os.mkdir(os.path.join(modmatepath, "Profiles"))
        pass

    def get_profiles(mc_path, foldername, saved_profiles_name) -> list[str]:
        res = []
        profiles_path = os.path.join(mc_path, foldername, saved_profiles_name)
        #here?
        for i in os.listdir(profiles_path):
            if os.path.isfile(os.path.join(profiles_path, i)):
                res.append(i.replace(".json", ""))
        return res