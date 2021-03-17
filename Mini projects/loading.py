import os
import time
import colorama
from colorama import Back,Style,Fore

def Bar(seconds):
    for loading in range(0,seconds+1):
        print("\n")
        print("Loading...")
        print("<"+("-"*loading)+(" "*(seconds-loading))+">"+str(loading*100)+"%")
        print("\n")
        time.sleep(1)
        os.system("clear")

def screen(seconds):
    screens=open("screen.txt","a")
    screens=open("screen.txt","r")
    for lines in screens:
        print(lines,end="")
        time.sleep(seconds)
    screens.close()

Bar(3)
os.system("clear")
screen(.5)
