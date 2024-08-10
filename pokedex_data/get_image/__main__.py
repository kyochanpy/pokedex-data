from pokedex_data.common.utils.config import load_config
from pokedex_data.get_image.main import main
from pokedex_data.get_image.repositories.image import GetImageRepositoryImpl


if __name__ == "__main__":
    config = load_config()
    main(
        poke_api_config=config.poke_api,
        image_repository=GetImageRepositoryImpl(config.poke_api),
    )
