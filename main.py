#1.1 Feladat
#Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!

lista = []

while True:
    beker = input('Szám: ')
    if beker == '':
        break
    lista.append(int(beker))

print('A lista elemei:',lista)
print(f'A lista legkisebb eleme: {min(lista)}')
print(f'A lista legnagyobb eleme: {max(lista)}')

#1.2 Feladat
#Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az 'X'-et vagy 'x'-et nem üt! A számokat tárolja el a program egy listában! 
#Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!

lista = []
while True:
    szam = input("kérek egy zsamot: ")
    if szam != "x":
        lista.append(szam)
    else:
        lista.sort(key = int)
        print(lista)
        break
print("a legnagyobb szám: ", max(lista), "a legkissebb szám a :", min(lista),"a lista pedig: ", lista)

#1.3 Feladat
#Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb páros számot!

szamlista = []
paros_lista = []


while True:
    szam = input("kérek egy számot: ")
    if szam == "":
        break
    else:
        szamlista.append(int(szam))
        if int(szam) % 2 == 0:
            paros_lista.append(int(szam))

print(f"A lista elemei: {szamlista}")
print(f"A legkisebb páros szám:   {min(paros_lista)}")
print(f"A legnaygobb páros szám : {max(paros_lista)}")

#2. Feladat
#Készíts egy programot, amely a felhasználótól szavakat kér be, amíg az csupán ENTER-t nem üt! A szavakat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legrövidebb és a leghosszabb szót!

szavak = []
leghosszabb_szo = []
legrovidebb_szo = []


while True:
  szo = input("Adj meg egy szót! ")
  if szo == "":
    break
  else:
    szavak.append(szo)
    if len(szo) <= len(szavak[0]):
      legrovidebb_szo = szo
    if len(szo) > len(szavak[0]):
      leghosszabb_szo = szo


print(f"A lista szavai: {szavak} ")
print(f" {legrovidebb_szo} ")
print(f" {leghosszabb_szo} ")