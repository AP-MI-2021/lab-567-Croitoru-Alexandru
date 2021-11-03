#Calcule, retineri de date
from Domain.Obiect import creeaza_obiect, get_id, get_pret, get_descriere, get_nume, get_locatie


def adauga_obiect(id, nume, descriere, pret, locatie, lista): #lista - adaugam lista de dictionare
    '''
    adauga un obiect intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: lista cu noul obiect introdus
    '''
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]

def sterge_obiect(id, lista):
    '''
    sterge un obiect din inventar
    :param id: id-ul obiectului ce trebuie sters
    :param lista: lista de obiecte
    :return: lista fara obiectul care a trebuit sa fie sters
    '''
    return [obiect for obiect in lista if get_id(obiect) != id]

def modifica_obiect(id, nume, descriere, pret, locatie, lista):
    '''
    modifica un obiect dupa id
    :param id: id-ul obiectului de modificat
    :param nume: numele obiectului de modificat
    :param descriere: descrierea obiectului de modificat
    :param pret: pretul obiectului de modificat
    :param locatie: locatia obiectului de modificat
    :param lista: lista de obiecte
    :return: lista modificata
    '''
    lista_noua = []
    for obiect in lista:
        if get_id(obiect) == id:
            obiect_nou = creeaza_obiect(id, nume, descriere, pret, locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua

def get_by_id(id, lista):
    '''
    gaseste un obiect dupa id-ul dat din lista
    :param id: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat din lista
    '''
    for obiect in lista:
        if get_id(obiect) == id:
            return obiect
    return None

#Functionalitate 2.2

def mutare_obiect(id, locatie, lista):
    '''
    Muta un obiect dintr-o locatie in alta
    :param id: string
    :param locatie: string
    :param lista: lista de obiecte
    :return: obiectul cu noua locatie in lista
    '''
    lista_noua = []
    for obiect in lista:
        if get_id(obiect) == id:
            nume = get_nume(obiect)
            descriere = get_descriere(obiect)
            pret = get_pret(obiect)
            obiect_nou = creeaza_obiect(id, nume, descriere, pret, locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua

#Functionalitate 2.3

def concatenare_obiect(str, pret, lista):
    '''
    concatezenaza str-ul la descriere daca pretul obiectului este mai mare decat pretul dat
    :para![](C:/Users/flexr/AppData/Local/Temp/download.jpg)m str: string
    :param pret: float
    :param lista: lista de obiecte
    :return: lista in care s-au concatenat obiectele daca pretul este mai mare decat cel dat
    '''
    lista_noua = []
    for obiect in lista:
        if get_pret(obiect) > pret:
            id = get_id(obiect)
            nume = get_nume(obiect)
            descriere = get_descriere(obiect) + str
            pret = get_pret(obiect)
            locatie = get_locatie(obiect)
            obiect_nou = creeaza_obiect(id, nume, descriere, pret, locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua













