print ('Vítejte v aplikaci pro výpočet obsah obdelníku')

a = input ('Zadejte délku strany a: ')
b = input ('Zadejte délku strany b: ')

a = int(a)
b = int(b)

if a>0 and b>0:
    print('Výsledek je: ')
    print(a*b)
else:
    print('Co pak to děláš? Ty troubo zadal jsi zápor')