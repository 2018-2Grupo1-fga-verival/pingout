from pingout.db import connect_to_database
from pingout.db import connect_to_collection
from pingout.filters import filter_pings_of_date
import pytest as py
import datetime

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
    wrong_date = 'lfjladaldal'
    with py.raises(ValueError) as info:
        filter_pings_of_date(uuid, collection, right_date)
