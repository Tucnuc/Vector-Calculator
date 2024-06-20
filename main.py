# ----------------
#  MENU + IMPORTY
# ----------------

from math import sqrt, pow, acos, degrees

def menu():
    moznosti = [
        (delkaMenu, "Délka Vektoru"),
        (skalarMenu, "Skalární Součin"),
        (vektorovySoucin, "Vektorový Součin"),
        (odchylkyMenu, "Odchylka Vektorů")
    ]

    for index, (func, desc) in enumerate(moznosti):
        print(f"\033[1m{index + 1}.\033[0m {desc}")
    print("")
    numChoice = int(input("Co chceš spočítat? [číslo]: ")) - 1
    print("")
    if 0 <= numChoice < len(moznosti):
        func, _ = moznosti[numChoice]
        func()
    else:
        print("Špatná odpověď.")


# -------------------------------
#  POSKLADANE FUNKCE PRO VYPOCTY
# -------------------------------

# CELKOVY VYPOCET ODCHYLKY
def odchylkyMenu():
    choice = str(input("Jsou vektory ve 2D nebo 3D? [1 - 2D, 2 - 3D]: "))
    print("")
    if choice == "1":
        vypocetOdchylky(4)
    elif choice == "2":
        vypocetOdchylky(6)
    else:
        print("Špatná odpověď.")

def vypocetOdchylky(pocetSlozek):
    ziskatVektory(pocetSlozek, True)
    skalarSoucin()
    vektorDelka(2)
    ziskatUhel()
    startAgain()


# CELKOVY VYPOCET DELKY
def delkaMenu():
    choice = str(input("Je vektor ve 2D nebo 3D? [1 - 2D, 2 - 3D]: "))
    print("")
    if choice == "1":
        vypocetDelky(4)
    elif choice == "2":
        vypocetDelky(6)
    else:
        print("Špatná odpověď.")

def vypocetDelky(pocetSlozek):
    ziskatVektory(pocetSlozek, False)
    vektorDelka(1)
    print(f"Délka tvého vektoru je: \033[1m{round(finalVektor, 2)} j\033[0m")
    print("")
    startAgain()


# CELKOVY SKALAR SOUCIN
def skalarMenu():
    choice = str(input("Jsou vektory ve 2D nebo 3D? [1 - 2D, 2 - 3D]: "))
    print("")
    if choice == "1":
        vypocetSkalar(4)
    elif choice == "2":
        vypocetSkalar(6)
    else:
        print("Špatná odpověď.")

def vypocetSkalar(pocetSlozek):
    ziskatVektory(pocetSlozek, True)
    skalarSoucin()
    print(f"Skalární součin tvých vektorů je: \033[1m{round(finalSkalar, 2)}\033[0m")
    print("")
    startAgain()


# CELKOVY VEKTOROVY SOUCIN
def vektorovySoucin():
    ziskatVektory(6, True)
    vektorSoucin()
    print(f"Tvůj vektorový součin je: \033[1m{finalVektorSoucin}\033[0m")
    print("")
    startAgain()


# -------------------
#  VEKTOROVE OPERACE
# -------------------

# ZISKANI VEKTORU
vektor1 = []
vektor2 = []
def ziskatVektory(pocetSlozek, dvojice):
    global vektor1, vektor2

    if dvojice:
        vektorInt = 1
        vektor = vektor1
        for _ in range(2):
            slozkaInt = 1
            for _ in range(pocetSlozek // 2):
                slozka = float(input(f"Zadej {slozkaInt}. složku {vektorInt}. vektoru: "))
                vektor.append(slozka)
                slozkaInt += 1
            vektorInt += 1
            vektor = vektor2
    else:
        slozkaInt = 1
        for _ in range(pocetSlozek // 2):
            slozka = float(input(f"Zadej {slozkaInt}. složku vektoru: "))
            vektor1.append(slozka)
            slozkaInt += 1
    print("")

# VYPOCET SKALARNIHO SOUCINU
finalSkalar = 0
def skalarSoucin():
    index = 0
    skalary = []
    
    for _ in range(len(vektor1)):
        skalar = vektor1[index] * vektor2[index]
        skalary.append(skalar)
        index += 1
        
    global finalSkalar
    for skalar in skalary:
        finalSkalar += skalar

# VYPOCET DELKY VEKTORU
finalVektor = 1
def vektorDelka(pocet):
    vektory = []
    vektor = vektor1
    for _ in range(pocet):
        index = 0
        delka = 0
        for _ in range(len(vektor1)):
            delka += pow(vektor[index], 2)
            index += 1
        vektory.append(sqrt(delka))
        vektor = vektor2

    global finalVektor
    for vektor in vektory:
        finalVektor *= vektor

# ZISKANI UHLU
def ziskatUhel():
    cosFi = finalSkalar / finalVektor
    uhel = degrees(acos(cosFi))
    stupne = int(uhel)
    minuty = round((uhel - stupne) * 60)

    print(f"Tvoje odchylka je: \033[1m{stupne}° {minuty}'\033[0m")
    print("")

# VEKTOROVY SOUCIN
finalVektorSoucin = []
def vektorSoucin():
    cycleRepetition = 1
    for _ in range(3):
        if cycleRepetition == 1:
            index1 = 1
            index2 = 2
        elif cycleRepetition == 2:
            index1 = 2
            index2 = 0
        elif cycleRepetition == 3:
            index1 = 0
            index2 = 1
        
        vektor = 0
        vektor += ((vektor1[index1] * vektor2[index2]) - (vektor1[index2] * vektor2[index1]))
        
        global finalVektorSoucin
        finalVektorSoucin.append(vektor)
        cycleRepetition += 1


# -----------------
#  START + RESTART
# -----------------

# RESTART APP
def startAgain():
    choice = str(input("Další výpočet? [1 - ano, 2 - ne]: "))
    if choice == "1":
        print("")
        global vektor1, vektor2, finalSkalar, finalVektor
        vektor1 = []
        vektor2 = []
        finalSkalar = 0
        finalVektor = 1
        menu()
    elif choice == "2":
        print("")
    else:
        print("Špatná odpověď.")

# START APP
menu()