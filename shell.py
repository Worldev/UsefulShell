#!/usr/bin/env python3.5
# Python 3.5 needed
__author__ = "Miquel Comas (Mikicat)"
__copyright__ = "Copyright 2016 Miquel Comas (Mikicat) & Worldev"
__credits__ = ["Miquel Comas (Mikicat)", "JeDa", "NeoMahler"]
__license__ = "GPLv3"
__version__ = "v1.1.2"
__maintainer__ = "Miquel Comas (Mikicat), Worldev"
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
            from modules import *
            import getpass
            import datetime
            import optparse

        except ImportError:
            print('WARNING: A module has failed to load')
            exit()

        try:
            os.mkdir('tmp')
        except FileExistsError:
            pass
        argv = None
        parser = optparse.OptionParser('%prog [options]')
        parser.add_option('--help-commands', action="store_true", dest="hc", help="Displays commands available and then exits")
        parser.add_option("-c", '--class', action="store_true", dest="classe", help="Registers a class group and then exits")
        parser.add_option("-s", '--http-server', action="store_true", dest="httpd", help="Opens a port and then exits")
        parser.add_option('--credits', action="store_true", dest="credits", help="Shows credits and then exits")
        parser.add_option('--no-color', action="store_true", dest="no_color", help="Disables shell color")
        opts, args = parser.parse_args(argv)
        if opts.hc:
            ajuda('commands')
            exit()
        elif opts.classe:
            classe = Class()
            exit()
        elif opts.httpd:
            run()
            exit()
        elif opts.credits:
            print(__credits__)
            exit()
        elif opts.no_color:
            bcolors.no_color()

        day = time.strftime("%d")
        month = time.strftime("%b")
        year = time.strftime("%Y")
        print(bcolors.HEADER + 'OS: %s --> Init time: %s' % (platform.system(), time.asctime()) + bcolors.ENDC)
        if day == "25" and month == "Dec":
            print("Merry Christmas!")
        elif day == "01" and month == "Jan":
            print("Happy new", year, "!")
        else:
            pass
        logging.basicConfig(filename='tmp/shell_log.log', level=logging.INFO)
        logging.info(' Initialization time: ' + time.asctime())
        logging.info(' OS: ' + platform.system())
        builtins.lang = input('Choose your language (en/ca) [en]: ')
        if lang == '':
            lang = 'en'
        else:
            pass
            
        if lang == 'ca':
            print(bcolors.HEADER + 'Benvinguts a la consola d\'ajuda en desenvolupament a partir de Python 3.5.')
            print('Escriviu ajuda o help per a obtenir ajuda' + "\n" 'Escriu "show c" per veure les condicions de llicència, o "show w" per veure la garantia' + bcolors.ENDC)
            logging.info(' Language: ' + lang)
        else:
            print(bcolors.HEADER + 'Welcome to the helping shell in development based off Python 3.5.')
            print('Type "help" to obtain help' + "\n" + 'Type "show c" to see the License conditions, or "show w" to see the warranty' + bcolors.ENDC)
            logging.info(' Language: ' + lang)

        first_run()

        def clear():
            os.system('cls' if os.name=='nt' else 'clear')
            return ''

        while True:
            try:
                dircd = newcd
            except NameError:
                dircd = os.path.expanduser('~')
            inp = input(bcolors.OKGREEN + getpass.getuser() + '@' + platform.node() + ' ' + dircd + "> " + bcolors.ENDC)
            if "cd" in inp:
                pass
            else:
                np = inp.lower()
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
            try:
                if "ftp" == shell[0]:
                    try:
                        ftpserver = FTPConnect(shell[1], int(shell[2]), shell[3], shell[4])
                    except ValueError:
                        print(bcolors.WARNING + 'Syntax: <host> <port> <user> <passwd>' + bcolors.ENDC)
                    except ConnectionRefusedError:
                        print(bcolors.FAIL + 'Connection refused' + bcolors.ENDC)
                    except IndexError:
                        print(bcolors.WARNING + 'Syntax: <host> <port> <user> <passwd>' + bcolors.ENDC)
                else:
                    pass
            except IndexError:
                pass
            if "print" in shell or "show" in shell or "echo" in shell or "mostra" in shell or "ensenya" in shell:
                if inp == 'show c':
                    print("type 'show c all' to display all the conditions")
                    print("or 'show c short' to display the first point")
                elif inp == 'show c all':
                    conditions_all()
                elif inp == 'show c short':
                    conditions_short()
                elif inp == 'show w':
                    warranty()
                else:
                    del shell[0]
                    print(' '.join(shell))

            elif "stop" in shell or "exit" in shell or "finish" in shell or "end" in shell or "final" in shell or "fi" in shell or "acabar" in shell or "bye" in shell or "quit" in shell:
                if lang == 'ca':
                    print('Final de la Sessió.')
                    exit(0)
                else:
                    print('Session End.')
                    exit(0)
                break

            elif "cd" in shell:
                try:
                    try:
                        if shell[1] == '..':
                            newcd = os.path.abspath(os.path.join(dircd, os.pardir))
                        elif shell[1] == '.':
                            newcd = dircd
                        elif ':' in shell[1]:
                            dircd = shell[1]
                        else:
                            if platform.system() == 'Windows':
                                os.listdir(dircd + '\%s' % shell[1])
                                newcd = dircd + '\%s' % shell[1]
                            else:
                                os.listdir(dircd + '/%s' % shell[1])
                                newcd = dircd + '/%s' % shell[1]
                    except FileNotFoundError:
                        print('The system cannot find the file/directory specified')
                    except OSError:
                        print('There was a problem')
                except IndexError:
                    print("cd where?")

            elif "ls" in shell or "list" in shell or "llista" in shell:
                if platform.system() == 'Windows':
                    lsdir = os.listdir(dircd)
                    print("\n".join(lsdir))
                else:
                    if "ls" in shell:
                        subprocess.call(shell)
                    else:
                        lsdir = os.listdir(dircd)
                        print("\n".join(lsdir))

            elif "docs" in shell:
                webbrowser.open("https://github.com/Worldev/UsefulShell/wiki")

            elif inp == "feina" or inp == "work":
                work_web()

            elif "mirar" and "correu" in shell or "check" and "mail" in shell:
                mail()
            
            elif "ajuda" in shell or "help" in shell:
                try:
                    ajuda(shell[1])
                except IndexError:
                    ajuda(None)
  
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

            elif "zen" in shell:
                import this

            elif "ping" in shell:
                try:
                    ping(shell[1])
                except IndexError:
                    print('What I\'m supposed to ping?')
            
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
            elif "search" in shell or "busca" in shell or "cerca" in shell:
                del shell[0]
                search('+'.join(shell))
                
            elif "usefulshell" and "logo" in shell:
                webbrowser.open('https://github.com/Worldev/UsefulShell/images/usefulshell_logo.png')
            elif "copyright" in shell:
                print(__copyright__)


            elif "web" in shell or "browser" in shell or "browse" in shell or "navega" in shell:
                try:
                    if not 'http://' in shell[1]:
                        webbrowser.open('http://' + shell[1])
                    else:
                        webbrowser.open(shell[1])
                except IndexError:
                    if lang == 'ca':
                        print("Sintaxi: web/navega <url>")
                    else:
                        print("Syntax: web/browser/browse <url>")

            elif "credits" in shell:
                print(__credits__)

            else:
                try:
                    retcode = subprocess.call(inp, shell=True)
                    if retcode < 0:
                        print("Child was terminated by signal", -retcode, file=sys.stderr)
                    else:
                        print("Child returned", retcode, file=sys.stderr)
                except OSError as e:
                    print("Execution failed:", e, file=sys.stderr)
                    if lang == 'ca':
                        print(bcolors.FAIL + 'Aquesta ordre no s\'ha reconegut!' + bcolors.ENDC)
                    else:
                        print(bcolors.FAIL + 'This is not a known command!' + bcolors.ENDC)


    except KeyboardInterrupt:
        print('Session has ended because Ctrl-C has been pressed')
        
else:
    print('Shell: I\'m not supposed to be included!')