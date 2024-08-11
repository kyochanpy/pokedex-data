from abc import ABC, abstractmethod
import polars as pl


class InsertPokemonsRepository(ABC):
    @abstractmethod
    def insert_pokemons(self, df: pl.DataFrame) -> None: ...
