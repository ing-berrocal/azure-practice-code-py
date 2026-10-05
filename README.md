Codigo de practica para conectar recurosos azure python

# enviorement

- uv init
- uv sync
- uv add azure-storage-blob azure-identity

- set PATH=%PATH%;D:\Programas\azure-cli-2.85.0-x64\bin
- az login --use-device-code

# Azure

- Storage
    - Blobs

## Cargar un Block Blob con SAS

Configura estas variables en el archivo `.env` de la raiz del proyecto:

```dotenv
AZURE_STORAGE_ACCOUNT_URL=https://<cuenta>.blob.core.windows.net
AZURE_STORAGE_SAS_TOKEN="<token SAS>"
AZURE_STORAGE_CONTAINER_NAME=<contenedor>
AZURE_STORAGE_FILE_PATH="D:/archivos/documento.pdf"
```

La URL de la cuenta no debe incluir el token SAS. El contenedor debe existir
y el SAS debe permitir la escritura (`w`). La ruta puede ser absoluta o relativa
al directorio desde el que ejecutas el comando; en Windows usa `/` en la ruta.

Ejecuta desde la raiz del proyecto:

```sh
uv run python storage/02-upload-block-blob-sas.py
```

El blob usa el nombre del archivo local y no sobrescribe un blob existente.