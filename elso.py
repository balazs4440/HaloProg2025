import random

#Lista
szamok = []

#Feltötése
while len(szamok)!=40:
    szam=random.randint(10, 99)
    if szam not in szamok:
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
        if (tipp < kitalalando_szam):
            print("Tippelj nagyobbat!")
        else:
            print("Tippelj kissebbet!")
        tipp_sz= input("[Kilépés X el lehetséges] \n Tippelj újra! :")
        if(tipp_sz.isdecimal()):
            tipp= int(tipp_sz)
        elif (tipp_sz == "X"):
            exit()
        else:
            print("Egész számmal játsz!")
            continue
    print("Kitaláltad!")

    folytat=input("Szeretnél még játszani? [I/N]")

    if(folytat=="N"):
        jatszol=False
