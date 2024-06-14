---------------------------------------------------
-- Proejto Final - Laboratorio de Bases de Dados --
---------------------------------------------------

-------------------------------------------------------------
-- Scripts DML para Inser��o de Registros na Base de Dados --
-------------------------------------------------------------


-- Inserts para testar o trigger "trg_insert_user_automaticamente" e "trg_hash_password". 
-- Ao inserir esses dados em LIDER, automaticamente s�o inseridos em USERS (trg_insert_user_automaticamente).
-- Ao inserir a senha default definida (admin), ela ser� codificada em um hash ao ser armazenada no banco (trg_hash_password).
INSERT INTO LIDER VALUES ('123.436.559-76',	'Julio', 'OFICIAL', 'Facilis illo.', 'Illo fugit');
INSERT INTO LIDER VALUES ('444.444.444-44',	'Heitor', 'CIENTISTA', 'Facilis illo.', 'Illo fugit');
COMMIT;

-------------------------------------------------------------------------------------------------------------
-- Inserts para testar os diferentes tipos de usu�rio/lider na aplica��o, cobrindo todas as possibilidades --
-------------------------------------------------------------------------------------------------------------

-- OFICIAL que � L�der de Fac��o:
INSERT INTO LIDER VALUES ('999.999.999-98', 'John', 'OFICIAL', 'Facilis illo.', 'Illo fugit');
INSERT INTO FACCAO VALUES ('faccao_suprema', '999.999.999-98', 'TOTALITARIA', 86);

-- OFICIAL que N�O � L�der de Fac��o:
INSERT INTO LIDER VALUES ('333.444.765-32', 'Z�', 'OFICIAL', 'Maxime tempora.', 'Nisi rem odio');


-- COMANDANTE que � L�der de Fac��o:
INSERT INTO LIDER VALUES ('333.333.333-32', 'Anakin', 'COMANDANTE', 'Natus a.', 'Nisi rem odio');
INSERT INTO FACCAO VALUES ('Faccao_Liberta', '333.333.333-32', 'PROGRESSITA', 2);

-- COMANDANTE que N�O � L�der de Fac��o:
INSERT INTO LIDER VALUES ('555.436.559-76', 'Harry', 'COMANDANTE', 'Facilis illo.', 'Illo fugit');


-- CIENTISTA que � L�der de Fac��o:
INSERT INTO LIDER VALUES ('987.654.321-10', 'Brown', 'CIENTISTA', 'Ut quam.', 'At eum natus');
INSERT INTO FACCAO VALUES ('Faccao_Futuro', '987.654.321-10', 'PROGRESSITA', 3);

-- CIENTISTA que N�O � L�der de Fac��o:
INSERT INTO LIDER VALUES ('198.519.851-23', 'Marty', 'CIENTISTA', 'Ut quam.', 'At eum natus');

COMMIT;

