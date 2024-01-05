CREATE DATABASE SCOPED CREDENTIAL blobcredentialas1
WITH IDENTITY = 'user',
SECRET = 'sp=racwdyti&st=2024-01-05T19:46:17Z&se=2025-01-06T03:46:17Z&spr=https&sv=2022-11-02&sr=b&sig=minyoBkhCpURkY66sWaF99v%2FhqxLV5Bu%2FEp8%2BJOCyx0%3D'; -- Reemplaza con tu token SAS generado

-- Crea el External Data Source para acceso anónimo
CREATE EXTERNAL DATA SOURCE BlobStorageDataSource
WITH (
    TYPE = BLOB_STORAGE,
    LOCATION = 'https://comunal.blob.core.windows.net/inputs',
    CREDENTIAL = 'blobcredentialas1'
);

-- Carga datos desde el archivo CSV en la tabla temporal
BULK INSERT [dbo].[JK_workersColab]
FROM 'dataDn18.csv'
WITH (
    DATA_SOURCE = 'BlobStorageDataSource',
    FIELDTERMINATOR = ',',    -- Delimitador de campos: coma
    FIRSTROW = 2,
    MAXERRORS = 50,
    --IGNORE_DUP_KEY = ON,      -- Omitir filas duplicadas
    KEEPNULLS                 -- Mantener los valores NULL en las filas duplicadas
);


CREATE UNIQUE INDEX IX_ID ON dbo.JK_workersColab(ID) WITH (IGNORE_DUP_KEY = ON);


-- Buscar DNI de mi base de datos calados
SELECT *
FROM JK_workersColab
WHERE DNI = '47509971';




-- Verificar si la credencial existe y eliminarla si es necesario
IF EXISTS (SELECT * FROM sys.database_scoped_credentials WHERE name = 'blobcredentialas')
BEGIN
    DROP DATABASE SCOPED CREDENTIAL blobcredentialas;
END

-- Verificar si el External Data Source existe y eliminarlo si es necesario
IF EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'bloddatsource')
BEGIN
    DROP EXTERNAL DATA SOURCE bloddatsource;
END
