import pytest
from flask import Response

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
    print(ping)
    assert ping['uuid'] == uuid
    assert ping['pings'][0]['count'] == 1
    assert response_ping.status_code == 201
