
CREATE TABLE empresa (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE ciudad (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE direcciones (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    empresa_id INT NOT NULL,
    ciudad_id INT NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    FOREIGN KEY (empresa_id) REFERENCES empresa(id),
    FOREIGN KEY (ciudad_id) REFERENCES ciudad(id)
);
INSERT INTO empresa (nombre)
VALUES
('MADEX SAC'),
('ESCRITORIOS SAC');
INSERT INTO ciudad (nombre)
VALUES
('Arequipa'),
('Lima'),
('Cusco');
INSERT INTO direcciones (empresa_id, ciudad_id, direccion)
VALUES
(1, 1, 'Av. requipa g8'), 
(1, 1, 'Av. dolores 458'), 
(2, 2, 'Av. atlanta 1'),    
(2, 3, 'Calle mercaderes g7');   