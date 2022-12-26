# Delete a file
import os
try: 
    os.remove("/home/ruser/tmp/demofile_creation.txt")
except:
    print("No file to delete")

# Create a folder
os.mkdir("/home/ruser/tmp/myfolder")

# Delete a folder
try:
    os.rmdir("/home/ruser/tmp/myfolder")
except:
    print("No folder to delete")

# Create a file
f = open("/home/ruser/tmp/demofile_creation.txt", "x")
f = open("/home/ruser/tmp/randomfile.txt", "x")

# Create a new file if it doesn't exist and/or overwrite existing
f = open("/home/ruser/tmp/demofile2.txt", "w")
f.write("New file created and added some data")
f.close

# Append to existing file
f = open("/home/ruser/tmp/demofile2.txt", "a")
f.write("\n\nNow the file has more content!")
f.close

# Better way to do it
with open("/home/ruser/tmp/demofile2.txt", "a") as f:
    f.write("\n\nAdded some more content a better way")
    # it implicitly closes the file, saving you having to remember to do it

# Read files
f = open("/home/ruser/tmp/randomfile.txt", "r")
print(f.read()) 