from typing import Mapping, Sequence
import polars as pl
from polars import DataFrame
from pokedex_data.common.clients.supabase import prepare_supabase_client
from pokedex_data.common.models.config import SupaBaseConfig
from pokedex_data.insert_data.interfaces import InsertPokemonTypeRepository


class InsertPokemonTypeReositoryImpl(InsertPokemonTypeRepository):
    def __init__(self, supabase_config: SupaBaseConfig):
        self._supabase_config = supabase_config
        self._supabase_client = prepare_supabase_client(self._supabase_config)
        self._type_and_id = {
            "normal": 1,
            "fire": 2,
            "water": 3,
            "electric": 4,
            "grass": 5,
            "ice": 6,
            "fighting": 7,
            "poison": 8,
            "ground": 9,
            "flying": 10,
            "psychic": 11,
            "bug": 12,
            "rock": 13,
            "ghost": 14,
            "dragon": 15,
            "dark": 16,
            "steel": 17,
            "fairy": 18,
        }

    def _get_pokemon_and_id(self) -> Mapping[str, int]:
        response = self._supabase_client.table("pokemons").select("id, name").execute()
        rows: Sequence[Mapping[str, int | str]] = response.data
        return {row["name"]: row["id"] for row in rows}

    def _get_pokemon_and_type_id(self, df: DataFrame) -> Mapping[str, int]:
        pokemon_and_is = self._get_pokemon_and_id()
        pokemon_and_types_df = df.select(["name", "type_1", "type_2"])
        pokemon_and_type_df = pokemon_and_types_df.melt(
            id_vars=["name"], value_vars=["type_1", "type_2"]
        ).drop_nulls(subset=["value"])
        pokemon_and_type_df = pokemon_and_type_df.with_columns(
            pl.col("name").replace_strict(pokemon_and_is).alias("pokemon_id")
        )
        pokemon_and_type_df = pokemon_and_type_df.with_columns(
            pl.col("value").replace_strict(self._type_and_id).alias("type_id")
        )
        return pokemon_and_type_df.select(["pokemon_id", "type_id"]).to_dicts()

    def insert_pokemon_type(self, df: DataFrame) -> None:
        self._supabase_client.table("pokemon_type").insert(
            self._get_pokemon_and_type_id(df)
        ).execute()
