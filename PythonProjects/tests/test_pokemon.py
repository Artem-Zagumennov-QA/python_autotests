import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'

TRAINER_ID = 'USER_ID'

def test_status_code():
    answer = requests.get(url = f'{URL}/trainers')
    assert answer.status_code == 200

def test_part_of_answer():
    answer_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert answer_get.json()['data'][0]['trainer_name'] == '.......'

