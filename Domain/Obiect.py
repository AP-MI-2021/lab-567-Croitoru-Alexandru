def creeaza_obiect(id, nume, descriere, pret, locatie):
    '''
    creeaza un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: un dictionar ce retine un obiect
    '''
    return {
        'id' : id,
        'nume' : nume,
        'descriere' : descriere,
        'pret' : pret,
        'locatie' : locatie
    }

def get_id(obiect):
    '''
    preia id-ul obiectului
    :param obiect: dictionar de tipul obiect
    :return: id-ul obiectului
    '''
    return obiect['id']

def get_nume(obiect):
    '''
    preia numele obiectului
    :param obiect: dictionar de tipul obiect
    :return: numele obiectului
    '''
    return obiect['nume']

def get_descriere(obiect):
    '''
    preia descrierea obiectului
    :param obiect: dictionar de tipul obiect
    :return: descrierea obiectului
    '''
    return obiect['descriere']

def get_pret(obiect):
    '''
    preia pretul obiectului
    :param obiect: dictionar de tipul obiect
    :return: pretul obiectului
    '''
    return obiect['pret']

def get_locatie(obiect):
    '''
    preia locatia obiectului
    :param obiect: dictionar de tipul obiect
    :return: locatia obiectului
    '''
    return obiect['locatie']

def to_string(obiect): # Are un rol estetic, pentru a il pune in consola cum vrem noi sa arate
    return 'id : {}, nume : {}, descriere : {}, pret : {}, locatie : {}'.format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret(obiect),
        get_locatie(obiect)
    )