#!/usr/bin/env python3
# Python 3.5 needed
__author__ = "Miquel Comas"
__copyright__ = "Copyright 2015, The UsefulShell Project"
__credits__ = "Miquel Comas"
__license__ = "GPLv3"
__version__ = "0.1"
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

            
        except ImportError:
            print('A module has failed to load')
            exit()

        def run():
            """ This function opens a port in your localhost.
             The default port is 8000 in order to not cause trouble
             to any apache/php server in 8080, even though, you will be prompted."""
            que = queue.Queue(-1)
            queue_handler = logging.handlers.QueueHandler(que)
            handler_listener = logging.StreamHandler()
            listener = logging.handlers.QueueListener(que, handler_listener)
            httplog = logging.getLogger('tcpserver')
            httplog.addHandler(queue_handler)
            formatter = logging.Formatter('%(threadName)s: %(message)s')
            handler_listener.setFormatter(formatter)
            listener.start()
            try:
                PORT = int(input("Port [8000]: "))
            except ValueError:
                PORT = 8000
                                   
            
            Handler = http.server.SimpleHTTPRequestHandler
            try:
                httpd = socketserver.TCPServer(("", PORT), Handler)
            

                print("serving at port", PORT)
            
                httplog.info('HOST: localhost')
                httplog.info('PORT: ' + str(PORT))
                try:
                    httpd.serve_forever()
                    listener.stop()
                except KeyboardInterrupt:
                    print('Server stopped.'+"\n")
            except OSError:
                print('I couldn\'t stablish connection to this port.')
                print("\n")
                print('Only one usage of each socket address (protocol/network address/port) is normally permitted.')
                print("\n")
                print('Check if you have another connection to the port %s and close it.' % PORT)

        class Class:
            """ This class registers a group (e.g. school class) into a txt file.
            You can adapt the code to register anything you want """
            try:
                def __init__(self):
                    try:
                        os.mkdir('Classes')
                    except FileExistsError:
                        pass
                    self.teach = input('Tutor: ')
                    self.email = input('Teacher\'s email: ')
                    self.number = input('Students number: ')
                    def save(self):
                        self.classe = input('Class: ')
                        print('---------')
                        self.file = open('Classes/' + self.classe + '.txt', 'w')
                        self.file.write('======= Class of %s =======' % self.classe + "\n")
                        self.file.write("Tutor: " + self.teach + "\n")
                        self.file.write("Email: " + self.email + "\n")
                        self.file.write("Students number: " + self.number)
                        self.file.close()

                    save(self)
                    
                    

            except KeyboardInterrupt:
                pass
                
        try:
            if sys.argv[1] == 'http' or sys.argv[1] == 'httpd' or sys.argv[1] == 'server':
                run()
            elif sys.argv[1] == 'class':
                classe = Classe()
            elif sys.argv[1] == 'classes':
                try:
                    while True:
                        classe = Classe()
                except EOFError:
                    pass
                except KeyboardInterrupt:
                    pass
            else:
                pass
        except IndexError:
            pass

        print('OS: ' + platform.system() + ' --> Init time: ' + time.asctime())
        logging.basicConfig(filename='shell_log.log', level=logging.INFO)
        logging.info(' Initialization time: ' + time.asctime())
        logging.info(' OS: ' + platform.system())
        lang = input('Choose your language (en/ca) [en]: ')
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
          
        def ajuda():
            """ This function displays help when called """
            if lang == 'ca':
                print('''Aquesta consola està en mode de desenvolupador.''')
                input('''Prem Enter per continuar...''')
                print('''
Per dir "igual a" has de posar ==
Creació de variables: !. variable = 'valor'
Per fer ping (i comprovar si el host està en línia), la sintaxi és: ping domini.com
Pots encriptar un missatge escrivint "encripta <missatge>"''')
                input('''Prem Enter per continuar...''')
                print("\n" + '''Ctrl+C per aturar la consola''')
            else:
                print('''This shell is in developer mode.''')
                input('''Press Enter to continue''')
                print('''
To say "equal to" you have to put ==
Creation of variables: !. variable = 'value'
To make ping (and check if host is up), the syntax is: ping domain.com
You can encrypt a message writing "encrypt <message>"''')
                input('''Press Enter to continue...''')
                print("\n" + '''Ctrl+C To stop the shell''')

        def clear():
            """ This function "clears" the screen by printing 100 "\n" """
            print("\n" * 100)

        def ping():
            """ This function ping a website and returns 0 if up or >0 if down """
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            hostname = shell[1]
            if platform.system() == "Windows":
                response = subprocess.call("ping -n 1 " + hostname, startupinfo=si)
            else:
                response = subprocess.call("ping -c 1 " + hostname, startupinfo=si)

            if response == 0:
                if lang == 'ca':
                    print(hostname, 'està en línia')
                else:
                    print(hostname, 'is up!')
            else:
                if lang == 'ca':
                    print(hostname, 'no està en línia')
                else:
                    print(hostname, 'is down!')

        def encode(s):
            """ This function encodes a message with base64 standard encode """
            encoded_text = base64.standard_b64encode(s)
            encoded_string = bytes.decode(encoded_text)
            print(encoded_string)

        def decode(s):
            """ This function decodes a message with base64 standard decode """
            decoded_text = base64.standard_b64decode(s)
            decoded_string = bytes.decode(decoded_text)
            print(decoded_string)
      

        def delete_content(filename):
            with open(filename, "w") as file:
                file.seek(0)
                file.truncate()

        
        while True:
            inp = input("> ")
            logging.info(' Input: ' + inp)
            shell = inp.split()
            
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
        
            elif "feina"  and "cole" in shell or "work" and "school" in shell or "feina" and "escola" in shell:
                webbrowser.open('http://www.escolatecnos.cat/campus/login/index.php')

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
                true_false = eval(inp)
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
                lang = 'en'
                if lang == 'en':
                    print('Language changed')
                else:
                    continue
            elif inp == "change language":
                lang = 'ca'
                if lang == 'ca':
                    print('Idioma canviat')
                else:
                    pass

            elif "!." in shell:
                try:
                    try:
                        dictionary = open('dictionary.variables', 'w')
                    except FileNotFoundError:
                        if lang == 'ca':
                            print('El fitxer dictionary.variables no ha estat trobat')
                        else:
                            print('The file dictionary.variables has not been found')
                    var = "%s = %s" %(shell[1], shell[3])
                    dictionary.write(var + "\n")
                    dictionary.close()
                except IndexError:
                    print('You have not entered all the variable parts!')
            
            elif "see" and "variables" in shell or "mostra" and "variables" in shell:
                seedictionary = open('dictionary.variables', 'r')
                print(seedictionary.read())


            elif "zen" and "python" in shell or "Zen" and "Python" in shell:
                import this

            elif "ping" in shell:
                ping()
            
            elif "http" and "server" in shell:
                run()
                
            elif "history" == inp or "historial" == inp:
                history = open('shell_log.log', 'r')
                print(history.read())
                
            elif "encrypt" in shell or "encripta" in shell or "encode" in shell:
                del shell[0]
                sjoin = ' '.join(shell)
                s = sjoin.encode('utf-8')
                encode(s)
                
            elif "decrypt" in shell or "desencripta" in shell or "decode" in shell:
                del shell[0]
                sjoin =  ''.join(shell)
                s = str.encode(sjoin)
                decode(s)

            elif "delete" and "history" in shell or "esborrar" and "historial" in shell or "clear" and "history" in shell:
                try:
                    delete_content('shell_log.log')
                    if lang == 'ca':
                        print('Fet')
                    else:
                        print('Done')
                except PermissionError:
                    if lang == 'ca':
                        print('No es pot accedir al fitxer perquè l\'està usant un altre procés')
                    else:
                        print('The process cannot access the file because it is being used by another process')
                except FileNotFoundError:
                    if lang == 'ca':
                        print('El fitxer no existeix.')
                    else:
                        print('The file was not found.')
                

                            
            elif "registrar" and "classe" in shell:
                classe = Classe()
            elif "registrar" and "classes" in shell:
                try:
                    while True:
                        classe = Classe()
                except KeyboardInterrupt:
                    pass
            else:
                if lang == 'ca':
                    print('Aquesta ordre no s\'ha reconegut')
                else:
                    print('This is not a known command')

                
    except KeyboardInterrupt:
        print('Session has ended because Ctrl-C has been pressed')
        
else:
    exit()
