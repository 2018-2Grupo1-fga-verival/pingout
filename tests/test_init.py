

def test_ping_valid_uuid(client, db_collection):
    response = client.post('/create-pingout')
    uuid = response.json['uuid']
    url = '/' + uuid + '/ping'
    response_ping = client.post(url)
    ping = db_collection.find_one(({'uuid': uuid}))
    print(ping)
    assert ping['uuid'] == uuid
    assert ping['pings'][0]['count'] == 1
    assert response_ping.status_code == 201
