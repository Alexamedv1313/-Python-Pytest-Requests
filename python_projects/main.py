import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '50ebc532edfc09b2f4d2a83137829113'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    'name': 'ALEXA',
    'photo': 'https://dolnikov.ru/pokemons/albums/001.png'
} 

body_change = {
    "pokemon_id": "26696",
    "name": "ALEXA2",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_pokeball = {
    "pokemon_id": "26694"
}

response = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_create) 
print (response.json)

responce_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print (responce_change.json) 

responce_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(responce_pokeball.json)
