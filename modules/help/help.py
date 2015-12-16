#!/usr/bin/env python3
from modules.ftp import *
from modules.httpd import *
from modules.group import *
from modules.encoding import *
from modules.ping import *
from modules.delete import *
from modules.workurl import *
from modules.colors import *

def ajuda(cosa):
    """ This function displays help when called """
    if cosa == None:
        if lang == 'ca':
            print('''Aquesta consola està en mode de desenvolupador.''')
            input('''Prem Enter per continuar...''')
            print('''
Per dir "igual a" has de posar ==
Per connectar-te a un servidor ftp, la sintaxi és:
<host> <port> <usuari> <contrasenya>
Per fer ping (i comprovar si el host està en línia), la sintaxi és: ping domini.com
Pots encriptar un missatge escrivint "encripta <missatge>"''')
            input('''Prem Enter per continuar...''')
            print("\n" + '''Ctrl+C per aturar la consola''')
        else:
            print('''This shell is in developer mode.''')
            input('''Press Enter to continue''')
            print('''
To say "equal to" you have to put ==
To connect to a ftp server, the syntax is:
<host> <port> <user> <password>
To make ping (and check if host is up), the syntax is: ping domain.com
You can encrypt a message writing "encrypt <message>"''')
            input('''Press Enter to continue...''')
            print("\n" + '''Ctrl+C To stop the shell''')
    elif cosa == 'colors':
        print(bcolors.__doc__)
    elif cosa == 'ftp':
        print(FTPConnect.__doc__)
    elif cosa == 'class' or cosa == 'classe':
        print(Class.__doc__)
    elif cosa == 'delete' or cosa == 'esborrar':
        print(delete_content.__doc__)
    elif cosa == 'encrypt' or cosa == 'encripta':
        print(encode.__doc__)
    elif cosa == 'decrypt' or cosa == 'desencripta':
        print(decode.__doc__)
    elif cosa == 'server' or cosa == 'servidor' or cosa == 'http' or cosa == 'httpd':
        print(run.__doc__)
    elif cosa == 'ping':
        print(ping.__doc__)
    elif cosa == 'feina' or cosa == 'work':
        print(work_web.__doc__)
    elif cosa == 'cerca' or cosa == 'search':
        print(search.__doc__)
    else:
        pass



