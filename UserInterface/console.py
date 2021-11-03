from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect, mutare_obiect, concatenare_obiect


def printmenu():
    print("1. Adauga obiectul dorit")
    print("2. Sterge obiectul dorit")
    print("3. Modifica obiectul")
    print("4. Mutare obiect")
    print("5. Concatenare string cu descrierea obiectului daca pretul obiectului este mai mare decat cel dat")
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

def ui_mutare_obiect(lista):
    id = input("Dati id-ul obiectului pe care doriti sa-l mutati: ")
    locatie = input("Dati noua locatie a obiectului: ")
    return mutare_obiect(id, locatie, lista)

def ui_concatenare_obiect(lista):
    pret = float(input("Dati pretul: "))
    str = input("Dati string-ul ce doriti sa fie concatenat: ")
    return concatenare_obiect(str, pret, lista)

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
        elif optiune == "4":
            lista = ui_mutare_obiect(lista)
        elif optiune == "5":
            lista = ui_concatenare_obiect(lista)
        elif optiune == "a":
            print(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune eronata, reincercati!")