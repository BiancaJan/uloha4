def faktorial(n:int):   #sprehladnuje kod
    fakt = 1
    for i in range(1,n+1):
        fakt = fakt * i
    return fakt
#print(faktorial(5))
# tu moze byt strasny kod
#print(faktorial(8))
#c = 10
#print(faktorial(c))

#kombinačné číslo
def kombi(n:int, k:int):
    return faktorial(n)//(faktorial(n-k)*faktorial(k))
print(kombi(7,3)) #ma tu byt nieco napriklad nase kommbinacne cislo


def Pas_Troj(vyska:int):
    for riadok in range(0,vyska):
        for item in range(0,riadok+1):
            print(kombi(riadok,item),end=" ")
        print("\n")
Pas_Troj(4)

#primitivne typy su predavane hodnotou int a float

def troj1(vyska:int,znak:str):
    for riadok in range (0,vyska):
        for item in range (0,riadok + 1):
            print(znak,end=" ")
        print(" ")
troj1(4,"*")


def troj1b(vyska:int, znak:str):
    for riadok in range(0,vyska):
        print(znak*(riadok+1))

troj1b(4,"*")

def troj2(vyska:int,znak:str):
    for riadok in range(0,vyska):
        print(" "*(vyska-(riadok+1)),end="")
        print(znak*(2*(riadok+1)))
#musi byt 1 hviezdicka v prvom potom 3 v druhom atd
#preprogramovat program tak aby boli hviezdy spravne
troj2(4,"*")


