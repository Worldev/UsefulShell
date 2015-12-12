#!/usr/bin/env python3
import os

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
            self.number = input('Number of students: ')
            def save(self):
                self.classe = input('Class: ')
                print('---------')
                self.file = open('Classes/' + self.classe + '.txt', 'w')
                self.file.write('======= Class of %s =======' % self.classe + "\n")
                self.file.write("Tutor: " + self.teach + "\n")
                self.file.write("Email: " + self.email + "\n")
                self.file.write("Number of students: " + self.number)
                self.file.close()

            save(self)
    except KeyboardInterrupt:
        pass