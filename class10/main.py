import os
import platform

# print(platform.system())
# print(platform.release())
# print(os.name)

#Assignment to raise error if windows

custom_env = os.environ["custom_env"]   # read the env variables
print(custom_env)
os.environ["python_custom_env"] = "setfrompythonscript" # set the env variables


# import shutil
#
# # print(dir(shutil))
#
# result = shutil.copy("copy_text.txt", "file_repo")
#
# print(result)

#password

# from getpass import getpass
#
# password = getpass()
#
# print(password)


# authentication public-private #paramiko #semaphore #multiprocessing







