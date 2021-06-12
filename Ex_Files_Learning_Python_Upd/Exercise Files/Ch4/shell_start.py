#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  if path.exists("canekfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("canekfile.txt")
    path.isfile("canekfile.txt")
    
    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    
    # copy over the permissions, modification times, and other info
    shutil.copy(src, dst)
    shutil.copystat(src, dst)   # This one copies the metadata too

    # rename the original file
    os.rename("canekfile.txt","Ren_canekfile.txt")
    f = open("Ren_canekfile.txt","r")
    contents = f.read()
    print("The file was renamed successfully and the contens are like these too: \n\r", contents)

    # now put things into a ZIP archive
    root_dir, tail = path.split(src)
    shutil.make_archive("archiveddir","zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("archivedfile.zip","w") as newzip:
      newzip.write("canekfile.txt")
      newzip.write("Ren_canekfile.txt")
      newzip.write("canekfile.txt.bak")
      
if __name__ == "__main__":
  main()
