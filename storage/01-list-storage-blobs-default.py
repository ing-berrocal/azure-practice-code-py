# List all blobs in an Azure Storage container using Python
# This script connects to an Azure Storage account using the provided connection string,
# retrieves the specified container, and lists all blobs within that container.
# connection_string and container_name get from .env file
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()
account_url = os.getenv("AZURE_STORAGE_ACCOUNT_URL")
container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient(account_url, credential=DefaultAzureCredential())

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# List all blobs in the container
blob_list = container_client.list_blobs()
for blob in blob_list:
    print(blob.name)