from supabase import Client
from pokedex_data.common.models.config import SupaBaseConfig


def prepare_supabase_client(supabase_config: SupaBaseConfig) -> Client:
    return Client(supabase_config.url, supabase_config.key)
