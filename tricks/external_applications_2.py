import subprocess

# Define command as string and then split() into list format
cmd = 'python --version'.split()

# Check the list value of cmd
print('command in list format:',cmd)

# Use shell=False to execute the command
sp = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

# Store the return code in rc variable
rc=sp.wait()

# Separate the output and error by communicating with sp variable.
# This is similar to Tuple where we store two values to two different variables
out,err=sp.communicate()

if rc == 0:
    for line in out.splitlines():
        if "failed" in line:
            print(line.split()[1])
else:
    print('The command returned an error: ',err)

print(f'What we got: \n- {out}\n- {err}\n')