CREATE USER MiNuevoUsuario WITH PASSWORD = 'Jackelino123';
GO


-- Otorgar permisos de SELECT, INSERT, UPDATE, DELETE
GRANT SELECT, INSERT, UPDATE, DELETE ON OBJECT::dbo.JK_workersColab TO MiNuevoUsuario;
GO