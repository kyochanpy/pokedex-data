from pokedex_data.common.utils.config import load_config
from pokedex_data.put_image.main import main
from pokedex_data.put_image.repositories.create_bucket import CreateBucketRepositoryImpl
from pokedex_data.put_image.repositories.put_image import PutImageRepositoryImpl


if __name__ == "__main__":
    config = load_config()
    main(
        create_bucket_repository=CreateBucketRepositoryImpl(config.supabase),
        put_image_repository=PutImageRepositoryImpl(config.supabase),
    )
