from polars import DataFrame
from pokedex_data.common.clients.supabase import prepare_supabase_client
from pokedex_data.common.models.config import SupaBaseConfig
from pokedex_data.insert_data.interfaces import InsertTypesRepository


class InsertTypesReositoryImpl(InsertTypesRepository):
    def __init__(self, supabase_config: SupaBaseConfig):
        self._supabase_config = supabase_config
        self._supabase_client = prepare_supabase_client(self._supabase_config)

    def insert_types(self, df: DataFrame) -> None:
        self._supabase_client.table("types").insert(
            [
                {"id": 1, "name": "normal"},
                {"id": 2, "name": "fire"},
                {"id": 3, "name": "water"},
                {"id": 4, "name": "electric"},
                {"id": 5, "name": "grass"},
                {"id": 6, "name": "ice"},
                {"id": 7, "name": "fighting"},
                {"id": 8, "name": "poison"},
                {"id": 9, "name": "ground"},
                {"id": 10, "name": "flying"},
                {"id": 11, "name": "psychic"},
                {"id": 12, "name": "bug"},
                {"id": 13, "name": "rock"},
                {"id": 14, "name": "ghost"},
                {"id": 15, "name": "dragon"},
                {"id": 16, "name": "dark"},
                {"id": 17, "name": "steel"},
                {"id": 18, "name": "fairy"},
            ]
        ).execute()
