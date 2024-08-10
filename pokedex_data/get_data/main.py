from pokedex_data.common.models.config import PokeApiConfig
from pokedex_data.common.utils.pokemon import get_pokemon_names_by_generation
from pokedex_data.get_data.interfaces import PokemonRepository, PokemonSpeciesRepository
import polars as pl


def main(
    *,
    poke_api_config: PokeApiConfig,
    pokemon_repository: PokemonRepository,
    pokemon_species_repository: PokemonSpeciesRepository,
) -> None:
    pokemon_names = get_pokemon_names_by_generation(poke_api_config.generation)

    order_list = list[int] = []
    name_list: list[str] = []
    genus_list: list[str] = []
    weight_list: list[int] = []
    height_list: list[int] = []
    type_1_list: list[str] = []
    type_2_list: list[str | None] = []
    hp_list: list[int] = []
    attack_list: list[int] = []
    defense_list: list[int] = []
    special_attack_list: list[int] = []
    special_defense_list: list[int] = []
    speed_list: list[int] = []
    flavor_text_list: list[str] = []
    for pokemon_name in pokemon_names:
        pokemon = pokemon_repository.get_pokemon(pokemon_name)
        pokemon_species = pokemon_species_repository.get_pokemon_species(pokemon_name)
        order_list.append(pokemon.order)
        name_list.append(pokemon_name)
        genus_list.append(pokemon_species.genus)
        weight_list.append(pokemon.weight)
        height_list.append(pokemon.height)
        type_1_list.append(pokemon.types.type_1)
        type_2_list.append(pokemon.types.type_2)
        hp_list.append(pokemon.stats.hp)
        attack_list.append(pokemon.stats.attack)
        defense_list.append(pokemon.stats.defense)
        special_attack_list.append(pokemon.stats.special_attack)
        special_defense_list.append(pokemon.stats.special_defense)
        speed_list.append(pokemon.stats.speed)
        flavor_text_list.append(pokemon_species.flavor_text)

    df = pl.DataFrame(
        {
            "order": order_list,
            "name": name_list,
            "genus": genus_list,
            "weight": weight_list,
            "height": height_list,
            "type_1": type_1_list,
            "type_2": type_2_list,
            "hp": hp_list,
            "attack": attack_list,
            "defense": defense_list,
            "special_attack": special_attack_list,
            "special_defense": special_defense_list,
            "speed": speed_list,
            "flavor_text": flavor_text_list,
        }
    )
    df.write_csv("pokemon.csv")
