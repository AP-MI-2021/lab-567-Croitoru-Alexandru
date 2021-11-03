def creeaza_obiect(id, nume, descriere, pret, locatie):
    lista = []
    lista.append(id)
    lista.append(nume)
    lista.append(descriere)
    lista.append(pret)
    lista.append(locatie)
    return lista

def get_id(obiect):
    return obiect[0]

def get_nume (obiect):
    return obiect [1]

def get_descriere (obiect):
    return obiect [2]

def get_pret (obiect):
    return obiect [3]

def get_locatie (obiect):
    return obiect [4]

def to_string (obiect):
    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie: {}". format(
        getId(obiect),
        getNume (obiect),
        getDescriere (obiect),
        getPret (obiect),
        getLocatie(obiect)
        )