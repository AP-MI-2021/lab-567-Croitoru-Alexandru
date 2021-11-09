from Domain.Obiect import creeaza_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie

def test_obiect():
    obiect = creeaza_obiect('1', 'pixuri', 'scriere cu cerneala albastra', 3.2, 'camera 208')
    assert get_id(obiect) == '1'
    assert get_nume(obiect) == 'pixuri'
    assert get_descriere(obiect) == 'scriere cu cerneala albastra'
    assert get_pret(obiect) == 3.2
    assert get_locatie(obiect) == 'camera 208'