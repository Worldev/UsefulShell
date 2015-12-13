import webbrowser
import os

def work_web():
    """ Inputs a website and saves it to tmp/url_work.txt """
    if lang == 'ca':
        listdir = os.listdir('tmp')
        if 'url_work.txt' in listdir:
             work_url = open('tmp/url_work.txt', 'r').read()
        else:
            work_url = input('Url (sense http://): ')
            save = input('Guardar? ')
            save = save.lower()
    else:
        listdir = os.listdir('tmp')
        if 'url_work.txt' in listdir:
            work_url = open('tmp/url_work.txt', 'r').read()
        else:
            work_url = input('Url (without http://): ')
            save = input('Save? ')
            save = save.lower()
    try:
        if save == "yes" or save == "sí" or save == "y" or save == "s":
            document = open('tmp/url_work.txt', 'w')
            document.write(work_url)
            document.close()
            webbrowser.open('http://' + work_url)
        else:
            webbrowser.open('http://' + work_url) #work link
    except NameError:
        webbrowser.open('http://' + work_url) #work link
