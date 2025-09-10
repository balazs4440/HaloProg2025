import random

#Lista
szamok = []

#Feltötése
for i in range(100):
    szam=random.randint(10, 99)
    szamok.append(szam)

#ell
print(len(szamok),szamok)

#egyszam jatek
jatek_szam=0
nem_talaltDB=0

kitalalando_szam = szamok[random.randint(len(szamok))]

