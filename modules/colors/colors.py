import sys

class bcolors:
    """ Changes the colour of the text"""
    if sys.executable.find('pythonw.exe') == sys.executable.find('WinPy') == -1:
        HEADER = ''
        OKBLUE = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
    else:
        HEADER = '\033[96m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'



