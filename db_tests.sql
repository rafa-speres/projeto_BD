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

-- Credenciar comunidades novas -- OK
BEGIN
    PacoteLiderFaccao.CredenciarComunidadesNovas('faccao_suprema', 'Ut nam', 'com_fritas');
END;

-- Remover Faccao de Nacao  -- OK
BEGIN
    PacoteLiderFaccao.RemoverFaccaoDeNacao('Sit saepe ad.', 'Faccao_Caballo');
END;


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


-------------------------
-- RELATÓRIO - Oficial --
-------------------------

-- Caso DEFAULT -- OK
SELECT agrupamento as COMUNIDADE, total_habitantes, data_ini as DATA_INICIO, data_fim FROM TABLE(pkg_oficial.relatorio_oficial('999.999.999-98'));

-- Agrupamento por FACCAO -- OK
SELECT agrupamento as FACCAO, qtd_comunidades, total_habitantes FROM TABLE(pkg_oficial.relatorio_oficial('999.999.999-98', 'FACCAO'));

-- Agrupamento por ESPECIE -- OK
SELECT agrupamento as ESPECIE, qtd_comunidades, total_habitantes FROM TABLE(pkg_oficial.relatorio_oficial('999.999.999-98', 'ESPECIE'));

-- Agrupamento por PLANETA  -- OK
SELECT agrupamento as PLANETA, qtd_comunidades, total_habitantes FROM TABLE(pkg_oficial.relatorio_oficial('999.999.999-98', 'PLANETA'));

-- Agrupamento por SISTEMA -- OK
SELECT agrupamento as SISTEMA, qtd_comunidades, total_habitantes FROM TABLE(pkg_oficial.relatorio_oficial('999.999.999-98', 'SISTEMA'));
