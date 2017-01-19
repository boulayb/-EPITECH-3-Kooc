import os.path

def check(filename : str):
    if os.path.isfile(filename) is not True:
        print(filename + " : no such file")
        return 'ERROR'
    extc = filename.find(".kc")
    exth = filename.find(".kh")
    if extc == -1 and exth == -1:
        print(filename + " has wrong extension, only .kh and .kc extension are accepted")
        return "ERROR"
    if extc != -1:
        return filename[:extc] + ".c"
    return filename[:exth] + ".h"
