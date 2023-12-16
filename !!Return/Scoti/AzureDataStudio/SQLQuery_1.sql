-- Ver todas las filas
SELECT COUNT(*) as TotalFilas
FROM dbo.JK_workersColab;

-- Ver las filas de los procesados 0
SELECT COUNT(*) as TotalFilas
FROM dbo.JK_workersColab
WHERE Procesado = 0;


SELECT *
FROM DataReC
WHERE DNI = '45495550';

SELECT *
FROM JK_workersColab
WHERE DNI = '07799205';



EXECUTE ObtenerDNIPorProcesado 28


SELECT TOP 1 DNI FROM JK_workersColab WHERE Procesado = 0

SELECT TOP 1 DNI 
FROM JK_workersColab 
WHERE Procesado = 0 
ORDER BY NEWID();


SELECT TOP 100000 * 
FROM JK_workersColab 
WHERE Procesado = 101

SELECT TOP 1000 * 
FROM JK_workersColab 
WHERE Status = 'ERROR AL OBTENER DATOS DEL DNI'


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
VALUES (101, 'data history escolta');



ALTER PROCEDURE spGetEstadoProcesadoCount 
AS 
BEGIN
    SELECT EP.Valor, 
           EP.Descripcion, 
           ISNULL(COUNT(WC.Procesado), 0) as TotalFilas
    FROM dbo.JK_EstadoProcesado EP
    LEFT JOIN dbo.JK_workersColab WC 
           ON EP.Valor = WC.Procesado AND WC.Procesado BETWEEN 0 AND 200
    GROUP BY EP.Valor, EP.Descripcion
    ORDER BY EP.Valor;
END;
