from Tests.test_CRUD import test_adauga_obiect, test_sterge_obiect, test_mutare_obiect, test_concatenare_obiect, \
    test_cmmp_locatie, test_ordonare_obiecte_pret, test_suma_preturi_locatie
from Tests.test_domeniu import test_obiect

def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_sterge_obiect()
    test_mutare_obiect()
    test_concatenare_obiect()
    test_cmmp_locatie()
    test_ordonare_obiecte_pret()
    test_suma_preturi_locatie()
