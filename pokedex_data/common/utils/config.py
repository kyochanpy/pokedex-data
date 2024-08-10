import json
from ..models.config import Config


def load_config() -> Config:
    config_dict = json.load(open("settings/local.json"))
    return Config.model_validate(config_dict)
