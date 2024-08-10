from pydantic import BaseModel, Field


class PokeApiConfig(BaseModel):
    generation: int = Field(default=1)
    endpoint: str


class Config(BaseModel):
    poke_api: PokeApiConfig
