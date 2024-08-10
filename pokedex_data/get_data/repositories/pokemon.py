import requests
from pokedex_data.common.models.config import PokeApiConfig
from pokedex_data.get_data.interfaces import PokemonRepository
from pokedex_data.get_data.models.pokemon import Pokemon, StatsJson, TypesJson


class PokemonRepositoryImpl(PokemonRepository):
    def __init__(self, poke_api_config: PokeApiConfig):
        self._poke_api_config = poke_api_config

    def get_pokemon(self, name: str) -> Pokemon:
        pokemon_response = requests.get(
            self._poke_api_config.endpoint + f"/pokemon/{name}"
        )
        if pokemon_response.status_code != 200:
            raise Exception("'pokemon'エンドポイントからのデータ取得に失敗しました。")
        pokemon_json = pokemon_response.json()
        stats = StatsJson.model_validate(pokemon_json["stats"])
        types = TypesJson.model_validate(pokemon_json["types"])
        return Pokemon(
            order=pokemon_json["order"],
            stats=stats.parse(),
            types=types.parse(),
            weight=pokemon_json["weight"],
            height=pokemon_json["height"],
        )
