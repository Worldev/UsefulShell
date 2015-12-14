#!/usr/bin/env python3
# Python 3.5 needed
__author__ = "Miquel Comas (Mikicat)"
__copyright__ = "Copyright 2015, The UsefulShell Project"
__credits__ = ["Miquel Comas (Mikicat)", "JeDa"]
__license__ = "GPLv3"
__version__ = "dev"
__maintainer__ = "Miquel Comas"
__email__ = "usefulshellproject@gmail.com"
__status__ = "Development"

if __name__ == "__main__":
    try:
        try:
            import os
            import sys
            import platform
            import webbrowser
            import time
            import random
            import subprocess
            import logging, logging.handlers
            import logging.config
            import http.server
            import socketserver
            import queue
            import urllib, urllib.parse, urllib.request
            import json
            import re
            import base64
            import inspect
            import builtins
            from ftplib import *
            from modules.ftp import *
            from modules.httpd import *
            from modules.group import *
            from modules.encoding import *
            from modules.help import *
            from modules.ping import *
            from modules.delete import *
            from modules.workurl import *
            from modules.colors import *

        except ImportError:
            print('A module has failed to load')
            exit()

        try:
            os.mkdir('tmp')
        except FileExistsError:
            pass

        try:
            if sys.argv[1] == 'http' or sys.argv[1] == 'httpd' or sys.argv[1] == 'server':
                run()
            elif sys.argv[1] == 'class':
                classe = Class()
            elif sys.argv[1] == 'classes':
                try:
                    while True:
                        classe = Class()
                except EOFError:
                    pass
                except KeyboardInterrupt:
                    pass
            elif sys.argv[1] == 'ftp':
                FTPConnect(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
            else:
                pass
        except IndexError:
            pass

        print('OS: ' + platform.system() + ' --> Init time: ' + time.asctime())
        logging.basicConfig(filename='tmp/shell_log.log', level=logging.INFO)
        logging.info(' Initialization time: ' + time.asctime())
        logging.info(' OS: ' + platform.system())
        builtins.lang = input('Choose your language (en/ca) [en]: ')
        if lang == '':
            lang = 'en'
        else:
            pass
            
        if lang == 'ca':
            print('Benvinguts a la consola d\'ajuda en desenvolupament a partir de Python 3.5.' + "\n" + 'Escriviu ajuda o help per a obtenir ajuda' + "\n")
            logging.info(' Language: ' + lang)
        else:
            print('Welcome to the helping shell in development based off Python 3.5.' + "\n" + 'Type help to obtain help' + "\n")
            logging.info(' Language: ' + lang)


        def clear():
            """ This function "clears" the screen by printing 100 "\n" """
            print("\n" * 100)


        while True:
            direct = os.getcwd()
            inp = input(direct + "> ")
            shell = inp.split()
            try:
                if shell[0] == "ftp":
                    loglist = [shell[0], shell[1], shell[2], shell[3], '*' * len(shell[4])]
                    logstr = ' '.join(loglist)
                    logging.info(logstr)
                else:
                    logging.info(' Input: ' + inp)
            except IndexError:
                pass
            
            if "print" in shell or "show" in shell or "echo" in shell or "mostra" in shell or "ensenya" in shell:
                del shell[0]
                print(' '.join(shell))
            
            elif "stop" in shell or "exit" in shell or "finish" in shell or "end" in shell or "final" in shell or "fi" in shell or "acabar" in shell:
                if lang == 'ca':
                    print('Final de la Sessió.')
                    exit()
                else:
                    print('Session End.')
                    exit()
                break

            elif "cd" in shell:
                direct = os.path.abspath(os.path.join(shell[1], os.pardir))

            elif "ftp" in shell:
                try:
                    ftpserver = FTPConnect(shell[1], int(shell[2]), shell[3], shell[4])
                except ValueError:
                    print(bcolors.WARNING + 'Syntax: <host> <port> <user> <passwd>' + bcolors.ENDC)

            elif "feina" in shell or "work" in shell:
                work_web()


            elif "mirar" and "correu" in shell or "see" and "mail" in shell:
                webbrowser.open('https://mail.google.com')
            
            elif "ajuda" in shell or "help" in shell:
                ajuda()
  
            elif "*" in shell:
                try:
                    mult_first = float(shell[0])
                    mult_second = float(shell[2])
                    if lang == 'ca':
                        print('El resultat és %s' % (mult_first * mult_second))
                    else:
                        print('The result is %s' % (mult_first * mult_second))
                except IndexError or NameError:
                    if lang == 'ca':
                        print('Has deixat algun paràmetre en blanc')
                    else:
                        print('You have left some parameters in blank')
                except ValueError:
                    if lang == 'ca':
                        print('No pots dividir lletres')
                    else:
                        print('You can not divide letters')
                    
            elif "/" in shell:
                try:
                    div_first = float(shell[0])
                    div_second = float(shell[2])
                    if lang == 'ca':
                        print('El resultat és %s' % (div_first / div_second))
                    else:
                        print('The result is %s' % (div_first / div_second))
                except IndexError or NameError:
                    if lang == 'ca':
                        print('Has deixat algun paràmetre en blanc')
                    else:
                        print('You have left some parameters in blank')
                except ValueError:
                    if lang == 'ca':
                        print('No pots dividir lletres')
                    else:
                        print('You can not divide letters')
                    
            elif "+" in shell:
                try:
                    sum_first = float(shell[0])
                    sum_second = float(shell[2])
                    if lang == 'ca':
                        print('El resultat és %s' % (sum_first + sum_second))
                    else:
                        print('The result is %s' % (sum_first + sum_second))
                except IndexError or NameError:
                    if lang == 'ca':
                        print('Has deixat algun paràmetre en blanc')
                    else:
                        print('You have left some parameters in blank')
                except ValueError:
                    if lang == 'ca':
                        print('No pots sumar lletres')
                    else:
                        print('You can not sum letters')
                        
            elif "-" in shell:
                try:
                    rest_first = float(shell[0])
                    rest_second = float(shell[2])
                    if lang == 'ca':
                        print('El resultat és %s' % (rest_first - rest_second))
                    else:
                        print('The result is %s' % (rest_first - rest_second))
                except IndexError or NameError:
                    if lang == 'ca':
                        print('Has deixat algun paràmetre en blanc')
                    else:
                        print('You have left some parameters in blank')
                except ValueError:
                    if lang == 'ca':
                        print('No pots restar lletres')
                    else:
                        print('You can not rest letters')
                    
            elif ">" in shell or "<" in shell or "==" in shell:
                try:
                    true_false = eval(inp)
                except:
                    if lang == 'ca':
                        print("Has introduït un caràcter no numèric. Només s'accepten nombres (positius i negatius)")
                    else:
                        print("You have introduced a non-numeric character. Only numeric characters are accepted (positive and negative)")
                if lang == 'ca':
                    if true_false == True:
                        print('La operació %s és certa' % inp)
                    else:
                        print('La operació %s és falsa' % inp)
                else:
                    if true_false == True:
                        print('The operation %s is True' % inp)
                    else:
                        print('The operation %s is False' % inp)
            elif "clear" == inp or "cls" in shell or "esborra" == inp or "esborrar" == inp:
                clear()
                    
            elif inp == "":
                continue

            elif inp == "lang" or inp == "idioma" or inp == "language" in shell:
                if lang == 'ca':
                    print('Idioma: Català')
                else:
                    print('Language: English')
            elif inp == "canviar llengua" or inp == "canviar idioma":
                builtins.lang = 'en'
                if lang == 'en':
                    print('Language changed')
                else:
                    continue
            elif inp == "change language":
                builtins.lang = 'ca'
                if lang == 'ca':
                    print('Idioma canviat')
                else:
                    pass

            elif "zen" and "python" in shell or "Zen" and "Python" in shell:
                import this

            elif "ping" in shell:
                ping(shell[1])
            
            elif "http" and "server" in shell:
                run()
                
            elif "history" == inp or "historial" == inp:
                history = open('tmp/shell_log.log', 'r')
                print(history.read())
                
            elif "encrypt" in shell or "encripta" in shell or "encode" in shell:
                del shell[0]
                sjoin = ' '.join(shell)
                s = sjoin.encode('utf-8')
                encode(s)
                
            elif "decrypt" in shell or "desencripta" in shell or "decode" in shell:
                del shell[0]
                sjoin = ''.join(shell)
                s = str.encode(sjoin)
                decode(s)

            elif "delete" and "history" in shell or "esborrar" and "historial" in shell or "clear" and "history" in shell:
                delete_content('tmp/shell_log.log')

            elif "registrar" and "classe" in shell or "register" and "class" in shell:
                classe = Class()
            elif "registrar" and "classes" in shell or "register" and "classes" in shell:
                try:
                    while True:
                        classe = Class()
                except KeyboardInterrupt:
                    pass

            else:
                if lang == 'ca':
                    print('Aquesta ordre no s\'ha reconegut!')
                else:
                    print('This is not a known command!')

                
    except KeyboardInterrupt:
        print('Session has ended because Ctrl-C has been pressed')
        
else:
    exit()
