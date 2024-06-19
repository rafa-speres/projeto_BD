---------------------------------------------------
-- Proejto Final - Laboratorio de Bases de Dados --
---------------------------------------------------

-------------------------------------------------------------
-- Scripts DML para Inserção de Registros na Base de Dados --
-------------------------------------------------------------


-- Inserts para testar o trigger "trg_insert_user_automaticamente" e "trg_hash_password". 
-- Ao inserir esses dados em LIDER, automaticamente são inseridos em USERS (trg_insert_user_automaticamente).
-- Ao inserir a senha default definida (admin), ela será codificada em um hash ao ser armazenada no banco (trg_hash_password).
INSERT INTO LIDER VALUES ('123.436.559-76',	'Julio', 'OFICIAL', 'Facilis illo.', 'Illo fugit');
INSERT INTO LIDER VALUES ('444.444.444-44',	'Heitor', 'CIENTISTA', 'Facilis illo.', 'Illo fugit');
COMMIT;

-------------------------------------------------------------------------------------------------------------
-- Inserts para testar os diferentes tipos de usuário/lider na aplicação, cobrindo todas as possibilidades --
-------------------------------------------------------------------------------------------------------------

-- OFICIAL que é Líder de Facção:
INSERT INTO LIDER VALUES ('999.999.999-98', 'John', 'OFICIAL', 'Facilis illo.', 'Illo fugit');
INSERT INTO FACCAO VALUES ('faccao_suprema', '999.999.999-98', 'TOTALITARIA', 86);

-- OFICIAL que NÃO é Líder de Facção:
INSERT INTO LIDER VALUES ('333.444.765-32', 'Zé', 'OFICIAL', 'Maxime tempora.', 'Nisi rem odio');


-- COMANDANTE que é Líder de Facção:
INSERT INTO LIDER VALUES ('333.333.333-32', 'Anakin', 'COMANDANTE', 'Natus a.', 'Nisi rem odio');
INSERT INTO FACCAO VALUES ('Faccao_Liberta', '333.333.333-32', 'PROGRESSITA', 2);

-- COMANDANTE que NÃO é Líder de Facção:
INSERT INTO LIDER VALUES ('555.436.559-76', 'Harry', 'COMANDANTE', 'Facilis illo.', 'Illo fugit');


-- CIENTISTA que é Líder de Facção:
INSERT INTO LIDER VALUES ('987.654.321-10', 'Brown', 'CIENTISTA', 'Ut quam.', 'At eum natus');
INSERT INTO FACCAO VALUES ('Faccao_Futuro', '987.654.321-10', 'PROGRESSITA', 3);

-- CIENTISTA que NÃO é Líder de Facção:
INSERT INTO LIDER VALUES ('198.519.851-23', 'Marty', 'CIENTISTA', 'Ut quam.', 'At eum natus');

COMMIT;

---------------------------------------------------------------
-- Inserts para testar as Funcionalidades do Líder de Facção -- 
---------------------------------------------------------------

INSERT INTO FACCAO VALUES ('Faccao_Claquete', '888.482.444-10', 'PROGRESSITA', 0);
COMMIT;


-- Remover FACCAO de NACAO:
INSERT INTO LIDER VALUES ('555.452.444-10', 'Roger', 'OFICIAL', 'Sit saepe ad.', 'Amet id');
INSERT INTO NACAO VALUES('Sit saepe ad.', 0, 'Totam amet.');
INSERT INTO FACCAO VALUES('Faccao_Caballo', '555.452.444-10', 'PROGRESSITA', 1);
INSERT INTO NACAO_FACCAO VALUES ('Sit saepe ad.', 'Faccao_Caballo');

--------------------------------------------------------
-- Inserts para testar o Relatório do Líder de Facção -- 
--------------------------------------------------------

-- Já haviam sido inseridos:
-- INSERT INTO LIDER VALUES ('999.999.999-98', 'John', 'OFICIAL', 'Facilis illo.', 'Illo fugit');
-- INSERT INTO FACCAO VALUES ('faccao_suprema', '999.999.999-98', 'TOTALITARIA', 86);


 -- Inserindo duas COMUNIDADES com a mesma ESPÉCIE, para demonstrar o agrupamento posteriormente.
INSERT INTO COMUNIDADE VALUES ('Odio cum', 'com_empanada', 49);
INSERT INTO COMUNIDADE VALUES ('Odio cum', 'com_jugo', 21);
INSERT INTO COMUNIDADE VALUES ('Ut nam', 'com_fritas', 29);

INSERT INTO PARTICIPA VALUES ('faccao_suprema', 'Odio cum', 'com_empanada');
INSERT INTO PARTICIPA VALUES ('faccao_suprema', 'Odio cum', 'com_jugo');
INSERT INTO PARTICIPA VALUES ('faccao_suprema', 'Ut nam', 'com_fritas');
COMMIT;

-- Para demonstrar o agrupamento por PLANETA
INSERT INTO PLANETA VALUES ('planeta_papas', 5, 5, NULL);
INSERT INTO PLANETA VALUES ('planeta_burger', 11, 12, NULL);

INSERT INTO HABITACAO VALUES ('planeta_papas', 'Odio cum', 'com_empanada', SYSDATE, NULL);
INSERT INTO HABITACAO VALUES ('planeta_papas', 'Ut nam', 'com_fritas', SYSDATE, NULL);
INSERT INTO HABITACAO VALUES ('planeta_burger', 'Odio cum', 'com_jugo', SYSDATE, NULL);
COMMIT;

-- Para demonstrar o agrupamento por SISTEMA
--INSERT INTO ESTRELA VALUES('GJ 3837', 'Xuange', 'A0sh', 17,076544728138742, -17,435524, -11,802923, 21,870286');
--INSERT INTO ESTRELA VALUES('Gl 771A', 'Alshain', 'G8IVvar', 5,360434578161428, 6,563854, -11,925647, 1,528534');

INSERT INTO ORBITA_PLANETA VALUES('planeta_papas', 'GJ 3837', 20, 30, NULL);
INSERT INTO ORBITA_PLANETA VALUES('planeta_burger', 'Gl 771A', 50, 60, NULL);

INSERT INTO SISTEMA VALUES('GJ 3837', 'Sistema  Andrômeda');
INSERT INTO SISTEMA VALUES('Gl 771A', 'Sistema  Nutri');
COMMIT;


-- Para demonstrar o agrupamento por NACAO
--INSERT INTO NACAO VALUES('Facilis illo.', 2, 'Qui sed ut.'); -- Registro já incluso na carga inicial de dados
INSERT INTO NACAO VALUES('nacao_do_bem', 1, NULL);

INSERT INTO DOMINANCIA VALUES('planeta_papas', 'nacao_do_bem', SYSDATE, NULL);
INSERT INTO DOMINANCIA VALUES('planeta_burger', 'Facilis illo.', SYSDATE, NULL);
COMMIT;


------------------------------------------------
-- Inserts para testar o Relatório do Oficial -- 
------------------------------------------------

INSERT INTO COMUNIDADE VALUES ('Amet id', 'com_ramon', 100);
INSERT INTO COMUNIDADE VALUES ('In dicta', 'com_queso', 50);

INSERT INTO PLANETA VALUES ('planeta_pastel', 66, 42, 'Planeta quente');

INSERT INTO HABITACAO VALUES ('planeta_burger', 'Amet id', 'com_ramon', TO_DATE(
    'May 21, 2020, 09:00 A.M.',
    'Month dd, YYYY, HH:MI A.M.',
     'NLS_DATE_LANGUAGE = American'), SYSDATE);   
INSERT INTO HABITACAO VALUES ('planeta_pastel', 'In dicta', 'com_queso', TO_DATE(
    'January 22, 2017, 09:00 A.M.',
    'Month dd, YYYY, HH:MI A.M.',
     'NLS_DATE_LANGUAGE = American'), TO_DATE(
    'May 4, 2023, 11:00 A.M.',
    'Month dd, YYYY, HH:MI A.M.',
     'NLS_DATE_LANGUAGE = American'));

INSERT INTO PARTICIPA VALUES ('faccao_suprema', 'Amet id', 'com_ramon');

INSERT INTO DOMINANCIA VALUES ('planeta_pastel', 'Facilis illo.', TO_DATE(
    'January 22, 2017, 09:00 A.M.',
    'Month dd, YYYY, HH:MI A.M.',
     'NLS_DATE_LANGUAGE = American'), NULL);

INSERT INTO ESTRELA VALUES ('EAD567', 'estrela_animada', 'Gigante Vermelha', 789, -45, 35, 17);

INSERT INTO ORBITA_PLANETA VALUES ('planeta_pastel', 'EAD567', 55, 88, NULL);

INSERT INTO SISTEMA VALUES('EAD567', 'Sistema_Oil');

COMMIT;