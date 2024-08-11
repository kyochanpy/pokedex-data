from pydantic import BaseModel, Field


class PokeApiConfig(BaseModel):
    generation: int = Field(default=1)
    endpoint: str


class SupaBaseConfig(BaseModel):
    url: str
    key: str


class Config(BaseModel):
    poke_api: PokeApiConfig
    supabase: SupaBaseConfig
