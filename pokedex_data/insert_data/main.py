from pokedex_data.common.models.config import Config
from pokedex_data.insert_data.interfaces import (
    InsertPokemonTypeRepository,
    InsertPokemonsRepository,
    InsertTypesRepository,
)
import polars as pl


def main(
    *,
    config: Config,
    insert_pokemons_repository: InsertPokemonsRepository,
    insert_types_repository: InsertTypesRepository,
    insert_pokemon_type_repository: InsertPokemonTypeRepository,
):
    df = pl.read_csv(f"data/csv/generation_{config.poke_api.generation}.csv")
    insert_pokemons_repository.insert_pokemons(df)
    insert_types_repository.insert_types(df)
    insert_pokemon_type_repository.insert_pokemon_type(df)
