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
