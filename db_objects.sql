---------------------------------------------------
-- Proejto Final - Laboratorio de Bases de Dados --
---------------------------------------------------

------------------------------------------------------
-- Scripts para Cria��o de Objetos na Base de Dados --
------------------------------------------------------


-- Criando a tabela "USERS"
CREATE TABLE USERS (
    user_id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    password VARCHAR2(64) NOT NULL,
    id_lider CHAR(14) NOT NULL,
    CONSTRAINT FK_USERS_LIDER FOREIGN KEY (id_lider) REFERENCES LIDER(CPI) ON DELETE CASCADE,
    CONSTRAINT UN_USERS_id_lider UNIQUE (id_lider)
);


-- Trigger para armazenar a senha de um USER utilizando a fun��o MD5 para hash
CREATE OR REPLACE TRIGGER trg_hash_password
BEFORE INSERT OR UPDATE OF password
ON USERS
FOR EACH ROW
DECLARE
    v_hash_password VARCHAR2(64);
BEGIN
    SELECT STANDARD_HASH(:NEW.password, 'MD5') INTO v_hash_password FROM DUAL;
    :NEW.password := v_hash_password;
END;


-- Tabela "LOG_TABLE"
CREATE TABLE LOG_TABLE (
    user_id NUMBER NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    message VARCHAR2(1000),
    CONSTRAINT FK_LOG_TABLE_USERS FOREIGN KEY (user_id) REFERENCES USERS(user_id) ON DELETE CASCADE
);


-- Procedure para encontrar um Lider sem tupla na tabela USERS e inseri-lo com uma senha default (uma esp�cie de carga inicial de USERS)
CREATE OR REPLACE PROCEDURE sp_cadastrar_lider_user AS
BEGIN
    FOR i IN (
        SELECT CPI 
        FROM LIDER
        WHERE CPI NOT IN (SELECT id_lider FROM USERS)
    ) LOOP
        INSERT INTO USERS (Password, id_lider)
        VALUES ('admin', i.CPI);
    END LOOP;
    
    COMMIT;
END;

-- Chamando a Procedure para cadastrar os l�deres j� existentes na base
BEGIN
    sp_cadastrar_lider_user;
END;




-- Trigger para inserir um registro automaticamente na tabela de USERS ap�s uma inser��o em LIDER
CREATE OR REPLACE TRIGGER trg_insert_user_automaticamente
AFTER INSERT ON LIDER
FOR EACH ROW
BEGIN
    INSERT INTO USERS (password, id_lider)
    VALUES ('admin', :NEW.CPI);
END;


-- Trigger para excluir um registro automaticamente na tabela de USERS ap�s uma exclus�o em LIDER
CREATE OR REPLACE TRIGGER trg_delete_user_automaticamente
AFTER DELETE ON LIDER
FOR EACH ROW
BEGIN
    DELETE FROM USERS WHERE id_lider = :OLD.CPI;
END;

-- Inserts para testes do trigger "trg_insert_user_automaticamente"
INSERT INTO LIDER VALUES ('555.436.559-76',	'Harry', 'COMANDANTE', 'Facilis illo.', 'Illo fugit');
INSERT INTO LIDER VALUES ('123.436.559-76',	'Julio', 'OFICIAL', 'Facilis illo.', 'Illo fugit');
INSERT INTO LIDER VALUES ('444.444.444-44',	'Heitor', 'CIENTISTA', 'Facilis illo.', 'Illo fugit');

-- Delete para teste do trigger "trg_delete_user_automaticamente"
--DELETE FROM LIDER WHERE CPI = '555.436.559-76'; --MUTANTE


-- TESTE de fazer SELECT com HASH
SELECT * FROM USERS WHERE ID_LIDER = '123.456.789-10' AND PASSWORD = STANDARD_HASH('admin', 'MD5');






-- relatorio lider faccao

-- View com todas as informa��es necess�rias
--CREATE OR REPLACE VIEW V_COMUNIDADES AS
--SELECT
--    F.NOME AS FACCAO,
--    L.CPI AS LIDER_CPI,
--    L.NOME AS LIDER_NOME,
--    N.NOME AS NACAO,
--    C.ESPECIE,
--    C.NOME AS COMUNIDADE,
--    C.QTD_HABITANTES,
--    H.PLANETA,
--    S.NOME AS SISTEMA
--FROM
--    FACCAO F
--    JOIN LIDER L ON F.LIDER = L.CPI
--    JOIN PARTICIPA P ON F.NOME = P.FACCAO
--    JOIN COMUNIDADE C ON P.ESPECIE = C.ESPECIE AND P.COMUNIDADE = C.NOME
--    JOIN HABITACAO H ON C.ESPECIE = H.ESPECIE AND C.COMUNIDADE = H.COMUNIDADE
--    JOIN PLANETA PL ON H.PLANETA = PL.ID_ASTRO
--    JOIN SISTEMA S ON PL.ID_ASTRO = S.ESTRELA
--    JOIN NACAO_FACCAO NF ON F.NOME = NF.FACCAO
--    JOIN NACAO N ON NF.NACAO = N.NOME;
--
--
--CREATE OR REPLACE PROCEDURE SP_RELATORIO_COMUNIDADES (
--    p_faccao IN VARCHAR2,
--    p_lider_cpi IN CHAR,
--    p_group_by IN VARCHAR2
--) IS
--    v_sql VARCHAR2(4000);
--BEGIN
--    v_sql := 'SELECT ';
--
--    CASE p_group_by
--        WHEN 'nacao' THEN
--            v_sql := v_sql || 'NACAO, ';
--        WHEN 'especie' THEN
--            v_sql := v_sql || 'ESPECIE, ';
--        WHEN 'planeta' THEN
--            v_sql := v_sql || 'PLANETA, ';
--        WHEN 'sistema' THEN
--            v_sql := v_sql || 'SISTEMA, ';
--        ELSE
--            RAISE_APPLICATION_ERROR(-20001, 'Par�metro de agrupamento inv�lido');
--    END CASE;
--
--    v_sql := v_sql || 'COUNT(COMUNIDADE) AS QTD_COMUNIDADES, SUM(QTD_HABITANTES) AS TOTAL_HABITANTES ' ||
--              'FROM V_COMUNIDADES ' ||
--              'WHERE FACCAO = :faccao AND LIDER_CPI = :lider_cpi ' ||
--              'GROUP BY ' || p_group_by;
--
--    EXECUTE IMMEDIATE v_sql USING p_faccao, p_lider_cpi;
--END;
