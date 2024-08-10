from pokedex_data.common.utils.config import load_config
from pokedex_data.get_data.main import main
from pokedex_data.get_data.repositories.pokemon import PokemonRepositoryImpl
from pokedex_data.get_data.repositories.pokemon_species import (
    PokemonSpeciesRepositoryImpl,
)


if __name__ == "__main__":
    config = load_config()
    main(
        poke_api_config=config.poke_api,
        pokemon_repository=PokemonRepositoryImpl(config.poke_api),
        pokemon_species_repository=PokemonSpeciesRepositoryImpl(config.poke_api),
    )
