from pydantic import BaseModel


class PokeApiConfig(BaseModel):
    endpoint: str


class Config(BaseModel):
    poke_api: PokeApiConfig
