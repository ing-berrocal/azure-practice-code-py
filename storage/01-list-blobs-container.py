# List all blobs in an Azure Storage container using Python
# This script connects to an Azure Storage account using the provided connection string,
# retrieves the specified container, and lists all blobs within that container.
# connection_string and container_name get from .env file
from dotenv import load_dotenv
import os

load_dotenv()
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

from azure.storage.blob import BlobServiceClient

# Replace with your connection string and container name
# connection_string = "your_connection_string"
# container_name = "your_container_name"

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string,sas_token=os.getenv("AZURE_STORAGE_SAS_TOKEN"))
#blob_service_client = BlobServiceClient.from_connection_string(connection_string,credential=AzureSasCredential(os.getenv("AZURE_STORAGE_SAS_TOKEN")))

# se necesita token de servicio
for container in blob_service_client.list_containers():
    print(container.name)

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# List all blobs in the container
blob_list = container_client.list_blobs()
for blob in blob_list:
    print(blob.name)