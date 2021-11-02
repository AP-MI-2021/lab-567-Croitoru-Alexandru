from Domain.Obiect import get_id, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import adauga_obiect, get_by_id, sterge_obiect


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
