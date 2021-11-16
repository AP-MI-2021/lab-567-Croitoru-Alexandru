from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect, mutare_obiect, concatenare_obiect, \
    ordonare_obiecte_pret, cmmp_locatie, suma_preturi_locatie


def printmenu():
    print("1. Adauga obiectul dorit")
    print("2. Sterge obiectul dorit")
    print("3. Modifica obiectul")
    print("4. Mutare obiect")
    print("5. Concatenare string cu descrierea obiectului daca pretul obiectului este mai mare decat cel dat")
    print("6. Determina cel mai mare preț pentru fiecare locație")
    print("7. Ordona obiectele crescător după prețul de achiziție")
    print("8. Afiseaza suma preturilor de pe fiecare locatie")
    print("u. Undo")
    print("r. Redo")
    print("a. Afiseaza obiectele")
    print("x. Iesire")

def ui_adauga_obiect(lista, undolist, redolist):
    id = input("Dati id-ul obiectului: ")
    nume = input("Dati numele obiectului: ")
    descriere = input("Dati descrierea: ")
    pret = float(input("Dati pretul obiectului: "))
    locatie = input("Dati locatia obiectului: ")
    rezultat = adauga_obiect(id, nume, descriere, pret, locatie, lista)
    undolist.append(lista)
    redolist.clear()
    return rezultat

def ui_sterge_obiect(lista, undolist, redolist):
    id = input("Dati id-ul obiectului ce trebuie sters: ")
    rezultat = sterge_obiect(id, lista)
    undolist.append(lista)
    redolist.clear()
    return rezultat

def ui_modificare_obiect(lista, undolist, redolist):
    id = input("Dati noul id obiectului: ")
    nume = input("Dati noul numele obiectului: ")
    descriere = input("Dati noua descriere: ")
    pret = float(input("Dati noul pret al obiectului: "))
    locatie = input("Dati noua locatie a obiectului: ")
    rezultat = modifica_obiect(id, nume, descriere, pret, locatie, lista)
    undolist.append(lista)
    redolist.clear()
    return rezultat

def ui_mutare_obiect(lista, undolist, redolist):
    id = input("Dati id-ul obiectului pe care doriti sa-l mutati: ")
    locatie = input("Dati noua locatie a obiectului: ")
    rezultat = mutare_obiect(id, locatie, lista)
    undolist.append(lista)
    redolist.clear()
    return rezultat

def ui_concatenare_obiect(lista, undolist, redolist):
    pret = float(input("Dati pretul: "))
    str = input("Dati string-ul ce doriti sa fie concatenat: ")
    rezultat = concatenare_obiect(str, pret, lista)
    undolist.append(lista)
    redolist.clear()
    return rezultat

def ui_cmmp_locatie(lista):
    locatie = input("Dati locatia unde doriti sa se realizeze determinarea obiectului cu cel mai mare pret: ")
    return cmmp_locatie(locatie, lista)

def ui_ordonare_obiecte_pret(lista, undolist, redolist):
    lista_sortata = ordonare_obiecte_pret(lista)
    undolist.append(lista)
    redolist.clear()
    return lista_sortata

def ui_suma_preturi_locatie(lista):
    rezultat = suma_preturi_locatie(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))

def ui_undo(lista, undolist, redolist):
    if len(undolist) > 0:
        redolist.append(lista)
        lista = undolist.pop()
        print(lista)
    else:
        print("Nu se mai poate da redo!")

def ui_redo(lista, undolist, redolist):
    if len(redolist) > 0:
        undolist.append(lista)
        lista = redolist.pop()
        print(lista)
    else:
        print("Nu se mai poate da redo!")

def run_menu(lista):
    obiect = []
    undolist = []
    redolist = []
    while True:
        printmenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adauga_obiect(lista, undolist, redolist)
        elif optiune == "2":
            lista = ui_sterge_obiect(lista, undolist, redolist)
        elif optiune == "3":
            lista = ui_modificare_obiect(lista, undolist, redolist)
        elif optiune == "4":
            lista = ui_mutare_obiect(lista, undolist, redolist)
        elif optiune == "5":
            lista = ui_concatenare_obiect(lista, undolist, redolist)
        elif optiune == "6":
            lista = ui_cmmp_locatie(lista)
            print(max)
        elif optiune == "7":
            lista = ui_ordonare_obiecte_pret(lista, undolist, redolist)
        elif optiune == "8":
            lista = ui_suma_preturi_locatie(lista)
        elif optiune == "a":
            print(lista)
        elif optiune == 'u':
            ui_undo(lista, undolist, redolist)
        elif optiune == 'r':
            ui_redo(lista, undolist, redolist)
        elif optiune == "x":
            break
        else:
            print("Optiune eronata, reincercati!")

