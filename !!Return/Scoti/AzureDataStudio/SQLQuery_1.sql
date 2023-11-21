-- Ver todas las filas
SELECT COUNT(*) as TotalFilas
FROM dbo.JK_workersColab;

-- Ver las filas de los procesados 0
SELECT COUNT(*) as TotalFilas
FROM dbo.JK_workersColab
WHERE Procesado = 0;


SELECT *
FROM JK_workersColab
WHERE DNI = '99999997';

SELECT TOP 1 DNI FROM JK_workersColab WHERE Procesado = 0

SELECT TOP 1 DNI 
FROM JK_workersColab 
WHERE Procesado = 0 
ORDER BY NEWID();


SELECT TOP 100 * 
FROM JK_workersColab 
WHERE Procesado = 1


UPDATE JK_workersColab SET FechaTrabajo = '2023-09-29' WHERE DNI = 07546930   

EXEC dbo.InsertOrUpdateWorker '08231595', 2, '', N'calar de nuevo', '';


SELECT TOP 10000 * FROM JK_workersColab
ORDER BY FechaTrabajo DESC 


SELECT TOP 10 
    DNI, 
    Status, 
    CONVERT(datetimeoffset, FechaTrabajo AT TIME ZONE 'UTC' AT TIME ZONE 'Eastern Standard Time') as FechaTrabajo_UTC5
FROM JK_workersColab
WHERE Status LIKE '%LIVE%'
ORDER BY FechaTrabajo DESC;





-- Buscar el la lista de 0
SELECT TOP 100 DNI
FROM JK_workersColab
WHERE Procesado = 0;


/*
CREATE PROCEDURE dbo.InsertOrUpdateWorker
    @DNI VARCHAR(8),
    @Procesado INT,
    @FechaTrabajo DATETIME,
    @Status NVARCHAR(200),
    @IpCliente NVARCHAR(20)
AS
BEGIN
    IF EXISTS (SELECT 1 FROM [dbo].[JK_workersColab] WHERE [DNI] = @DNI)
    BEGIN
        -- Actualizar el registro si ya existe
        UPDATE [dbo].[JK_workersColab]
        SET [Procesado] = @Procesado,
            [FechaTrabajo] = @FechaTrabajo,
            [Status] = @Status,
            [IpCliente] = @IpCliente
        WHERE [DNI] = @DNI;
    END
    ELSE
    BEGIN
        -- Insertar un nuevo registro si no existe
        INSERT INTO [dbo].[JK_workersColab] ([DNI], [Procesado], [FechaTrabajo], [Status], [IpCliente])
        VALUES (@DNI, @Procesado, @FechaTrabajo, @Status, @IpCliente);
    END
END;


CREATE PROCEDURE GetRandomDNI
AS
BEGIN
    WITH SampleRows AS (
        SELECT TOP 100 DNI 
        FROM JK_workersColab 
        WHERE Procesado = 0 
        ORDER BY NEWID()
    )
    SELECT TOP 1 DNI
    FROM SampleRows
    ORDER BY NEWID();
END;

*/

select * from JK_EstadoProcesado


INSERT INTO JK_EstadoProcesado (Valor, Descripcion)
VALUES (99, 'test');


------------------------
-- desactivar el duup key

-- Elimina el índice actual si existe
IF EXISTS (SELECT * FROM sys.indexes WHERE object_id = OBJECT_ID(N'[dbo].[JK_workersColab]') AND name = N'IX_ID')
DROP INDEX IX_ID ON [dbo].[JK_workersColab];
GO

-- Crea el índice nuevamente sin la opción IGNORE_DUP_KEY
CREATE UNIQUE NONCLUSTERED INDEX IX_ID
ON [dbo].[JK_workersColab]([DNI] ASC);
GO

------------- este es para activar nuevamente  


-- Elimina el índice actual si existe
IF EXISTS (SELECT * FROM sys.indexes WHERE object_id = OBJECT_ID(N'[dbo].[JK_workersColab]') AND name = N'IX_ID')
DROP INDEX IX_ID ON [dbo].[JK_workersColab];
GO

-- Crea el índice con la opción IGNORE_DUP_KEY activada
CREATE UNIQUE NONCLUSTERED INDEX IX_ID
ON [dbo].[JK_workersColab]([DNI] ASC) WITH (IGNORE_DUP_KEY = ON);
GO
