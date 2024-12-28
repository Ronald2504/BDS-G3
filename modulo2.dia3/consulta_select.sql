-- Active: 1735007931138@@127.0.0.1@3306@datag3
-- SELECT
SELECT * from empleado;
SELECT nombre,pais from empleado;
SELECT * FROM empleado limit 10;
SELECT * FROM empleado ORDER BY nombre;
select * from empleado order by salario desc;
SELECT * FROM empleado where pais = 'Peru';
SELECT * FROM empleado where salario > 5000;
SELECT * FROM empleado WHERE salario > 5000 and pais = 'Peru';