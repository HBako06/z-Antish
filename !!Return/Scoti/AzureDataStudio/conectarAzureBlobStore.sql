-- Crear la credencial con el token SAS
CREATE DATABASE SCOPED CREDENTIAL BlobStorageCredential2
WITH IDENTITY = 'user',
SECRET = 'sp=racwdli&st=2023-10-28T05:24:36Z&se=2025-10-28T13:24:36Z&spr=https&sv=2022-11-02&sr=c&sig=8pA3CkH1iKJSzXSlVpsJQhsD7rCr%2FZajktRrKVq15bs%3D';

-- Crear el External Data Source utilizando la credencial
CREATE EXTERNAL DATA SOURCE BlobStorageDataSource
WITH (
    TYPE = BLOB_STORAGE,
    LOCATION = 'https://comunal.blob.core.windows.net/inputs',
    CREDENTIAL = BlobStorageCredential2
);

-- Cargar datos desde el archivo CSV a la tabla temporal
BULK INSERT [dbo].[JK_workersColab]
FROM 'dataDn6 lives.csv'
WITH (
    DATA_SOURCE = 'BlobStorageDataSource',
    FIELDTERMINATOR = ',',    -- Delimitador de campos: coma
    FIRSTROW = 2,
    MAXERRORS = 50,
    IGNORE_DUP_KEY = ON,      -- Omitir filas duplicadas
    KEEPNULLS                 -- Mantener los valores NULL en las filas duplicadas
);


CREATE UNIQUE INDEX IX_ID ON dbo.JK_workersColab(ID) WITH (IGNORE_DUP_KEY = ON);


-- Buscar DNI de mi base de datos calados
SELECT *
FROM JK_workersColab
WHERE DNI = '47509971';




-- Verificar si la credencial existe y eliminarla si es necesario
IF EXISTS (SELECT * FROM sys.database_scoped_credentials WHERE name = 'BlobStorageCredential')
BEGIN
    DROP DATABASE SCOPED CREDENTIAL BlobStorageCredential;
END

-- Verificar si el External Data Source existe y eliminarlo si es necesario
IF EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'BlobStorageDataSource')
BEGIN
    DROP EXTERNAL DATA SOURCE BlobStorageDataSource;
END
