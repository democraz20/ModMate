import shutil
import os

def copy_from_list(list: list[str],st , ds):
    #clear folder before
    shutil.rmtree(ds)
    os.mkdir(ds)
    #here, i is just the filename
    for i in list:
        #should be complete path to default mods folder
        mod_path = os.path.join(st, f"{i}.jar")
        print("copied ", mod_path)
        try:
            shutil.copy2(mod_path, ds)
        except Exception as e:
            # TODO: make a report of failed copies later
            # printing colors
            CRED = '\033[91m'
            CEND = '\033[0m'
            print(CRED, f"failed to copy {mod_path}, skipping\nreason : {e}", CEND)
    print("    to ", ds)