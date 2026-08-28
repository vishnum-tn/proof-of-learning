"""
import sys
try:
    print("hello my name is", sys.argv[1] )
except:
    print("few elements")

"""


import sys
if len(sys.argv) < 2:
    sys.exit("toofew arugemts")
elif len(sys.args) > 2:
    sys.exit("too many arguments")


print("hello,my name is",sys.argv[1])