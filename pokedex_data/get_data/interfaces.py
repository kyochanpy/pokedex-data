from abc import ABC, abstractmethod

from pokedex_data.get_data.models.pokemon import Pokemon


class PokemonRepository(ABC):
    @abstractmethod
    def get_pokemon(self, name: str) -> Pokemon: ...
