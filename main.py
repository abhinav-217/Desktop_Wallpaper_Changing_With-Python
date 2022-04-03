import ctypes
import os
from os.path import isfile, join
from time import sleep

def ChangeForInfinite():
    folderPath = r"C:\Users\hp\Desktop\IronMan"
    all_files = [
        f for f in os.listdir(folderPath) if isfile(join(folderPath,f))
    ]
    print(len(all_files))
    all_files_len = len(all_files)
    while True:
        for i in range(0,all_files_len):
            ctypes.windll.user32.SystemParametersInfoW(20,0,all_files[i],0)
            print(f"Changed {i} th image")
            sleep(10)

def ChangeAtRegularInterval(interval):
    folderPath = r"C:\Users\hp\Desktop\IronMan"
    all_files = [
        f for f in os.listdir(folderPath) if isfile(join(folderPath,f))
    ]
    print(len(all_files))
    all_files_len = len(all_files)
    for i in range(0,all_files_len):
        ctypes.windll.user32.SystemParametersInfoW(20,0,all_files[i],0)
        print(f"Changed {i} th image")
        sleep(interval)


print("\n")
print("*****  Note this Program will not work if you have customized \nyour pc or you have already setted some live wallpaper from third party apps \nthen this will not work  *****")
print("\n")
print("Enter Your choice Out of the following choices:- ")
print("!. Change the Wallpaper and Run program Endlessly")
print("2. Change the Wallpaper with the custom time interval")
print("Enter Your Choice:-")
user_input = int(input())

if(user_input==1):
    ChangeForInfinite()
elif(user_input==2):
    print("Enter Your Custom Time Interval between two wallpaper")
    time = int(input())
    ChangeAtRegularInterval(time)