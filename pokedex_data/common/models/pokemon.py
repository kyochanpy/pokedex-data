from typing import Sequence
from pydantic import BaseModel


class Pokemon(BaseModel):
    name: str
    url: str


class Pokemons(BaseModel):
    pokemons: Sequence[Pokemon]
