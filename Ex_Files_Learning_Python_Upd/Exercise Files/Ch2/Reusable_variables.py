# Create a reusable variable to be called by different fucntions
"""
name = "Canek"

def hello():
    print('Hello ' + name)

def goodbye():
    print('goodbye ' + name) 

hello()
goodbye()
"""

# Now  To pass an argument to a variable during the runtime with sys
import sys

def hello(name):
    print('Hola ' + name + ' Good job on learning Python')

name = sys.argv[1]

hello(name)

