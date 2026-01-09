CREATE TABLE animal(
	id INT PRIMARY KEY AUTO_INCREMENT,
    raca VARCHAR(50),
    nome VARCHAR(50),
    sexo VARCHAR(1),
    idade INT,
    porte VARCHAR(1),
    temperamento VARCHAR(50),
    `status` VARCHAR(30)
);

CREATE TABLE cachorro(
	id_animal INT PRIMARY KEY,
    necessidade_passeio BOOLEAN NOT NULL,
    independencia BOOLEAN NOT NULL,
    CONSTRAINT FOREIGN KEY (id_animal) REFERENCES animal(id)
);

CREATE TABLE gato(
	id_animal INT PRIMARY KEY,
    necessidade_passeio BOOLEAN NOT NULL,
    independencia BOOLEAN NOT NULL,
    CONSTRAINT FOREIGN KEY (id_animal) REFERENCES animal(id)
);