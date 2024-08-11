from pokedex_data.common.clients.supabase import prepare_supabase_client
from pokedex_data.common.models.config import SupaBaseConfig
from pokedex_data.put_image.interfaces import PutImageRepository


class PutImageRepositoryImpl(PutImageRepository):
    def __init__(self, supabase_config: SupaBaseConfig):
        self._supabase_config = supabase_config
        self._supabase_client = prepare_supabase_client(supabase_config)

    def put_image(self, bucket_name: str, image_path: str, image: bytes) -> None:
        self._supabase_client.storage.from_(bucket_name).upload(
            path=image_path, file=image
        )
