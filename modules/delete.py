
def delete_content(filename):
    """ This function deletes the history file's content """
    try:
        with open(filename, "w") as file:
            file.seek(0)
            file.truncate()
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