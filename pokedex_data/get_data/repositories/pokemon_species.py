import requests
from pokedex_data.common.models.config import PokeApiConfig
from pokedex_data.common.utils.pokemon import get_game_soft_by_generation
from pokedex_data.get_data.interfaces import PokemonSpeciesRepository
from pokedex_data.get_data.models.pokemon_species import (
    FlavorTextsJson,
    GeneraJson,
    NamesJson,
    PokemonSpecies,
)


class PokemonSpeciesRepositoryImpl(PokemonSpeciesRepository):
    def __init__(self, poke_api_config: PokeApiConfig) -> None:
        self._poke_api_config = poke_api_config

    def get_pokemon_species(self, name: str) -> PokemonSpecies:
        species_response = requests.get(
            self._poke_api_config.endpoint + f"/pokemon-species/{name}"
        )
        if species_response.status_code != 200:
            raise Exception(
                "'pokemon-species'エンドポイントからのデータ取得に失敗しました。"
            )
        species_json = species_response.json()
        names = NamesJson.model_validate(species_json["names"])
        genera = GeneraJson.model_validate(species_json["genera"])
        flavor_text = FlavorTextsJson.model_validate(
            species_json["flavor_text_entries"]
        )
        return PokemonSpecies(
            name=names.get_name(),
            genus=genera.get_genus(),
            flavor_text=flavor_text.get_flavor_text(
                get_game_soft_by_generation(self._poke_api_config.generation)
            ),
        )
