import webbrowser
import os

def mail():
    """ Opens a website and saves it to tmp/url_mail.txt if wanted """
    if lang == 'ca':
        listdir = os.listdir('tmp')
        if 'url_mail.txt' in listdir:
             mail_url = open('tmp/url_mail.txt', 'r').read()
        else:
            mail_url = input('Url (sense http://): ')
            save = input('Guardar? ')
            save = save.lower()
    else:
        listdir = os.listdir('tmp')
        if 'url_mail.txt' in listdir:
            mail_url = open('tmp/url_mail.txt', 'r').read()
        else:
            mail_url = input('Url (without http://): ')
            save = input('Save? ')
            save = save.lower()
    try:
        if save == "yes" or save == "sí" or save == "y" or save == "s":
            document = open('tmp/url_mail.txt', 'w')
            document.write(mail_url)
            document.close()
            webbrowser.open('http://' + mail_url)
        else:
            webbrowser.open('http://' + mail_url) #work link
    except NameError:
        webbrowser.open('http://' + mail_url) #work link