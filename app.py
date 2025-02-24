import requests
from flask import Flask, render_template


def fetch_pokemon_list(limit=151):
    """
    Get a list of pokemon from pokeapi.
    :param limit: Number of pokemon we pull from pokeapi.
    :return: List of Pokémon with their name and detail URL.
    """
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)
    response.raise_for_status()  # raise error for bad response
    data = response.json()
    return data["results"]


def fetch_pokemon_details(url):
    """
    Get individual pokemons details like name, type, abilities, etc.
    :param url: Endpoint for pokemon data.
    :return: JSON data for the pokemon.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def process_pokemon_data(details):
    """
    Grab and process the relevant data for our pokemon.
    :param details: JSON data of our pokemon.
    :return: Dictionary of all fields we want to show for each pokemon.
    """
    return {
        "id": details.get("id"),
        "name": details.get("name"),
        "image": details.get("sprites", {}).get("front_default"),
        "types": [t["type"]["name"] for t in details.get("types", [])],
        "abilities": [a["ability"]["name"] for a in details.get("abilities", [])],
        "stats": {
            stat["stat"]["name"]: stat["base_stat"] for stat in details.get("stats", [])
        },
        "weight": details.get("weight"),
        "height": details.get("height"),
        "base_experience": details.get("base_experience"),
    }


def categorize_pokemon_cards(pokemon_cards):
    """
    Categorize pokemon based on their types (ie fire, water, grass).
    :param pokemon_cards: List of pokemon card dictionaries.
    :return: Dictionary mapping each type to a list of Pokémon cards.
    """
    categories = {}
    for card in pokemon_cards:
        for poke_type in card["types"]:
            if poke_type not in categories:
                categories[poke_type] = []
            categories[poke_type].append(card)
    return categories


# initialize app
app = Flask(__name__)


@app.route("/")
def index():
    # fetch list of pokemon (limited to 151 for original 151 pokemon in first gen)
    pokemon_list = fetch_pokemon_list(limit=151)
    pokemon_cards = []
    # fetch details for each pokemon
    for pokemon in pokemon_list:
        details = fetch_pokemon_details(pokemon["url"])
        card = process_pokemon_data(details)
        pokemon_cards.append(card)

    # group pokemon based on type
    categories = categorize_pokemon_cards(pokemon_cards)

    # send grouped data to html template
    return render_template("index.html", categories=categories)


if __name__ == "__main__":
    app.run(debug=True)
