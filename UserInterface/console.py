from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect

def printmenu():
    print("1. Adauga obiectul dorit")
    print("2. Sterge obiectul dorit")
    print("3. Modifica obiectul")
    print("a. Afiseaza obiectele")
    print("x. Iesire")

def ui_adauga_obiect(lista):
    id = input("Dati id-ul obiectului: ")
    nume = input("Dati numele obiectului: ")
    descriere = input("Dati descrierea: ")
    pret = float(input("Dati pretul obiectului: "))
    locatie = input("Dati locatia obiectului: ")
    return adauga_obiect(id, nume, descriere, pret, locatie, lista)

def ui_sterge_obiect(lista):
    id = input("Dati id-ul obiectului ce trebuie sters: ")
    return sterge_obiect(id, lista)

def ui_modificare_obiect(lista):
    id = input("Dati noul id obiectului: ")
    nume = input("Dati noul numele obiectului: ")
    descriere = input("Dati noua descriere: ")
    pret = float(input("Dati noul pret al obiectului: "))
    locatie = input("Dati noua locatie a obiectului: ")
    return modifica_obiect(id, nume, descriere, pret, locatie, lista)

def run_menu(lista):
    while True:
        printmenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adauga_obiect(lista)
        elif optiune == "2":
            lista = ui_sterge_obiect(lista)
        elif optiune == "3":
            lista = ui_modificare_obiect(lista)
        elif optiune == "a":
            print(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune eronata, reincercati!")