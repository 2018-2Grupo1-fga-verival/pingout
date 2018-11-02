from pingout.db import connect_to_database
from pingout.db import connect_to_collection
import pymongo
import os

DB_HOST = os.environ.get('MONGO_HOST', 'localhost')
DB_PORT = int(os.environ.get('MONGO_PORT', 27017))

def test_connect_to_database():
    client = pymongo.MongoClient(DB_HOST, DB_PORT)
    assert client['pingout_db'] == connect_to_database()

def test_connect_to_collection():
    client = pymongo.MongoClient(DB_HOST, DB_PORT)
    assert client['pingout_db']['pings_history'] == connect_to_collection(connect_to_database())