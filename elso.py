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
    tipp_sz=input("Tippelj egy pozitív egész számot!: ").strip()
    if(tipp_sz.isdecimal()):
        tipp= int(tipp_sz)
    else:
        print("Egész számmal játsz!")
        continue
    
    while(tipp!=kitalalando_szam):
        print("Nem talált!")
        tipp_sz= input("Tippelj újra!: ")
        if(tipp_sz.isdecimal()):
            tipp= int(tipp_sz)
        else:
            print("Egész számmal játsz!")
            continue
    print("Kitaláltad!")

    folytat=input("Szeretnél még játszani? [I/N]")

    if(folytat=="N"):
        jatszol=False
