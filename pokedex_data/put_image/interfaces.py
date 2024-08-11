from abc import ABC, abstractmethod


class CreateBucketRepository(ABC):
    @abstractmethod
    def create_bucket(self, bucket_name: str) -> None: ...
