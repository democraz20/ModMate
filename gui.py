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
            return r
        try:
            with open(os.path.join(modmate_path, "Profiles", f"{profile}.json")) as file:
                j = file.read().replace('\n', '')
                js = json.loads(j)
                desc = js['desc']
                mods = js['mods']
                r=((mods, desc), (None, None))
                return r
        except Exception as e:
            emsg = str(e)
            ret = str(e)
            if "No such file or directory" in emsg:
                ret = f"Error: Profile '{profile}' not found"
            #could have a thing where it matchs the error message then 
            #provide a more user-friendly error message back instead
            #such as file not found to profile not found
            #or do it at the main function
            r=((None, None), ("Exception", ret))
            return r

    def get_profiles(mc_path, foldername, saved_profiles_name) -> list[str]:
        res = []
        profiles_path = os.path.join(mc_path, foldername, saved_profiles_name)
        #here?
        for i in os.listdir(profiles_path):
            if os.path.isfile(os.path.join(profiles_path, i)):
                res.append(i.replace(".json", ""))
        return res
    
class Editor:
    def window(profiles):
        editor_layout = []