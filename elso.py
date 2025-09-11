import random

#Lista
szamok = []


#Feltötése
for i in range(100):
    szam=random.randint(10, 99)
    szamok.append(szam)

#ell
#print(len(szamok),szamok)

#egyszam jatek
print("Számkitalálós játék!")
jatek_szam=0
nem_talaltDB=0

kitalalando_szam = szamok[random.randint(0,len(szamok))]

jatszol = True

while(jatszol):
    tipp = int(input("Tippelj egy pozitív egész számot!: "))

    while(tipp!=kitalalando_szam):
        print("Nem talált!")
        tipp= int(input("Tippelj újra!: "))
    print("Kitaláltad!")

    folytat=input("Szeretnél még játszani? [I/N]")

    if(folytat=="N"):
        jatszol=False
