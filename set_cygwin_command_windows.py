__author__ = 'yufeilong'

import json
import os

# read config path params
config = json.loads(open('params.json').read())
cygwin_path = config["cygwin_install_path"]
cygwin_user = config["cygwin_user_name"]
cygwin_bat_add = config["cygwin_config_add"]
cygwin_bash_add = config["cygwin_bash_add"]

cygwin_bat_name = "Cygwin.2.bat"

# modify Cygwin.bat file
if os.path.exists(cygwin_path):
    if os.path.exists(cygwin_path + "\\" + cygwin_bat_name):
        batFileWrite = open(cygwin_path + "\\" + cygwin_bat_name, "r+")
        batFileWrite.writelines(cygwin_bat_add)
    else:
        print("can't find ", cygwin_bat_name)

    print(".bash_profile2 path::", cygwin_path + "\\home\\" + cygwin_user + "\\.bash_profile2")

    if os.path.exists(cygwin_path + "\\" + cygwin_user + "\\home\\.bash_profile2"):
       bashFileWrite = open(cygwin_path + "\\home\\" + cygwin_user + "\\.bash_profile2", 'a')
       bashFileWrite.writelines(cygwin_bash_add)
    else:
        print("can't find .bash_profile2")
else:
    print("cygwin path error!!!")