import os
import shutil
import pprint,colorama
from colorama import Fore,Style



def terminal():

 while True:

      command=input('\n'+Fore.RED+Style.BRIGHT+"{"+os.path.dirname(os.getcwd())+"}"+Fore.GREEN+Style.NORMAL+"-"+os.path.basename(os.getcwd())+"-").strip()

      if command=='ls':
         print(pprint.pformat(os.listdir(os.getcwd())))

      elif command=='pwd':
         print(os.getcwd())

      elif command=='cd':
         Dirpath=input('Directory Path:')
         if os.path.exists(Dirpath) and os.path.isdir(Dirpath):
            os.chdir(Dirpath)
            print(os.getcwd())
         else:
            print("No such Directory Exists")  

      elif command=='copy':
         DirFile=input("Dir/File Name:")
         if os.path.exists(os.path.join(os.getcwd(),DirFile)) and os.path.isfile(os.path.join(os.getcwd(),DirFile)):
            Destpath=input("Desination Path:")
            if os.path.exists(Destpath):
               shutil.copy(os.path.join(os.getcwd(),DirFile),Destpath)
            else:
               print("No such File")

         elif os.path.exists(os.path.join(os.getcwd(),DirFile)) and os.path.isdir(os.path.join(os.getcwd(),DirFile)):
            Destpath=input("Desination Path:")
            if os.path.exists(Destpath):
               shutil.copytree(os.path.join(os.getcwd(),DirFile),os.path.join(Destpath,DirFile))
            else:
               print("No such Directory")

         else:
            print("No such File or Directory")


      else:
         print("No such file or Directory")
             

terminal()