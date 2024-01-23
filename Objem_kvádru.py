#Uvítání
print ('Vítejte v aplikaci pro výpočet objem kvádru')
#Deklarace proměných
a = input ('Zadejte délku strany a: ')
b = input ('Zadejte délku strany b: ')
c = input ('Zadejte délku strany c: ')
#Přetypování na int
a = int(a)
b = int(b)
c = int(c)
#Kontrola záporného čísla
if a>0 and b>0 and c>0:
    print('Výsledek je: ')
    print(a*b*c)
#Pokud není splněná podmínka tak napíše výsledek
else:
    print('Co pak to děláš? Ty troubo zadal jsi zápor')