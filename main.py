# imports
import platform
import os
import PySimpleGUI as sg
import ModMate

# file imports
from cli import CLI
from gui import GUI

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
        default_gray = "gray25"

        layouts = [ [sg.Text(folder_name, background_color=default_gray)] ,
                    [sg.Text("Enter Minecraft path (leave blank for default)", background_color=default_gray)],
                    [sg.InputText(key="mcpathinput"), sg.Button("Get Profiles")],
                    [sg.Text("Error PlaceHolder", background_color=default_gray, key="ErrorDisplay", visible=False)],
                    [sg.Text("Select Profile", background_color=default_gray), sg.Combo([], size=(40,1))],
                    [sg.Output(size=(80,10), background_color="black", text_color="white", key="output_debug", visible=False)],
                    [sg.Button("Debug values")],
                  ]
        sg.theme("Dark")

        window = sg.Window(folder_name, layouts)

        gui = GUI
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Debug values":
                window["output_debug"].update(visible=True)
                print(values)
            elif event == "Get Profiles":
                if values["mcpathinput"] == "":
                    import platform
                    #init mc path
                    plat = platform.system()
                    if plat == "Windows":
                        values["mcpathinput"] = os.path.join(os.environ["USERPROFILE"], "AppData","Roaming",".minecraft")
                    elif plat == "Linux":
                        values["mcpathinput"] = "~/.minecraft"
                
                print(values)
                
                if gui.validate_mcpath(values["mcpathinput"]) == False:
                    sg.popup_auto_close(
                        "Minecraft folder not detected, install minecraft or try a correct path",
                        auto_close=False
                        )
                    pass
                else:
                    if gui.validate_modmate(values["mcpathinput"], folder_name) == False:
                        ch = sg.popup_yes_no("ModMate folder not found, create now?")
                        if ch == "Yes":
                            # call init folder
                            pass
                        else:
                            window["ErrorDisplay"].update(
                                "ModMate folder not found",
                                visible=True,
                                text_color="Red"
                                )
                    pass
                gui.get_profiles(values["mcpathinput"])
                #init
                pass
                
        window.close()
    elif mode == "cli":
        cli = CLI
        try:
            mc_path = cli.init_f(cli, folder_name)
        except Exception as e:
            print(f"An Exception occured while init'ing \n Error : {e}")
            exit()
        # mc_path = cli.get_mc_path() #init mc_path, cannot be empty
        modmate_path = os.path.join(mc_path, folder_name)
        # saved_config_path = config_path(modmate_path)
        saved_store_path = store_path(modmate_path)
        cli.print_all_profiles(modmate_path, saved_profiles_name)
        # just testing
        try: 
            json = cli.select_profile(modmate_path)
            desc = json['desc']
            mods = json['mods']
        except Exception as e:
            desc = str(e).replace('\\\\', '\\')
            mods = []
            pass
        print(f"Profile description : {desc}")
        ModMate.copy_from_list(mods, saved_store_path, os.path.join(mc_path, "Mods"))

def config_path(modmate_path) -> str :
    return os.path.join(modmate_path, "config.json")

def store_path(modmate_path) -> str :
    return os.path.join(modmate_path, "Mods")

main("gui")