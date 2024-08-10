import requests
from pokedex_data.common.models.config import PokeApiConfig
from pokedex_data.get_image.interface import GetImageRepository


class GetImageRepositoryImpl(GetImageRepository):
    def __init__(self, poke_api_config: PokeApiConfig):
        self._poke_api_config = poke_api_config

    def _get_image(self, url: str) -> bytes:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("画像の取得に失敗しました。")
        return response.content

    def get_image(self, name: str) -> tuple[bytes, bytes]:
        response = requests.get(f"{self._poke_api_config.endpoint}/pokemon/{name}")
        if response.status_code != 200:
            raise Exception("画像の取得に失敗しました。")
        image_urls_json = response.json()["sprites"]
        image_url = image_urls_json["other"]["official-artwork"]["front_default"]
        dot_image_url = image_urls_json["front_default"]
        return self._get_image(image_url), self._get_image(dot_image_url)
