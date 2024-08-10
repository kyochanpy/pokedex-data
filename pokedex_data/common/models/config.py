from pydantic import BaseModel


class PokeApiConfig(BaseModel):
    generation: int
    endpoint: str


class Config(BaseModel):
    poke_api: PokeApiConfig
