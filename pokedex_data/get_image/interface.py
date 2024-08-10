from abc import ABC, abstractmethod


class GetImageRepository(ABC):
    @abstractmethod
    def get_image(self, name: str) -> tuple[bytes, bytes]: ...
