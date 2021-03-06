import pytest
from uuid import uuid4
from flask import Response
import requests

def test_get_pingout():

    response_create = requests.post("http://localhost:5000/create-pingout")
    response_create_json = response_create.json()
    created_uuid = response_create_json['uuid']

    response_get = requests.get("http://localhost:5000/" + created_uuid)
    response_get_json = response_get.json()
    pingout = response_get_json['pingout']

    assert created_uuid == pingout["uuid"]

def test_create_pingout(client):
    """ Test request methods of create pingout
        Testando a requisição do '/create_pingout' pelos métodos GET e POST que são listados em
        @app.route("/create-pingout", methods=['POST', 'GET']), percebe-se que a função não está funcionando
        corretamente para o método GET pois a resposta recebida não é igual a esperada.
        Assim ao executar:
        curl -X GET http://localhost:5000/create-pingout
        não é exibido:
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>405 Method Not Allowed</title>
        <h1>Method Not Allowed</h1>
        <p>The method is not allowed for the requested URL.</p>

        Atualmente, não está sendo exibido nada.
    """
    rPost = client.post('/create-pingout', data='', follow_redirects=True)
    rGet = client.get('/create-pingout', query_string='')

    assert rPost.status_code == 201
    assert rGet != Response(status=405)


def test_ping_valid_uuid(client, db_collection):
    """ Test request method ping
    É testado o caso em que a uuid é válida e não há nenhum ping anterior"""
    response = client.post('/create-pingout')
    uuid = response.json['uuid']
    url = '/' + uuid + '/ping'
    response_ping = client.post(url)
    ping = db_collection.find_one(({'uuid': uuid}))
    assert ping['uuid'] == uuid
    assert len(ping['pings']) == 1
    assert response_ping.status_code == 201

def test_ping_greater_than_one(client, db_collection):
    """ Test request method ping
    É testado o caso em que a uuid é válida e há dois pings anteriores"""
    response = client.post('/create-pingout')
    uuid = response.json['uuid']
    url = '/' + uuid + '/ping'
    for count_ping in range(2):
        response_ping = client.post(url)
        ping = db_collection.find_one(({'uuid': uuid}))
        assert ping['uuid'] == uuid
        assert len(ping['pings']) == count_ping + 1
        assert response_ping.status_code == 201

def test_ping_uuid_not_in_database(client, db_collection):
    """ Test request method ping
    É testado o caso em que a uuid é válida mas não está no banco de dados"""
    uuid = uuid4().hex
    db_collection.delete_many(({'uuid': uuid}))
    url = '/' + uuid + '/ping'
    response = client.post(url)
    assert response.status_code == 404
    assert response.json['errors'] == 'Pingout not found'

def test_ping_bad_format_uuid(client):
    """ Test request method ping
    É testado o caso que a uuid não é valida, ie, está um formato inválido"""
    uuid = str(uuid4())
    url = '/' + uuid + '/ping'
    response = client.post(url)
    assert response.status_code == 400
    assert response.json['errors'] == 'Bad format uuid'
