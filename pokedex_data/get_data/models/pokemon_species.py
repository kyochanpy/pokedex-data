from typing import Sequence
from pydantic import BaseModel


class LanguageJson(BaseModel):
    name: str
    url: str


class NameJson(BaseModel):
    language: LanguageJson
    name: str


class NamesJson(BaseModel):
    names: Sequence[NameJson]

    def get_name(self) -> str:
        for name in self.names:
            if name.language.name == "ja":
                return name.name
        raise Exception("日本語対応していません。")


class GenusJson(BaseModel):
    language: LanguageJson
    genus: str


class GeneraJson(BaseModel):
    genera: Sequence[GenusJson]

    def get_genus(self) -> str:
        for genus in self.genera:
            if genus.language.name == "ja":
                return genus.genus
        raise Exception("日本語対応していません。")


class VersionJson(BaseModel):
    name: str
    url: str


class FlavorTextJson(BaseModel):
    flavor_text: str
    language: LanguageJson
    version: VersionJson


class FlavorTextsJson(BaseModel):
    flavor_text_entries: Sequence[FlavorTextJson]

    def get_flavor_text(self, soft: str) -> str:
        for flavor_text in self.flavor_text_entries:
            if flavor_text.language.name == "ja" and flavor_text.version.name == soft:
                return flavor_text.flavor_text
        raise Exception(
            "日本語対応していない、もしくは指定したソフトのバージョンが存在しません・"
        )


class PokemonSpecies(BaseModel):
    name: str
    genus: str
    flavor_text: str
