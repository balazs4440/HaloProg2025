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
jatek_szam=1
nem_talaltDB=0

kitalalando_szam = szamok[random.randint(0,len(szamok))]

jatszol = True

while(jatszol):
    tipp_sz=input("Tippelj egy pozitív egész számot!: ").strip()
    if(tipp_sz.isdecimal()):
        tipp= int(tipp_sz)
    else:
        print("Egész számmal játsz!")
        tipp = 123
        continue
    
    while (tipp!=kitalalando_szam):
        nem_talaltDB+=1
        if (tipp == 123):
            pass
        elif (tipp < kitalalando_szam):
            print("Tippelj nagyobbat!")
        elif (tipp > kitalalando_szam):
            print("Tippelj kissebbet!")
        tipp_sz= input("[Kilépés X el lehetséges] \n Tippelj újra! :")
        if (tipp_sz.isdecimal()):
            tipp= int(tipp_sz)
        elif (tipp_sz == "X"):
            print(f"{jatek_szam} db szám kitalálásához {nem_talaltDB}-szor próbálkozott rosszul.")
            exit()
        else:
            print("Egész számmal játsz!")
            continue
    print("Kitaláltad!")

    folytat=input("Szeretnél még játszani? [I/N]")
    if (folytat=="N"):
        jatszol=False
        print(f"{jatek_szam} db szám kitalálásához {nem_talaltDB}-szor próbálkozott rosszul.")
    elif (folytat=="I"):
        jatek_szam+=1
