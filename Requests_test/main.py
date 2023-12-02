import requests


response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
json={
    "name": "generate",
    "photo": "generate"
    },
    headers={'Content-Type': 'application/json', 'trainer_token': 'c566196054570f009254b047740dcea4'}) 

print(response)

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
json={
    "pokemon_id": "21031",
    "name": "colt",
    "photo": "https://api.pokemonbattle.me:9104/images/20230000120021815132890.png"
},
    headers={'Content-Type': 'application/json', 'trainer_token': 'c566196054570f009254b047740dcea4'}) 

print(response)

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
json={
    "pokemon_id": "21034"
},
    headers={'Content-Type': 'application/json', 'trainer_token': 'c566196054570f009254b047740dcea4'}) 

print(response)