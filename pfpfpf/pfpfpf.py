#harjutus 8.2

import random

for a in range(1,101):
 print(a)
a = int(input("sisestage ülaltoodut number:"))

while a>100 !=True:
 try:
   a = int(input("sisestage veel kord:"))
 except:
  ValueError

if a % 2 == 0:
 print("see on paaris number")
 print("tsükkel on lõpp")

elif a % 2 == 1:
 print("see on paaritu number")
 print("tsükkel on lõpp")



#harjutus 8.1
import random

a = random.randint(1, 100)

a = int(input("siseta number:"))

while a > 100:
 try:
   a = int(input("sisesta veel kord:"))
 except:
  ValueError

if a % 2 == 0:

 print("paaris number")

 print("tsükkel on lõpp")

elif a % 2 == 1:

 print("paaritu number")

 print("tsükkel on lõpp")

 from math import*
from random import*
#harjutus 0.2
katsed=0
answer=""
while answer!="10111":
    answer=input("palun kirjutage postindeks!")
    katsed+=1
    print(f"katsed: {katsed}")
    print()





#harjutus0.1
print("palun kirjutage postindeks")
katsed=0
while True:
    answer=input("palun kirjutage postindeks!")
    katsed +=1
    if answer.lower()=="10111":
        print(f"teil postindeks kirjutakse kulus {katsed} katse.")
        break
    #22
print("ma tahan kommi")
katsed=0
while True:
    answer=input("tahan kommi!")
    katsed +=1
    if answer.lower()=="komm":
        print(f"teil kommid kirjutakse kulus {katsed} katse.")
        break
    #22.2
katsed=0
answer=""
while answer!="komm":
    answer=input("tahan kommi!")
    katsed+=1
    print(f"katsed: {katsed}")
    print()
#0
p=0
while True:
    number=int(input("sisestage number suurem kui 10: "))
    p+=1
    if number >=10:
        print("õigesti")
        break
    else:
        print("arv on liiga väike",)
print("katsed",p)




#ülesane 11
print("arvuti mõistatab numbrit 1-10 ja sina üritad seda ära arvata.")
a=randint(1,10)
vastus=int(input("mis arv on mõistatanud arvutit?:  "))
k=p=1
while vastus!=a:
    print("Ära sa ei arvunud ära, proovi uuesti!:  ")
    vastus=int(input("sisesta vastus:  "))
    k+=1
    p+=1
    if k>2:
        print("püüdlused on lõppenud")
        b=input("proovi veel kord")
        if b.upper()=="JÄH":
         k=0
         continue
        else:
            break
if vastus==a:
    print("palju õnne;sa arvasid ära!",p)
print() 

#harjutus 6
n=0
print ("*kolmnurga")
for e in range (11,0,-1):
    n = n+1
    for f in range (0, n+1):
        print ("*", end = "")
    print()
print("")
