import pytest
import requests

def test_get_pingout():
    
    response_create = requests.post("http://localhost:5000/create-pingout")
    response_create_json = response_create.json()
    created_uuid = response_create_json['uuid']

    response_get = requests.get("http://localhost:5000/" + created_uuid)
    response_get_json = response_get.json()
    pingout = response_get_json['pingout']

    assert created_uuid == pingout["uuid"]