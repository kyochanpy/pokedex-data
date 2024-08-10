from typing import Sequence
from pydantic import BaseModel


class GenPokemon(BaseModel):
    name: str
    url: str


class GenPokemons(BaseModel):
    pokemons: Sequence[GenPokemon]
