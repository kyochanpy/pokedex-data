from pokedex_data.common.utils.config import load_config
from pokedex_data.insert_data.main import main
from pokedex_data.insert_data.repositories.pokemon_type import (
    InsertPokemonTypeReositoryImpl,
)
from pokedex_data.insert_data.repositories.pokemons import InsertPokemonsReositoryImpl
from pokedex_data.insert_data.repositories.types import InsertTypesReositoryImpl


if __name__ == "__main__":
    config = load_config()
    main(
        config=config,
        insert_pokemons_repository=InsertPokemonsReositoryImpl(config.supabase),
        insert_types_repository=InsertTypesReositoryImpl(config.supabase),
        insert_pokemon_type_repository=InsertPokemonTypeReositoryImpl(config.supabase),
    )
