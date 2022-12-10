import os

def get_log_path():
    return "/tmp/logfile" if os.name == "posix" else f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\logfile"

def get_img_path():
    return "/tmp/imgfile" if os.name == "posix" else f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\imgfile"
