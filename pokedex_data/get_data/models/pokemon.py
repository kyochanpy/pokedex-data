from typing import Literal, Sequence
from pydantic import BaseModel


class Stats(BaseModel):
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


class StatJson(BaseModel):
    name: Literal[
        "hp", "attack", "defense", "special-attack", "special-defense", "speed"
    ]
    url: str


class BaseStatJson(BaseModel):
    base_stat: int
    effort: int
    stat: StatJson


class StatsJson(BaseModel):
    stats: Sequence[BaseStatJson]

    def parse(self) -> Stats:
        for stat in self.stats:
            value = stat.base_stat
            match stat.stat.name:
                case "hp":
                    hp = value
                case "attack":
                    attack = value
                case "defense":
                    defense = value
                case "special-attack":
                    special_attack = value
                case "special-defense":
                    special_defense = value
                case "speed":
                    speed = value
        return Stats(
            hp=hp,
            attack=attack,
            defense=defense,
            special_attack=special_attack,
            special_defense=special_defense,
            speed=speed,
        )


class Types(BaseModel):
    type_1: str
    type_2: str | None


class TypeJson(BaseModel):
    name: str
    url: str


class SlotJson(BaseModel):
    slot: int
    type: TypeJson


class TypesJson(BaseModel):
    types: Sequence[SlotJson]

    def parse(self) -> Types:
        if len(self.types) == 1:
            return Types(type_1=self.types[0].type.name, type_2=None)
        return Types(type_1=self.types[0].type.name, type_2=self.types[1].type.name)


class Pokemon(BaseModel):
    order: int
    stats: Stats
    types: Types
    weight: int
    height: int
