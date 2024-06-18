---------------------------------------------------
-- Proejto Final - Laboratorio de Bases de Dados --
---------------------------------------------------

----------------------------------------------------------
-- Scripts para Testes das Funcionalidades e Relatórios --
----------------------------------------------------------

---------------------------------------
-- FUNCIONALIDADES - Líder da Facção --
---------------------------------------

-- Alterar nome da facção -- OK
BEGIN
    PacoteLiderFaccao.AlterarNomeFaccao('PROGRESSITA04', 'PROGRESSITA05');
END;

-- Indicar novo Lider -- OK
BEGIN
    PacoteLiderFaccao.IndicarNovoLiderFaccao('FAC_CAMERA', '555.436.559-76');
END;


--BEGIN
--    PacoteLiderFaccao.CredenciarComunidadesNovas();
--END;


----------------------------------
-- RELATÓRIO - Líder da Facção --
----------------------------------

-- Caso DEFAULT -- OK
SELECT agrupamento AS COMUNIDADE, especie, total_habitantes FROM TABLE(relatorio_lider_faccao(p_lider_id => '999.999.999-98'));

-- Agrupamento por ESPECIE -- OK
SELECT agrupamento AS ESPECIE, qtd_comunidades, total_habitantes FROM TABLE(relatorio_lider_faccao(p_lider_id => '999.999.999-98', p_agrupamento => 'ESPECIE'));

-- Agrupamento por PLANETA -- OK
SELECT agrupamento AS PLANETA, qtd_comunidades, total_habitantes FROM TABLE(relatorio_lider_faccao(p_lider_id => '999.999.999-98', p_agrupamento => 'PLANETA'));

-- Agrupamento por SISTEMA -- OK
SELECT agrupamento AS SISTEMA, qtd_comunidades, total_habitantes FROM TABLE(relatorio_lider_faccao(p_lider_id => '999.999.999-98', p_agrupamento => 'SISTEMA'));

-- Agrupamento por NACAO -- OK
SELECT agrupamento AS NACAO, qtd_comunidades, total_habitantes FROM TABLE(relatorio_lider_faccao(p_lider_id => '999.999.999-98', p_agrupamento => 'NACAO'));