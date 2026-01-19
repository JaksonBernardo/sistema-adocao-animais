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

CREATE TABLE pessoa(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    idade INT NOT NULL,
    moradia VARCHAR(30) NOT NULL,
    area_util DECIMAL(6, 2) NOT NULL,
    experiencia_pets TINYINT(1),
    tem_crianca TINYINT(1),
    outros_animais TINYINT(1)
);

CREATE TABLE adotante(
	id_pessoa INT NOT NULL,
    renda_mensal DECIMAL(10, 2) NOT NULL,
    CONSTRAINT FOREIGN KEY (id_pessoa) REFERENCES pessoa(id)
);

CREATE TABLE vacinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_animal INT NOT NULL,
    nome_vacina VARCHAR(50) NOT NULL,
    data_aplicacao DATE,
    CONSTRAINT fk_vacinas_animal FOREIGN KEY (id_animal) REFERENCES animal(id) ON DELETE CASCADE
);

CREATE TABLE adestramento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_animal INT NOT NULL,
    comando_aprendido VARCHAR(50) NOT NULL,
    data_aprendizado DATE DEFAULT (CURRENT_DATE), 
    CONSTRAINT fk_adestramento_animal FOREIGN KEY (id_animal) REFERENCES animal(id) ON DELETE CASCADE
);