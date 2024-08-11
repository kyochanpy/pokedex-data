from abc import ABC, abstractmethod


class CreateBucketRepository(ABC):
    @abstractmethod
    def create_bucket(self, bucket_name: str) -> None: ...


class PutImageRepository(ABC):
    @abstractmethod
    def put_image(self, bucket_name: str, image_path: str, image: bytes) -> None: ...
