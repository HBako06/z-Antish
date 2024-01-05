CREATE TABLE personas (
    dni VARCHAR(10),
    ap_pat VARCHAR(255),
    ap_mat VARCHAR(255),
    nombres VARCHAR(255),
    fecha_nac VARCHAR(255),
    fch_inscripcion VARCHAR(255),
    fch_emision VARCHAR(255),
    fch_caducidad VARCHAR(255),
    ubigeo_nac VARCHAR(255),
    ubigeo_dir VARCHAR(255),
    direccion VARCHAR(255),
    sexo VARCHAR(255),
    est_civil VARCHAR(255),
    dig_ruc VARCHAR(255),
    madre VARCHAR(255),
    padre VARCHAR(255)
);

ALTER TABLE personas ADD PRIMARY KEY (dni);

-- agregando colum nueva
ALTER TABLE personas ADD COLUMN nombre_completo VARCHAR(765);

UPDATE personas
SET nombre_completo = COALESCE(ap_pat, '') || ' ' || COALESCE(ap_mat, '') || ' ' || COALESCE(nombres, '');


SELECT dni,fecha_nac,nombres,ap_pat,ap_mat FROM personas
WHERE nombre_completo LIKE UPPER('%callupe paliza elmer luis%');

-- extra para buscar random
select * from personas

SELECT *
FROM personas
WHERE DNI = '76192275';

SELECT COUNT(*) as TotalFilas
FROM personas;

delete from personas

CREATE EXTENSION aws_commons;
CREATE EXTENSION aws_s3;
SELECT * FROM pg_extension;

UPDATE personas SET dni = LPAD(dni, 8, '0');


-- este funciona
psql -h database-1-instance-1.c8dbue4rjz1y.us-east-2.rds.amazonaws.com -U postgres -d postgres -c "\COPY personas FROM 'E:\\Respaldo\\carpetas\\Tareas\\reniec\\datatest.csv' WITH (FORMAT csv, HEADER, ENCODING 'ISO-8859-1')"

psql -h database-1-instance-1.c8dbue4rjz1y.us-east-2.rds.amazonaws.com -U postgres -d postgres -c "\COPY personas FROM 'E:\\Respaldo\\carpetas\\Tareas\\reniec\\archivos_salida2\\archivo_1.csv' WITH (FORMAT csv, HEADER, ENCODING 'ISO-8859-1')"
psql -h database-1-instance-1.c8dbue4rjz1y.us-east-2.rds.amazonaws.com -U postgres -d postgres -c "\COPY personas FROM 'E:\\Respaldo\\carpetas\\Tareas\\reniec\\archivos_salida2\\archivo_2.csv' WITH (FORMAT csv, ENCODING 'ISO-8859-1')"
psql -h database-1-instance-1.c8dbue4rjz1y.us-east-2.rds.amazonaws.com -U postgres -d postgres -c "\COPY personas FROM 'E:\\Respaldo\\carpetas\\Tareas\\reniec\\archivos_salida2\\archivo_3.csv' WITH (FORMAT csv, ENCODING 'ISO-8859-1')"



CREATE INDEX idx_nombre_completo ON personas (nombre_completo);
