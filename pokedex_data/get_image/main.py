import time
from tqdm import tqdm
from pokedex_data.common.models.config import PokeApiConfig
from pokedex_data.common.utils.pokemon import get_pokemon_names_by_generation
from pokedex_data.get_image.interface import GetImageRepository


def main(
    *, poke_api_config: PokeApiConfig, image_repository: GetImageRepository
) -> None:
    pokemon_names = get_pokemon_names_by_generation(poke_api_config.generation)

    for pokemon_name in tqdm(pokemon_names):
        image, dot_image = image_repository.get_image(pokemon_name)
        with open(f"images/{pokemon_name}.png", "wb") as f:
            f.write(image)
        with open(f"images/{pokemon_name}_dot.png", "wb") as f:
            f.write(dot_image)
        time.sleep(5)
