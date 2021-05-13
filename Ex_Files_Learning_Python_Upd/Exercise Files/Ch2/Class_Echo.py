import os
import sys

# Define a Function tha uses the OS Library
def trigger_echo(name):
    # Use the System Method from the OS Library
    print_name = os.system("echo Hello, " + name)
    print(print_name)


# Use the 'sys' library to pass in a value at runtime
name = sys.argv[1]

trigger_echo(name)