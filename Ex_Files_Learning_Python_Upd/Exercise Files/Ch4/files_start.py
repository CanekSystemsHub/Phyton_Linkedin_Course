#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  #f = open("canekfile.txt","w+")

  
  # Open the file for appending text to the end
  f = open("canekfile.txt","a")

  # write some lines of data to the file
  for i in range(20):
    f.write("Hey Budy1 this is the line numer " + str(i) + "\r\n")

  
  # close the file when done
  f.close()
  
  # Open the file back up and read the contents
  f = open("canekfile.txt","r")
  if f.mode == 'r':
    contents = f.read()
    print(contents)

    
if __name__ == "__main__":
  main()
