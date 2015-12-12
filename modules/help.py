#!/usr/bin/env python3
def ajuda():
    """ This function displays help when called """
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