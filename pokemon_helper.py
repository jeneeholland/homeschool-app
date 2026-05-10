import random
import requests
from datetime import datetime

def get_daily_pokemon():
    today_key = datetime.now().strftime("%Y-%m-%d")
    random.seed(today_key)

    pokemon_ids = random.sample(range(1, 152), 3)

    daily_pokemon = []

    for pokemon_id in pokemon_ids:
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        pokemon_response = requests.get(pokemon_url)
        pokemon_data = pokemon_response.json()

        pokemon_name = pokemon_data["name"].title()
        pokemon_image = pokemon_data["sprites"]["front_default"]

        pokemon_types = [
            item["type"]["name"].title()
            for item in pokemon_data["types"]
        ]

        daily_pokemon.append({
            "name": pokemon_name,
            "image": pokemon_image,
            "types": pokemon_types
        })

    return daily_pokemon