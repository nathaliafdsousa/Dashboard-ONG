CREATE TABLE doacoes (
    id SERIAL PRIMARY KEY,
    data_doacao DATE NOT NULL,
    tipo_doacao VARCHAR(50) NOT NULL,
    quantidade  FLOAT NOT NULL,
    descricao TEXT
);

INSERT INTO doacoes (id, data_doacao, tipo_doacao, quantidade, descricao) 
VALUES
(1, "2025-01-25", "alimentos", 100, "80 sacos de 15kg de ração de cachorro e 20 sacos de 10kg de ração de gato"),
(2, "2025-01-31", "limpeza", 20, "20 kits de limpeza"),
(3, "2025-02-08", "financeira", 8000.90,"Reais"),
(4, "2025-02-26", "financeira", 1345.77,"Reais"),
(5, "2025-03-06", "alimentos", 300, "100 sacos de 15kg de ração de cachorro e 200 sacos de 10kg de ração de gato"),
(6, "2025-02-08", "limpeza", 5,"5 kits de limpeza");