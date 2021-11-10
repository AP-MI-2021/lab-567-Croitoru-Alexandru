from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect, mutare_obiect, concatenare_obiect, cmmp_locatie, \
    ordonare_obiecte_pret
from Domain.Obiect import to_string

def helpmenu():
    print ("1. Pentru comanda adaugare obiect, introduceti id, nume, descriere, pret si locatie")
    print ("2. Pentru commanda stergere obiect, introduceti id-ul pe care doriti sa il stergeti")
    print ("3. Pentru comanda modificare, introduceti id-ul obiectului pe care doriti sa il modificati, nume, descrierea, pretul si locatia noua")
    print ("4. Pentru comanda mutare, introduceti noua locatie  si id-ul")
    print ("5. Pentru comanda concatenate, introduceti string-ul pe care doriti sa il concatenati si pretul de la care incepe concatenarea")
    print ("6.. Pentru comanda cel mai mare pret dintr-o locatie, introduceti locatia pentru care doriti sa aflati cel mai mare pret")
    print ("7. Pentru commanda  suma preturilor, nu mai introduceti niciun parametru")
    print ("a. afisare")
    print ("x. iesire")

def rum_menu():
    helpmenu()
    while True:
        comenzi = input ("Dati comenzile, separate cu punct si virgula, cu parametrii separati prin virgula: ")
        ComandaCuParametri = comenzi.split(";")
        lista = []
        for command in ComandaCuParametri:
            tokens = command.split (",")
            if tokens[0] == "adauga":
                try:
                    lista = adauga_obiect(tokens[1], tokens[2], tokens[3], float(tokens[4]), tokens[5], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif tokens[0] == "sterge":
                lista = sterge_obiect(tokens[1], lista)
            elif tokens[0] == "modifica":
                try:
                    lista = modifica_obiect(tokens[1], tokens[2], tokens[3], float(tokens[4]), tokens[5], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif tokens[0] == "mutare locatie":
                try:
                    lista = mutare_obiect(lista, tokens[1], tokens[2])
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif tokens[0] == "concatenate":
                try:
                    lista = concatenare_obiect(tokens[1], float(tokens[2]), lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif tokens [0] == "Cel mai mare pret dintr-o locatie":
                print (cmmp_locatie(tokens[1], lista))
            elif tokens[0] == "Ordonare crescator al preturilor":
                lista = ordonare_obiecte_pret(lista)
            elif tokens[0] == "show All":
                for obiect in lista:
                    print(to_string(obiect))
                print()
            elif tokens[0] == "quit":
                break
            else:
                print("Optiune gresita. Reincercati!")




