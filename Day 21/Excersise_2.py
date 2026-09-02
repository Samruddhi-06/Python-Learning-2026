# Write a program to clear the clutter inside a folder on your computer.
# You should use os module to rename all the png images from 1.png all till n.png 

import os 

folder = "Day 21\My_Folder"

files = os.listdir(folder)

print("Files before : ",files)

count = 1

for file in files:
    if file.endswith(".png"):
        old_path = os.path.join(folder,file)
        new_path = os.path.join(folder, str(count) + ".png")
        os.rename(old_path, new_path)
        count += 1

print()
files = os.listdir(folder)
print("Files after : ",files)