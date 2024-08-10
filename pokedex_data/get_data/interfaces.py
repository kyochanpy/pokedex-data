from abc import ABC, abstractmethod

from pokedex_data.get_data.models.pokemon import Pokemon
from pokedex_data.get_data.models.pokemon_species import PokemonSpecies


class PokemonRepository(ABC):
    @abstractmethod
    def get_pokemon(self, name: str) -> Pokemon: ...


class PokemonSpeciesRepository(ABC):
    @abstractmethod
    def get_pokemon_species(self, name: str) -> PokemonSpecies: ...
