from typing import Mapping, Sequence
import polars as pl
from polars import DataFrame
from pokedex_data.common.clients.supabase import prepare_supabase_client
from pokedex_data.common.models.config import SupaBaseConfig
from pokedex_data.insert_data.interfaces import InsertPokemonsRepository


class InsertPokemonsReositoryImpl(InsertPokemonsRepository):
    def __init__(self, supabase_config: SupaBaseConfig):
        self._supabase_config = supabase_config
        self._supabase_client = prepare_supabase_client(self._supabase_config)

    def _get_pokemons_columns(self, df: DataFrame) -> Sequence[Mapping[str, str | int]]:
        df = df.with_columns((pl.col("name_en") + ".png").alias("image_key"))
        df = df.with_columns((pl.col("name_en") + ".png").alias("dot_image_key"))
        pokemons_df = df.select(
            [
                "order",
                "name",
                "genus",
                "image_key",
                "dot_image_key",
                "height",
                "weight",
                "flavor_text",
            ]
        )
        return pokemons_df.to_dicts()

    def insert_pokemons(self, df: DataFrame) -> None:
        self._supabase_client.table("pokemons").insert(
            self._get_pokemons_columns(df)
        ).execute()
