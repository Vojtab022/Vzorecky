#Uvítání
print ('Vítejte v aplikaci pro výpočet obsah kruhu')
#Deklarace proměných
r = input ('Zadejte poloměr kruhu r: ')
#Vložení math
import math
#Přetypování na int
r = int(r)
#Kontrola záporného čísla
if r>0:
    print('Výsledek je: ')
    print(math.pi*r**2)
#Pokud není splněná podmínka tak napíše výsledek
else:
    print('Co pak to děláš? Ty troubo zadal jsi zápor')