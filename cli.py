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

    def print_all_profiles(mc_path, folder_name, saved_profiles_name):
        profiles = get_all_profile(mc_path, folder_name, saved_profiles_name)
        print("Avaliable Profiles : ")

        count = 0
        for i in profiles:
            count += 1
            print(f"\'{i}\',", end="")
            if count == 3:
                print() 
                count = 0
        print("\n_________________")

def get_all_profile(mc_path, folder_name, saved_profiles_name) -> list[str]:
    res = []
    profiles_path = os.path.join(mc_path, folder_name, saved_profiles_name)
    for i in os.listdir(profiles_path):
        if os.path.isfile(os.path.join(profiles_path, i)):
            res.append(i)
    return res