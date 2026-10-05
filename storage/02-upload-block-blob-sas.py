import os
from pathlib import Path

from azure.storage.blob import BlobServiceClient, BlobType
from dotenv import load_dotenv


def main():
    load_dotenv()
    required_variables = (
        "AZURE_STORAGE_ACCOUNT_URL",
        "AZURE_STORAGE_SAS_TOKEN",
        "AZURE_STORAGE_CONTAINER_NAME",
        "AZURE_STORAGE_FILE_PATH",
    )
    missing_variables = [name for name in required_variables if not os.getenv(name)]
    if missing_variables:
        raise ValueError(f"Faltan variables en .env: {', '.join(missing_variables)}")

    file_path = Path(os.environ["AZURE_STORAGE_FILE_PATH"])
    if not file_path.is_file():
        raise FileNotFoundError(f"No existe el archivo: {file_path}")

    with BlobServiceClient(
        account_url=os.environ["AZURE_STORAGE_SAS_TOKEN"]
    ) as blob_service_client:
        blob_client = blob_service_client.get_blob_client(
            container=os.environ["AZURE_STORAGE_CONTAINER_NAME"],
            blob=file_path.name,
        )
        with file_path.open("rb") as data:
            blob_client.upload_blob(data, blob_type=BlobType.BLOCKBLOB, overwrite=False)

    print(f"Block Blob cargado: {file_path.name}")


if __name__ == "__main__":
    main()