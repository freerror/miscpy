from glob import fnmatch 
import platform

x = 999

def myfunc():
    global x
    x = 300

myfunc()

print(x) 

for name in str(dir(platform)).split(','):
    print(name)

for name in str(dir(fnmatch)).split(','):
    print(name)