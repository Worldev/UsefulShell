import os
import platform
import webbrowser

def first_run():
    if 'first_run.cache' in os.listdir('tmp'):
        pass
    else:
        if platform.system() == 'Windows':
            first_run_cache = open('tmp/first_run.cache', 'w')
            if lang == 'ca':
                git = input('Vols descarregar Git per a Windows? (s/n): ')
            else:
                git = input('Do you want to download Git for Windows? (y/n): ')
            git = git.lower()
            if git == 'y' or git == 's':
                first_run_cache.write('Yes')
                first_run_cache.close()
                webbrowser.open('https://git-scm.com/download/win')
            else:
                first_run_cache.write('No')
                first_run_cache.close()
        else:
            pass
