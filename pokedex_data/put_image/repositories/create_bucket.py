from pokedex_data.common.clients.supabase import prepare_supabase_client
from pokedex_data.common.models.config import SupaBaseConfig
from pokedex_data.put_image.interfaces import CreateBucketRepository


class CreateBucketRepositoryImpl(CreateBucketRepository):
    def __init__(self, supabase_config: SupaBaseConfig):
        self._supabase_config = supabase_config
        self._supabase_client = prepare_supabase_client(supabase_config)

    def create_bucket(self, bucket_name: str) -> None:
        self._supabase_client.storage.create_bucket(bucket_name)
