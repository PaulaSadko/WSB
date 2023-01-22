def przywitanie(imie, nazwisko, wiek):
    print('Siema', imie)
    if wiek >=18:
       print('Szanowny', nazwisko)

dict = {'imie' : 'Kamil' , 'nazwisko' : 'Kowalski'}
x = input ('Podaj imie, nazwisko i wiek - oddziel spacja').split()

przywitanie(x[0],x[1], int(x[2]))
przywitanie(dict['imie'], dict['nazwisko'], 22)


#rob cos tak dlugo az warunek bedzie spelniony
#pin = '1234'
#while True:
#    x = input('wprowadz pin')
#    if x == pin:
#       przywitanie()
#        break
#print('Kolejna instrukcja')

#x = 0
#while x != 'Kamil' or y == 5:
#   x = input('Podaj imie')

