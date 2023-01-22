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

for i in range (len(content)):
#lec przez wszystkie linie
    content[i] = content[i].replace('\n','')
    content[i] = content[i].split(';')


#wez linie 0,1,2,3 itd itd
#print(content)
#print(content[5])
#print(content[5][3])


#dane = 'Paula.Michał.Psiulek'
#print(dane)
#dane2 = dane.split('.')
#splitowanie po kropce
#print(dane2)

#2. Obliczanie średniej wypłaty

total = 0
for i in range(1, len(content)):
    #total = total + int(content[i][1])
    total += int(content[i][1])
average = total/(len(content)-1)
print('Srednia wynosi' , round(average,2), 'zlotych')
print(f'Srednia wynosi {round(average, 2)} zlotych')


#3. Oblicz ile kobiet jest na macierzynskim
total = 0
for i in range(1, len(content)):
    if content[i][4] == 't':
        total += 1
print(total)

#slowo = 'mama.tata'
#slowo = slowo.replace('.',' ',2)
#print(slowo)