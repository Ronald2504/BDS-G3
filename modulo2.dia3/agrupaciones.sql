-- Active: 1735007931138@@127.0.0.1@3306@datag3
-- Active: 1735007931138@@127.0.0.1@3306@sakila
-- funciones de agrupacion
-- 1. contar
SELECT COUNT(*) from empleado;
SELECT COUNT(*) from empleado where salario > 5000;

--2.Maximo y minimo
SELECT MAX(salario), MIN(salario), AVG(salario) from empleado;
SELECT DISTINCT PAIS FROM empleado;
SELECT pais,COUNT(*) FROM empleado
GROUP BY pais
ORDER BY COUNT(*) DESC;
--FILTRA LOS DATOS ANTES DE HACER LA EJECUCION DE LA SENTENCIA
SELECT pais,area, MAX(salario), MIN(salario), AVG(salario) from empleado
WHERE salario > 5000
GROUP BY pais,area;
-- FILTRA LOS RESULTADOS DESPUES DE SACAR EL AVG
SELECT pais, AVG(salario) from empleado
GROUP BY pais
HAVING AVG(salario) > 4000;
-- SUBCONSULTAS
SELECT * FROM empleado 
WHERE salario > (SELECT AVG(salario) from empleado);
-- COUNT ES NECESARIO QUE VAYA CON GROUP BY
select pais, COUNT(*), (SELECT AVG(salario) from empleado) as salario_promedio from empleado
WHERE salario > (SELECT AVG (salario) from empleado)
GROUP BY pais ORDER BY COUNT(*) desc;