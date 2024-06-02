import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '50ebc532edfc09b2f4d2a83137829113'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4159'

def test_get_trainers_status_code():
    response = requests.get(f'{URL}/trainers')
    assert response.status_code == 200

def test_get_trainers_name():
    response_trainers_name = requests.get(f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_trainers_name.json()["data"][0]["trainer_name"] == "Alyx" 


