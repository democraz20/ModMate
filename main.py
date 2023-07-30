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
saved_profiles_name = "Profiles"  # path where all profiles are saved

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
        second_gray = "gray30"

        mc_path = ""

        layouts = [
            [sg.Text(folder_name, background_color=default_gray)],
            [
                sg.Text(
                    "Enter Minecraft path (leave blank for default)",
                    background_color=default_gray,
                )
            ],
            [
                sg.InputText(
                    key="mcpathinput",
                    background_color=second_gray,
                    text_color="White",
                    expand_x=True,
                ),
                sg.Button("Get Profiles", expand_x=True),
            ],
            [
                sg.Text(
                    "Error PlaceHolder",
                    background_color=default_gray,
                    key="ErrorDisplay",
                    visible=False,
                )
            ],
            [
                sg.Text("Select Profile", background_color=default_gray),
                sg.Combo(
                    [],
                    size=(40, 1),
                    background_color=second_gray,
                    text_color="White",
                    key="profileselector",
                    expand_x=True,
                ),
            ],
            [
                sg.Button("Start", key="startcopy", visible=False, expand_x=True)
            ],
            # [sg.Button("Debug window", key="debugwindow")],
            [
                sg.Output(
                    size=(80, 10),
                    background_color="black",
                    text_color="white",
                    key="output_debug",
                    visible=False,
                    expand_x=True,
                    expand_y=True,
                )
            ],
        ]

        sg.theme("Dark")
        window = sg.Window(folder_name, layouts,return_keyboard_events=True, resizable=True)

        gui = GUI
        d = False


        while True:
            event, values = window.read()
            # print(event)
            if event == sg.WIN_CLOSED:
                break
            elif event == "d:68":
                if d != True:
                    window["output_debug"].update(visible=True)
                    d = True
                else: 
                    window["output_debug"].update(visible=False)
                print(values)

            # first
            elif event == "Get Profiles":
                # means use default
                if values["mcpathinput"] == "":
                    import platform

                    plat = platform.system()
                    # init mc path
                    if plat == "Windows":
                        values["mcpathinput"] = os.path.join(
                            os.environ["USERPROFILE"],
                            "AppData",
                            "Roaming",
                            ".minecraft",
                        )
                    elif plat == "Linux":
                        values["mcpathinput"] = "~/.minecraft"
                    mc_path = values["mcpathinput"]
                    # assume it is now valid , will check later

                print(values)
                mcpath_exist = gui.validate_mcpath(values["mcpathinput"])
                print("mcpathexist ", mcpath_exist)

                # minecraft exists
                if mcpath_exist == True:
                    a = True
                    # Modmate does not exist
                    if (
                        gui.validate_modmate(values["mcpathinput"], folder_name)
                        == False
                    ):
                        ch = sg.popup_yes_no("ModMate folder not found, create now?")
                        if ch == "Yes":
                            # call init folder
                            gui.init_modmate(values["mcpathinput"], folder_name)
                            pass
                        else:
                            window["ErrorDisplay"].update(
                                "ModMate folder not found",
                                visible=True,
                                text_color="Red",
                            )
                    # Everything goes right
                    else:
                        profiles = gui.get_profiles(
                            values["mcpathinput"], folder_name, saved_profiles_name
                        )
                        # window["mcpathinput"].update(default_text=values["mcpathinput"]) #shits bricks
                        window["profileselector"].update(values=profiles)
                        window["startcopy"].update(visible=True)
                        print(profiles)
                else:  # minecraft does not exists,
                    sg.popup_auto_close(
                        "Minecraft folder not detected, install minecraft or try a correct path",
                        auto_close=False,
                    )
                    window["ErrorDisplay"].update(
                        "Minecraft path does not exist", visible=True, text_color="Red"
                    )
                    window["profileselector"].update(values=[])
                    # do nothing after

            elif event == "startcopy":
                print("Event start copy")
                # open file
                # get list
                # get_mod_list handles above
                modmate_path = os.path.join(mc_path, folder_name)
                ((modlist, desc), (err, errdesc)) = gui.get_mod_list(
                    modmate_path, values["profileselector"]
                )
                if err != None:
                    print("An error occured")
                    # error occured
                    window["ErrorDisplay"].update(
                        f"{err} occured, {errdesc}", visible=True, text_color="Red"
                    )
                else:
                    print("No errors, proceeding with copying")
                    # everything went fine
                    # start copying
                    mods = modlist
                    profiledesc = desc
                    saved_store_path = store_path(modmate_path)
                    errorreport = ModMate.copy_from_list(
                        mods, saved_store_path, os.path.join(mc_path, "Mods")
                    )
                    if len(errorreport) == 0:
                        window["ErrorDisplay"].update(
                            "Task finished with no errors",
                            visible=True,
                            text_color="Green",
                        )
                    else:
                        window["ErrorDisplay"].update(
                            "Error occured while copying, check debug window for more info",
                            visible=True,
                            text_color="Red",
                        )
                    pass
                pass
                # init
        window.close()


#------------------------------------------------------------#


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
            desc = json["desc"]
            mods = json["mods"]
        except Exception as e:
            desc = str(e).replace("\\\\", "\\")
            mods = []
            pass
        print(f"Profile description : {desc}")
        ModMate.copy_from_list(mods, saved_store_path, os.path.join(mc_path, "Mods"))


def config_path(modmate_path) -> str:
    return os.path.join(modmate_path, "config.json")


def store_path(modmate_path) -> str:
    return os.path.join(modmate_path, "Mods")


main("gui")
