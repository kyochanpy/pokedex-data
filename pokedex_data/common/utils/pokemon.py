from typing import Sequence
import requests

from pokedex_data.common.models.pokemon import GenPokemon
from pokedex_data.common.utils.config import load_config


def get_pokemon_names_by_generation(generation: int) -> Sequence[str]:
    config = load_config()
    response = requests.get(config.poke_api.endpoint + f"/generation/{generation}")
    if response.status_code != 200:
        raise Exception("ポケモン一覧の取得に失敗しました。")
    pokemons = GenPokemon.model_validate(response.json())
    return [pokemon.name for pokemon in pokemons.pokemons]


def get_game_soft_by_generation(generation: int) -> str:
    generation_game_soft = {
        1: "red",
        2: "gold",
        3: "ruby",
        4: "daimond",
        5: "black",
        6: "x",
        7: "sun",
        8: "sword",
        9: "scarlet",
    }
    return generation_game_soft[generation]
