#Uvítání+nabídka možností
print ('Vítejte v aplikaci pro výpočet matematických vzorečků')
print("1.Obvod obdelníku")
print("2.Obsah obdelníku")
print ("3.Objem kvádru")
print("4.Obsah kruhu")
#Výběr vzorečku který budeme počítat
vyber = input("Vyberte si co budeme dnes počítat zadáním čísla 1-4: ")
#Kontroluje jaký byl vybrán vzoreček
if vyber == "1":
    #Deklarace proměných
    a = input ('Zadejte délku strany a: ')
    b = input ('Zadejte délku strany b: ')
    #Přetypování na int
    a = int(a)
    b = int(b)
    #Kontrola záporného čísla
    if a>0 and b>0:
        print('Výsledek je: ')
        print(2*a+2*b)
    #Pokud není splněná podmínka tak napíše výsledek
    else:
        print('Co pak to děláš? Ty troubo zadal jsi zápor')
#Kontroluje jaký byl vybrán vzoreček
elif vyber == "2":
    #Deklarace proměných
    a = input ('Zadejte délku strany a: ')
    b = input ('Zadejte délku strany b: ')
    #Přetypování na int
    a = int(a)
    b = int(b)
    #Kontrola záporného čísla
    if a>0 and b>0:
        print('Výsledek je: ')
        print(a*b)
    #Pokud není splněná podmínka tak napíše výsledek
    else:
        print('Co pak to děláš? Ty troubo zadal jsi zápor')
#Kontroluje jaký byl vybrán vzoreček
elif vyber == "3":
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
#Kontroluje jaký byl vybrán vzoreček
elif vyber =="4":
    #Deklarace proměných
    r = input ('Zadejte poloměr kruhu r: ')
    #Vložení math
    import math
    #Přetypování na int
    r = int(r)
    #Kontrola záporného čísla
    if r>0:
        print('Výsledek je: ')
        print(math.pi*(r**2))
    #Pokud není splněná podmínka tak napíše výsledek
    else:
        print('Co pak to děláš? Ty troubo zadal jsi zápor')
#Kontroluje jestli nebyl vybrán špatný vzoreček
else:
    print ("Nevybral sis žádnou z možností")