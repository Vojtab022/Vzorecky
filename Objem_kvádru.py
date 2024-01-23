print ('Vítejte v aplikaci pro výpočet objem kvádru')

a = input ('Zadejte délku strany a: ')
b = input ('Zadejte délku strany b: ')
c = input ('Zadejte délku strany c: ')

a = int(a)
b = int(b)
c = int(c)

if a>0 and b>0 and c>0:
    print('Výsledek je: ')
    print(a*b*c)
else:
    print('Co pak to děláš? Ty troubo zadal jsi zápor')