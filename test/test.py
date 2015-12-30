#!/usr/bin/python3
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

notworking = False

print("Testing modules")
try:
    from modules.colors import *
except:
    notworking = True
    print("modules.colors not working!")
try:
    from modules.delete import *
except:
    notworking = True
    print("modules.delete not working!")
try:
    from modules.encoding import *
except:
    notworking = True
    print("modules.encoding not working!")
try:
    from modules.ftp import *
except:
    notworking = True
    print("modules.ftp not working!")
try:
    from modules.group import *
except:
    notworking = True
    print("modules.group not working!")
try:
    from modules.help import *
except:
    notworking = True
    print("modules.help not working!")
try:
    from modules.httpd import *
except:
    notworking = True
    print("modules.httpd not working!")
try:
    from modules.ping import *
except:
    notworking = True
    print("modules.ping not working!")
try:
    from modules.search import *
except:
    notworking = True
    print("modules.search not working!")
try:
    from modules.httpd import *
except:
    notworking = True
    print("modules.workurl not working!")
try:
    from shell import *
except:
    notworking = True
    print("shell is not working!")

if notworking == True:
    print(1)
else:
    print(0)






