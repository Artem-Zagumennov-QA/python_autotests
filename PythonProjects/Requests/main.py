import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USERTOKEN'
HEADER = {'content-type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    'name':'TralaleloTralala',
    'photo_id': 319
}


answer_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(answer_create.text)
print(answer_create.status_code)

pokemon_id = answer_create.json()['id']
print(pokemon_id)


body_edit = {
    "pokemon_id": f'{pokemon_id}',
    "name": "generate",
    "photo_id": -1
}

answer_edit = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_edit )
print(answer_edit.text)
print(answer_edit.status_code)


body_catch = {
    "pokemon_id": f'{pokemon_id}'
}

answer_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch )
print(answer_catch.text)
print(answer_catch.status_code)