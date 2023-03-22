import subprocess
import win32gui
import win32process
import win32con
import pywinauto
import ctypes
from PyQt5 import QtCore, QtGui, QtWidgets


messageBox = QtWidgets.QMessageBox
run = subprocess.run
wilcomPath = "H:\Wilcom\EmbroideryStudio_e4.2\BIN\DESLOADR.EXE /dsgneditExe:ES.EXE"
florianiPath = "C:\Program Files (x86)\Floriani\Total Control U\FlorianiLauncher.exe"

# run(florianiPath)

def activate_window(hwnd):
    user32 = ctypes.windll.user32
    user32.SetForegroundWindow(hwnd)
    if user32.IsIconic(hwnd):
        user32.ShowWindow(hwnd, 9)


def bring_to_foreground(title):
    def callback(hwnd, hwnd_list):
        if win32gui.IsWindowVisible(hwnd) and title.lower() in win32gui.GetWindowText(hwnd).lower():
            hwnd_list.append(hwnd)
        return True
    
    hwnd_list = []
    win32gui.EnumWindows(callback, hwnd_list)
    
    if hwnd_list:
        hwnd = hwnd_list[0]
        win32gui.SetForegroundWindow(hwnd)
    else:
        print(f"No window found with title '{title}'")

def checkApp(name):
    # Replace name with a substring of the window title you want to find
    substring = (name)
    # Enumerate all windows and find the first one that contains the substring
    hwnd = None
    def enum_windows_callback(hwnd, results):
        if substring.lower() in win32gui.GetWindowText(hwnd).lower():
            results.append(hwnd)

    
    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    if windows:
        hwnd = windows[0]

    # If a window was found, get the process ID
    if hwnd:
        psid = win32process.GetWindowThreadProcessId(hwnd)[1]
        print(f"App is already running")
        activate_window(hwnd)

    else:
        print(f"No window found that contains '{substring}'")
        if name == "floriani":
            print("Running Floriani")
            run(florianiPath)
        elif name == "wilcom":
            print("Running Wilcom")
            run(wilcomPath)    
        else:
            print(f"Check the name of the app")
            
    
checkApp("floriani")

input("Press Enter to close...")
