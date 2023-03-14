import shutil
import os

def copy_from_list(list: list[str],st , ds):
    #here, i is just the filename
    for i in list:
        #should be complete path to default mods folder
        mod_path = os.path.join(st, f"{i}.jar")
        print("copied ", mod_path)
        shutil.copy2(mod_path, ds)
    print("    to ", ds)