import os
import keyboard
import time
import ctypes
from ctypes import wintypes
import ctypes


# Windows API constants
WM_CHAR = 0x0102
WM_KEYDOWN = 0x0100
VK_RETURN = 0x0D

os.system("start cmd")
time.sleep(0.1)
keyboard.write("start.cmd")
keyboard.press_and_release("enter")

# Load user32.dll
user32 = ctypes.windll.user32

# Find the cmd window (change "Command Prompt" if your window has a different title)
hwnd = user32.FindWindowW(None, "main")

if hwnd == 0:
    # Try alternative title
    hwnd = user32.FindWindowW(None, "C:\\Windows\\system32\\cmd.exe")

if hwnd == 0:
    print("Cmd window not found! Make sure cmd.exe is open.")
else:
    # Bring window to foreground
    user32.SetForegroundWindow(hwnd)
    
    # Function to send text
    def send_text(text):
        for char in text:
            # Send WM_CHAR for each character
            user32.PostMessageW(hwnd, WM_CHAR, ord(char), 0)
        # Send Enter key
        user32.PostMessageW(hwnd, WM_KEYDOWN, VK_RETURN, 0)    
def enum_windows():
    windows = []
    def callback(hwnd, _):
        if user32.IsWindowVisible(hwnd):
            length = user32.GetWindowTextLengthW(hwnd)
            if length > 0:
                buff = ctypes.create_unicode_buffer(length + 1)
                user32.GetWindowTextW(hwnd, buff, length + 1)
                if "cmd" in buff.value.lower():
                    windows.append(buff.value)
        return True
    user32.EnumWindows(ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)(callback), 0)
    print(windows)

enum_windows()
user32 = ctypes.windll.user32
while True:
    with open(r"C:\Users\boba1\Desktop\Py server\containers.txt", encoding='utf-8') as file:
        my_data1= file.read()
    time.sleep(1)
    with open(r"C:\Users\boba1\Desktop\Py server\containers.txt", encoding='utf-8') as file:
        my_data2= file.read()
    if my_data1 != my_data2:
        send_text(my_data2)
