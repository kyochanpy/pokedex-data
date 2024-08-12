import os
from pokedex_data.put_image.interfaces import CreateBucketRepository, PutImageRepository


def main(
    *,
    create_bucket_repository: CreateBucketRepository,
    put_image_repository: PutImageRepository,
) -> None:
    # create_bucket_repository.create_bucket("images")

    image_files = os.listdir("data/image/normal")
    for image_file in image_files:
        with open(f"data/image/normal/{image_file}", "rb") as f:
            put_image_repository.put_image("images", f"normal/{image_file}", f.read())
        with open(f"data/image/dot/{image_file}", "rb") as f:
            put_image_repository.put_image("images", f"dot/{image_file}", f.read())
