import os
import PySimpleGUI as sg
import json

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

    #if it is ok, first item of tuple is usable (list of mods and desc)
    #if error occurs, first still of second tuple will not be None and second string of inner tuple will be the desc
    def get_mod_list(modmate_path, profile) -> tuple[tuple[list[str], str], tuple[str, str]]:
        if profile == "":
            r=((None, None), ("Exception", "Profile name is empty!"))
        try:
            with open(os.path.join(modmate_path, "Profiles", "{profile}.json")) as file:
                j = file.read().replace('\n', '')
                json = json.loads(j)
            desc = json['desc']
            mods = json['mods']
            r=((mods, desc), (None, None))
            return r
        except Exception as e:
            #could have a thing where it matchs the error message then 
            #provide a more user-friendly error message back instead
            #such as file not found to profile not found
            #or do it at the main function
            r=((None, None), ("Exception", str(e)))
            return r

    def get_profiles(mc_path, foldername, saved_profiles_name) -> list[str]:
        res = []
        profiles_path = os.path.join(mc_path, foldername, saved_profiles_name)
        #here?
        for i in os.listdir(profiles_path):
            if os.path.isfile(os.path.join(profiles_path, i)):
                res.append(i.replace(".json", ""))
        return res