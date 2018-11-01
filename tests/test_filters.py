from pingout.db import connect_to_database
from pingout.db import connect_to_collection
from pingout.filters import *
import pytest as py
import datetime
import time

def test_filter_pings_of_invalid_type_date():
    """ Test if is a valid date type
        Testando captura de ValueError, percebe-se que a função não recebe uma string
        por esse motivo, a filtragem de data por
        curl -X POST http://localhost:5000/d76ec767721d4cc0bee1bdb3c36a3014/filter/?initial_date=2018-01-01&final_date=2018-02-02
        não funciona, pois está sendo passada uma string

        Assim, datas no formato pedido : "2018-01-01" não funciona no método
    """

    uuid = '13667dae53c84f13872ed4295347783e'
    collection =  connect_to_collection(connect_to_database())

    right_date = datetime.datetime.now()
    wrong_date = '2018-10-02'
    with py.raises(ValueError) as info:
        filter_pings_of_date(uuid, collection, wrong_date)


def test_filter_pings_range_of_dates_check_types():
    """Check of dates types

        Como o anterior, não aceita data no formato string
    """

    uuid = '13667dae53c84f13872ed4295347783e'
    collection =  connect_to_collection(connect_to_database())

    right_initial = datetime.datetime.now()
    time.sleep(1)
    right_final = datetime.datetime.now()

    wrong_initial = '2018-10-02'
    wrong_final = '2018-10-02'

    with py.raises(ValueError):
        # filter_pings_range_of_dates(uuid, collection, right_initial, right_final)
        filter_pings_range_of_dates(uuid, collection, wrong_initial, right_final)
        filter_pings_range_of_dates(uuid, collection, right_initial, wrong_final)
        filter_pings_range_of_dates(uuid, collection, wrong_initial, wrong_final)
