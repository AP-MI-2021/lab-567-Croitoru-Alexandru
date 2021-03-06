from Domain.Obiect import get_id, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import adauga_obiect, get_by_id, sterge_obiect, mutare_obiect, concatenare_obiect, cmmp_locatie, \
    ordonare_obiecte_pret, suma_preturi_locatie
from UserInterface.console import ui_adauga_obiect, ui_undo


def test_adauga_obiect():
    lista = []
    lista = adauga_obiect('1', 'pixuri', 'scriere cu cerneala albastra', 3.2, 'camera 208', lista)
    assert len(lista) == 1
    assert get_id(get_by_id('1', lista)) == '1'
    assert get_nume(get_by_id('1', lista)) == 'pixuri'
    assert get_descriere(get_by_id('1', lista)) == 'scriere cu cerneala albastra'
    assert get_pret(get_by_id('1', lista)) == 3.2
    assert get_locatie(get_by_id('1', lista)) == 'camera 208'

def test_sterge_obiect():
    lista = []
    lista = adauga_obiect('1', 'pixuri', 'scriere cu cerneala albastra', 3.2, 'camera 208', lista)
    lista = adauga_obiect('2', 'creioane', 'scriere cu carbune', 1.6, 'camera 230', lista)

    lista = sterge_obiect('1', lista)
    assert len(lista) == 1
    assert get_by_id('1', lista) == None

    lista = sterge_obiect ("3", lista)
    assert len(lista) == 1
    assert get_by_id ("2", lista) is not None

#Functionalitate 2.2

def test_mutare_obiect():
    lista = []
    lista = adauga_obiect('1', 'pixuri', 'scriere cu cerneala albastra', 3.2, 'camera 208', lista)
    lista = adauga_obiect('2', 'creioane', 'scriere cu carbune', 1.6, 'camera 233', lista)
    lista = adauga_obiect('3', 'carioca', 'scriere cu tus', 5.1, 'camera 245', lista)

    lista = mutare_obiect('1', 'camera 233', lista)

    obiect_mutat = get_by_id('1', lista)
    assert get_id(obiect_mutat) == '1'
    assert get_nume(obiect_mutat) == 'pixuri'
    assert get_descriere(obiect_mutat) == 'scriere cu cerneala albastra'
    assert get_pret(obiect_mutat) == 3.2
    assert get_locatie(obiect_mutat) == 'camera 233'

#Functionalitate 2.3

def test_concatenare_obiect():
    lista = []
    lista = adauga_obiect('1', 'pixuri', 'albastra', 3.2, 'camera 208', lista)
    lista = adauga_obiect('2', 'creioane', 'carbune', 1.6, 'camera 233', lista)
    lista = adauga_obiect('3', 'carioca', 'tus', 5.1, 'camera 245', lista)
    lista = adauga_obiect('4', 'rigle', 'cerneala', 10, 'camera 245', lista)

    lista = concatenare_obiect('verde', 7, lista)

    obiect_concatenat0 = get_by_id('1', lista)
    obiect_concatenat1 = get_by_id('2', lista)
    obiect_concatenat2 = get_by_id('3', lista)
    obiect_concatenat3 = get_by_id('4', lista)

    assert len(lista) == 4
    assert get_descriere(obiect_concatenat0) == "albastra"
    assert get_descriere(obiect_concatenat1) == "carbune"
    assert get_descriere(obiect_concatenat2) == "tus"
    assert get_descriere(obiect_concatenat3) == "cernealaverde"

#Functionalitate 2.4

def test_cmmp_locatie():
    lista = []
    lista = adauga_obiect('1', 'pixuri', 'albastra', 3.2, 'camera 233', lista)
    lista = adauga_obiect('2', 'creioane', 'carbune', 1.6, 'camera 233', lista)
    lista = adauga_obiect('3', 'carioca', 'tus', 5.1, 'camera 245', lista)
    lista = adauga_obiect('4', 'rigle', 'cerneala', 10, 'camera 245', lista)

    assert cmmp_locatie('camera 233', lista) == 3.2
    assert cmmp_locatie('camera 245', lista) == 10

#Functionalitate 2.5

def test_ordonare_obiecte_pret():
    lista = []
    lista = adauga_obiect('1', 'pixuri', 'albastra', 3.2, 'camera 233', lista)
    lista = adauga_obiect('2', 'creioane', 'carbune', 1.6, 'camera 233', lista)
    lista = adauga_obiect('3', 'carioca', 'tus', 5.1, 'camera 245', lista)
    lista = adauga_obiect('4', 'rigle', 'cerneala', 10, 'camera 245', lista)

    lista_sortata = ordonare_obiecte_pret(lista)

    assert get_id(lista_sortata[0]) == '2'
    assert get_id(lista_sortata[1]) == '1'
    assert get_id(lista_sortata[2]) == '3'
    assert get_id(lista_sortata[3]) == '4'

def test_suma_preturi_locatie():
    lista = []
    lista = adauga_obiect('1', 'pixuri', 'albastra', 3, 'camera 233', lista)
    lista = adauga_obiect('2', 'creioane', 'carbune', 4.8, 'camera 233', lista)
    lista = adauga_obiect('3', 'carioca', 'tus', 5.1, 'camera 245', lista)
    lista = adauga_obiect('4', 'rigle', 'cerneala', 10, 'camera 245', lista)

    rezultat = suma_preturi_locatie(lista)

    assert rezultat['camera 233'] == 7.8
    assert rezultat['camera 245'] == 15.1

# UNDO / REDO

def test_undo_redo():
    lista = []
    undolist = []
    redolist = []

    lista = adauga_obiect('1', 'pixuri', 'albastra', 3, 'camera 233', lista)
    undolist.append(lista)
    lista = adauga_obiect('2', 'creioane', 'carbune', 4.8, 'camera 233', lista)
    undolist.append(lista)
    lista = adauga_obiect('3', 'carioca', 'tus', 5.1, 'camera 245', lista)
    undolist.append(lista)
    lista = adauga_obiect('4', 'rigle', 'cerneala', 10, 'camera 245', lista)
    undolist.append(lista)

    assert len(lista) == 4

    lista, undolist, redolist = ui_undo(lista, undolist, redolist)

    assert len(lista) == 3
    assert get_by_id('1',lista) is not None
    assert get_by_id('2', lista) is not None
    assert get_by_id('3', lista) is not None
    assert get_by_id('4', lista) in None





