#1. Odczyt pliku csv z zapisem poszczegolnych pol

#with open(path, mode) as plik_csv:
#lub incaczej można zapisać
#with open(C:\\Users\\vdi-student\\Desktop\\WSB\\rozliczenie.csv','r') as plik_csv:
path = 'C:\\Users\\vdi-student\\Desktop\\WSB\\rozliczenie.csv'
mode = 'r'
with open(path, mode) as plik_csv:
    content = plik_csv.readlines()

print(type(content))
print(len(content))
print(content)
print(content[4])
#pokaże piątą linię




