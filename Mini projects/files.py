import os
import shutil
import pprint

print(os.path.join("home","username","Desktop"))

files=["Primary","University","High School"]

for filename in files:
    print("home/username/"+filename)

for i in range(1):
    for folders,subfolders,filenames in os.walk("/home/username/Desktop"):
        print(folders)
        
    for subfolder in subfolders:
        print(subfolder) 

    for filename in filenames:
        print(filename)      
#changing dir

os.getcwd()
os.chdir("/home/username")
print(os.getcwd())

print(os.path.dirname("/home/username/Desktop/Movies"))
print(os.path.basename("/home/username/Desktop/Movies"))

#making dir and listing dir and size

#size of file
print(os.path.getsize("/home/username/Desktop/Morvin/new file"))

#size of dir
total=0
print(pprint.pformat(os.listdir("/home/username/Desktop/Movies/Single Movies")))
for filename in os.listdir("/home/username/Desktop/Movies/Single Movies"):
    total=total+os.path.getsize(os.path.join("/home/username/Desktop/Movies/Single Movies",filename))

print(str(total/(1000000000))+" GB")


#copying file 
os.chdir("/home/username/Desktop")
shutil.copy("/home/username/Desktop/Tairon","/home/username/Desktop/IAN")
#copying folders
shutil.copytree("/home/username/Source Codes","/home/username/Desktop/Movies/Source Codes")

# renaming
shutil.move("/home/username/Desktop/Tairon","/home/username/Desktop/IAN")

#moving
shutil.move("/home/username/Desktop/Tairon","/home/username/Desktop/Movies")

#Deleting files and folders
os.unlink("/home/username/Desktop/new file")

#os.rmdir(path)
#os.rmtree(path)
