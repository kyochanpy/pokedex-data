from abc import ABC, abstractmethod
import polars as pl


class InsertPokemonsRepository(ABC):
    @abstractmethod
    def insert_pokemons(self, df: pl.DataFrame) -> None: ...


class InsertTypesRepository(ABC):
    @abstractmethod
    def insert_types(self, df: pl.DataFrame) -> None: ...


class InsertPokemonTypeRepository(ABC):
    @abstractmethod
    def insert_pokemon_type(self, df: pl.DataFrame) -> None: ...
