import random

class Virag:

    def __init__(self, nev, tipus, ar):
        self.nev = nev
        self.tipus = tipus
        self.ar = ar
        
    
def beker():
    nev = " "
    tipus = " "
    ar = 0
    while nev != "":
        nev = input("\nMi a virág neve? ")
        if nev != "":
            tipus = input("Mi a virág típusa? ")
            if tipus != "":
                ar = general(750,3000)
                print("A virág ára:", ar, "Ft")
                vir = Virag(nev, tipus, ar)
                virag_lista.append(vir)
            

def general(alsohatar, felsohatar):
    return random.randrange(alsohatar, felsohatar)
    

def kiir():
    print("\nA listában szereplő adatok:")
    for vir in virag_lista:
        print("A virág neve:", vir.nev, "típusa:", vir.tipus, "ára:", vir.ar, "Ft")

    
def legdragabb():
    index = 0
    for i in range(len(virag_lista)):
        if virag_lista[i].ar > virag_lista[index].ar:
            index = i

    print("\nA legdrágább virág neve:", virag_lista[index].nev, "típusa:", virag_lista[index].tipus, "ára:", virag_lista[index].ar, "Ft")


def fajlba_iras():
    fajl = open("adatok.txt", "w")
    for i in range(len(virag_lista)):
        sor = virag_lista[i].nev + ";" + virag_lista[i].tipus + ";" + str(virag_lista[i].ar) + "Ft\n"
        fajl.write(sor)
    fajl.close()
    print("\nA fájlba írás megtörtént.")


def keres_ar():
    talalat = False
    keresett = input("\nKérem a keresett árat! ")
    try:
        keresett = int(keresett)
    except:
        print("Nem számot adott meg.")
    if keresett >= 0:
        for i in range(len(virag_lista)):
            if virag_lista[i].ar == keresett:
                print("A keresett virág neve:", virag_lista[i].nev, "típusa:", virag_lista[i].tipus, "ára:", virag_lista[i].ar, "Ft")
                talalat = True
    if not talalat:
        print("\nNem szerepel a keresett ár.")
    

virag_lista = []

beker()
kiir()
legdragabb()
fajlba_iras()
keres_ar()
