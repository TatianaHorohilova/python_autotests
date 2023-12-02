import requests

response = requests.get(url='https://api.pokemonbattle.me:9104/trainers',
 json={
        "city": "Вворонеж",
        "get_history_battle": "0",
        "id": "3682",
        "level": "1",
        "photo": "/images/trainer_avatar_06.png",
        "pokemons": [],
        "pokemons_alive": [],
        "pokemons_in_pokeballs": [],
        "trainer_name": "Фло"
    },   headers={'Content-Type': 'application/json', 'trainer_token': 'c566196054570f009254b047740dcea4'})

print=(response)