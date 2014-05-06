__author__ = 'yufeilong'

import json
import os
import tarfile
import shutil

# read config path params
config = json.loads(open('params.json').read())
file_path = config["jdk_file_path"]
target_path = config["jdk_target_path"]
config_path = config["config_file_path"]
config_add = config["config_file_add"]

# copy file to system folder
# if it's a tar.gz direct extract to target folder
# if it's a folder copy to target folder
if os.path.exists(file_path):
    if os.path.isdir and file_path.find("tar") != -1:
        tar = tarfile.open(file_path)
        tar.extractall(target_path)
        tar.close()
        print("extract success!!!")
    else:
        if os.path.exists(target_path):
            shutil.rmtree(target_path)
        shutil.copytree(file_path, target_path)
        print("copy files success!!!")
else:
    print("file doesn't exist!!!")

# modify user configuration information
if os.path.exists(config_path):
    # write file
    fileWrite = open(config_path, 'a')

    fileWrite.writelines(config_add)

    os.system(". ~/.bashrc")

    print("config success !!!")

else:
    print("config file doesn't exist!!!")