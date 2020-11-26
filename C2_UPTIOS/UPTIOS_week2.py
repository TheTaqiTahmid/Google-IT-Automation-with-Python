# Reading file in python

# file = open("spider.txt")
# print(file.readline())  # It will read the current position line
# print(file.read())  # It will read the text from current position to the last position
#
# file.close()  # Always close the file before ending the script


# It is possible to create a block of code using the keyword with. It will allow us to open a file,
# do file operations and then python will close the file itself. Opened file inside a block will
# restrict the file inside the block and not allow the file to be used in other portion of the code

# with open("spider.txt") as file:
#     print(file.readline())

# Iterating through files

# with open("spider.txt") as file:
#     for line in file:
#         print(line.upper())
#
# # we can remove the all surrounding whitespace in between the strings using strip method
#
# with open("spider.txt") as file:
#     for line in file:
#         print(line.strip().upper())


file = open("spider.txt")
lines = file.readlines()  # This lines variable saves all lines in spider.txt as a list. Now we can perform different
# list operation on lines
# #print(lines)
file.close()
lines.sort()
print(lines)  # Python shows not printable characters using \ e.g \n, \t etc

# Write files File objects can be opened in several different modes. r - read only: it is the default file open mode,
# w - write only: it will override existing content of the file and reading the file is not possible in this mode,
# a - append  content into an existing file, r+ - for read-write mode.


with open("novel.txt", "w") as file:
    file.write("In was a warm summer night")

# We can use os module to interact with files, Such as remove, rename, access history etc.

import os
import time

os.remove("novel.txt")  # Remove a file
os.rename("finished_masterpiece.txt", 'first_draft.txt')
os.rename("first_draft.txt", "finished_masterpiece.txt")  # Rename a file
os.path.exists("finished_masterpiece.txt")  # Check if the file exists
os.path.getsize("finished_masterpiece.txt")  # Check the file size
os.path.getmtime("spider.txt")  # Check when the file was last modified
print(time.localtime(os.path.getmtime("spider.txt")))
os.path.abspath("spider.txt")  # Gives absolute path of the file
os.getcwd()  # Prints current working directory
os.mkdir("new_dir")  # Create new directory inside current working directory
os.rmdir("new_dir")  # Remove directory. It will only work if the directory is empty
# os.chdir("new_dir")  # Change the current directory
print(os.listdir("C:/Users/TAQI/PycharmProjects/google_IT"))  # Provides a list of files and subdirectories inside the directory


# Check which values are files and which values are subdirectory in the directory
dir = ("C:/Users/TAQI/PycharmProjects/google_IT")
for name in os.listdir(dir):
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))



