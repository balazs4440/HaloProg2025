import random

#Lista
szamok = []

#Feltötése
for i in range(100):
    szam=random.randint(10, 99)
    szamok.append(szam)

#ell
print(len(szamok),szamok)