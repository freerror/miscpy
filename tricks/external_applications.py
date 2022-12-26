import subprocess

# Define command as string
cmd = 'Dir'

# Use shell to execute the command and store it in sp variable
sp = subprocess.Popen(cmd,shell=True)

# Store the return code in rc variable
rc=sp.wait()

# Print the content of sp variable
print(sp)