import shutil
import os

def copy_from_list(list: list[str],st , ds):
    #clear folder before
    print('Clearing original folder ...')
    shutil.rmtree(ds)
    os.mkdir(ds)
    #here, i is just the filename
    for i in list:
        #should be complete path to default mods folder
        mod_path = os.path.join(st, f"{i}.jar")
        print("copied ", mod_path)
        err_report: list[(str, str)] = []
        CRED = '\033[91m'
        CEND = '\033[0m'
        try:
            shutil.copy2(mod_path, ds)
        except Exception as e:
            # TODO: make a report of failed copies later
            #Filename and Reason
            # printing colors
            print(CRED, f"failed to copy {mod_path}, skipping\nreason : {e}", CEND)
            err_report.append((mod_path, e))    
    print("    to ", ds)
    if err_report == []:
        print("Finished task successfully")
    else:
        print("error report :")
        for (name, reason) in err_report:
            print(CRED, f"{name} failed, {reason}", CEND)