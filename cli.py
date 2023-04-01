import platform
import os
import json
from os import path


class CLI:
    def init_f(self, folder_name) -> str:
        mc_path = self.get_mc_path()
        # minecraft path doesnt exist
        if path.exists(mc_path) != True:
            print("Minecraft is not installed on this computer.")
            print("please install Minecraft or make sure the path is correct.")
            print(f"({mc_path} does not exist)")

        # Modmate folder does not exist
        if path.exists(path.join(mc_path, folder_name)) != True:
            print("ModMate folder does not exist make one now? [y/n]")
            i = input(">> ")
            if i.lower == "y":
                # create required folders
                modmatepath = path.join(mc_path, folder_name)
                os.mkdir(modmatepath)
                os.mkdir(path.join(modmatepath, "Mods"))
                os.mkdir(path.join(modmatepath, "Profiles"))
                pass
            else:
                print("ModMate will not be installed, exiting")
                exit()

        # returns mc_path
        return mc_path

    def get_mc_path() -> str:
        print("Enter Minecraft path (leave blank for default)")
        i = input(">> ")
        if platform.system() == "Windows":
            if i == "":
                p = path.join(
                    os.environ["USERPROFILE"], "AppData", "Roaming", ".minecraft"
                )
                print("Selected : ", p)
            else:
                p = i
        elif platform.system() == "Linux":
            if i == "":
                p = "~/.minecraft"
                print("Selected : ", p)
            else:
                p = i
        return p
        # should return json object
        pass

    def select_profile(modmate_path):
        print("Enter selected profile's name")
        i = input(">> ")
        with open(path.join(modmate_path, "Profiles", f"{i}.json"), "r") as file:
            j = file.read().replace("\n", "")
        return json.loads(j)

    def print_all_profiles(modmate_path, saved_profiles_name):
        profiles = get_all_profile(modmate_path, saved_profiles_name)
        print("Avaliable Profiles : ")

        count = 0
        for i in profiles:
            i = i.replace(".json".lower(), "")
            count += 1
            print(f"'{i}',", end="")
            if count == 3:
                print()
                count = 0
        print("\n_________________")


def get_all_profile(modmate_path, saved_profiles_name) -> list[str]:
    res = []
    profiles_path = path.join(modmate_path, saved_profiles_name)
    for i in os.listdir(profiles_path):
        if path.isfile(path.join(profiles_path, i)):
            res.append(i)
    return res
