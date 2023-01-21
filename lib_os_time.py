#biblioteka os
#to jest zestaw instrukcji, niektóre są dodane do systyemu
#c = 'paula'
#print(len(c))
#pokazuje ilość znaków
#len jest wbudowany

import os
#daje dostęp do funkcji systemowych
#standardowa biblioteka, która już jest wgrana

print(os.getcwd())
#sprawdź current working directory, gdzie jestem

#from os import *
#drugi sposób na import wszystkiego * z bliioteki funkcji metod klas

os.chdir('C:\\Users\\vdi-student\\Desktop')
#zawsze w pythonie dwa \\ dzialaja jak jednen \, w ścieżce html to nie obowiązuje

print(os.getcwd())
#ponownie sprawdzamy lokalizajcę

os.mkdir('new_folder')
#tworzenie nowego folderu


