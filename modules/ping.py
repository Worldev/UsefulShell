import platform
import subprocess


def ping():
    """ This function ping a website and returns 0 if up or >0 if down """
    hostname = shell[1]
    if platform.system() == "Windows":
        response = subprocess.call("ping -n 1 " + hostname)
    else:
        response = subprocess.call("ping -c 1 " + hostname)

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