import customtkinter as ctk
from tkinter import messagebox
from database import conectar_bd
from datetime import datetime

def incluir_nacao(usuario, federacao):
    federacao = federacao.get()
    if federacao:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT NACAO FROM LIDER WHERE CPI = :1", [usuario])
        result = cursor.fetchone()
        if result:
            nacao = result[0]
            try:
                cursor.callproc("pkg_comandante.incluir_nacao_em_federacao", [usuario, nacao, federacao])
                conn.commit()
                messagebox.showinfo("Sucesso", "Nação incluída!")
            except Exception as e:
                conn.rollback()
                messagebox.showerror("Erro", f"Falha ao incluir nação")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Erro", "Nação não encontrada para o usuário fornecido.")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")      
        
          
def excluir_nacao(usuario, federacao):
    federacao = federacao.get()
    
    if federacao:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT NACAO FROM LIDER WHERE CPI = :1", [usuario])
        result = cursor.fetchone()
        if result:
            nacao = result[0]
            try:
                cursor.callproc("pkg_comandante.excluir_nacao_de_federacao", [usuario, nacao, federacao])
                conn.commit()
                messagebox.showinfo("Sucesso", "Nação excluida da federacao!")
            except Exception as e:
                conn.rollback()
                messagebox.showerror("Erro", f"Falha ao excluir nacao da federacao")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Erro", "Nação não encontrada para o usuário fornecido.")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")      

def criar_federacao(usuario, federacao):
    federacao = federacao.get()
    
    if federacao:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT NACAO FROM LIDER WHERE CPI = :1", [usuario])
        result = cursor.fetchone()
        if result:
            nacao = result[0]
            # Pegando a data atual do sistema
            data_atual = datetime.now()
                
            # Convertendo a data para o formato aceito pelo Oracle
            data_ini = data_atual.date()
            try:
                cursor.callproc("pkg_comandante.criar_federacao_com_nacao", [federacao, usuario, nacao, data_ini])
                conn.commit()
                messagebox.showinfo("Sucesso", "Federação criada")
            except Exception as e:
                conn.rollback()
                messagebox.showerror("Erro", f"Falha ao criar federação")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Erro", "Nação não encontrada para o usuário fornecido.")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")  
            
def inserir_dominancia(usuario, planeta):
    planeta = planeta.get()
    
    if planeta:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT NACAO FROM LIDER WHERE CPI = :1", [usuario])
        result = cursor.fetchone()
        if result:
            nacao = result[0]
            # Pegando a data atual do sistema
            data_atual = datetime.now()
                
            # Convertendo a data para o formato aceito pelo Oracle
            data_ini = data_atual.date()
            try:
                cursor.callproc("pkg_comandante.inserir_dominancia", [planeta, nacao, data_ini])
                conn.commit()
                messagebox.showinfo("Sucesso", "Dominância inserida!")
            except Exception as e:
                conn.rollback()
                messagebox.showerror("Erro", f"Falha ao inserir dominância")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Erro", "Nação não encontrada para o usuário fornecido.")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")  


def alterar_nome_faccao(faccao, nova_faccao):
    nova_faccao = nova_faccao.get()
    
    if nova_faccao:
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
                BEGIN
                    PacoteLiderFaccao.AlterarNomeFaccao('{faccao[0]}', '{nova_faccao}');
                END;
            """)
            conn.commit()
            messagebox.showinfo("Sucesso", "Nome de facção alterado!")
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Erro", f"Falha ao alterar nome da facção")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")  

def alterar_lider(faccao, novo_lider):
    novo_lider = novo_lider.get()
    
    if novo_lider:
        conn = conectar_bd()
        cursor = conn.cursor()
        check = 0
        try:
            cursor.execute(f"""
                BEGIN
                    PacoteLiderFaccao.IndicarNovoLiderFaccao('{faccao[0]}', '{novo_lider}');
                END;
            """)
            conn.commit()
            messagebox.showinfo("Sucesso", "Lider alterado!")
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Erro", f"Falha ao alterar lider")
            check = 1
        finally:
            cursor.close()
            conn.close()
            if check == 0:
                faccao[0] = 0
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")  

def atualizar_pagina(faccao,novo_lider,app, mostrar_tela_inicial, usuario, mostrar_relatorio_comandante, mostrar_relatorio_lider, mostrar_tela_comandante):
    alterar_lider(faccao,novo_lider)
    for widget in app.winfo_children():
        widget.pack_forget()
    criar_overview_comandante(app, mostrar_tela_inicial, usuario, faccao, mostrar_relatorio_comandante, mostrar_relatorio_lider, mostrar_tela_comandante)


def credenciar_comunidades(faccao, especie, comunidade):
    especie = especie.get()
    comunidade = comunidade.get()
    
    if especie and comunidade:
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
                BEGIN
                    PacoteLiderFaccao.CredenciarComunidadesNovas('{faccao[0]}', '{especie}', '{comunidade}');
                END;
            """)
            conn.commit()
            messagebox.showinfo("Sucesso", "Comunidade credenciada!")
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Erro", f"Falha ao credenciar")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")  
        
def remover_nacao_faccao(faccao, nacao):
    nacao = nacao.get()
    
    if nacao:
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
                BEGIN
                    PacoteLiderFaccao.RemoverFaccaoDeNacao('{nacao}', '{faccao[0]}');
                END;
            """)
            conn.commit()
            messagebox.showinfo("Sucesso", "Relação removida!")
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Erro", f"Falha ao remover")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

def criar_overview_comandante(app, mostrar_tela_inicial, usuario, faccao, mostrar_relatorio_comandante, mostrar_relatorio_lider, mostrar_tela_comandante):
    #faccao = [faccao]
    if not isinstance(faccao, list):
        faccao = [faccao]
    tipo_usuario = "comandante"
    frame_overview_comandante = ctk.CTkScrollableFrame(app, width=1400, height=800)
    frame_overview_comandante.pack()

    label_oficial = ctk.CTkLabel(frame_overview_comandante, text=f"Bem-vindo Comandante {usuario}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    if faccao[0] != 0:
        label_operacao_a1 = ctk.CTkLabel(frame_overview_comandante, text="Alterar nome da Facção", font=("Arial", 18))
        label_operacao_a1.pack(pady=10)
        
        # Nome novo da facção
        label_nome_novo = ctk.CTkLabel(frame_overview_comandante, text="Novo nome para facção")
        label_nome_novo.pack(pady=(10, 0))
        entrada_nome_novo = ctk.CTkEntry(frame_overview_comandante)
        entrada_nome_novo.pack(pady=(0, 10))

        # Botão para atualizar nome da facção
        botao_atualizar_faccao = ctk.CTkButton(frame_overview_comandante, text="Atualizar Facção", command=lambda: alterar_nome_faccao(faccao, entrada_nome_novo), width=400, height=40)
        botao_atualizar_faccao.pack(pady=10)

        label_operacao_a2 = ctk.CTkLabel(frame_overview_comandante, text="Indicar novo líder", font=("Arial", 18))
        label_operacao_a2.pack(pady=10)
        
        # Novo líder
        label_novo_lider = ctk.CTkLabel(frame_overview_comandante, text="Novo Líder")
        label_novo_lider.pack(pady=(10, 0))
        entrada_novo_lider = ctk.CTkEntry(frame_overview_comandante)
        entrada_novo_lider.pack(pady=(0, 10))

        # Botão para atualizar novo líder
        botao_atualizar_lider = ctk.CTkButton(frame_overview_comandante, text="Atualizar Líder", command=lambda: atualizar_pagina(faccao, entrada_novo_lider, app, mostrar_tela_inicial, usuario, mostrar_relatorio_comandante, mostrar_relatorio_lider, mostrar_tela_comandante), width=400, height=40)
        botao_atualizar_lider.pack(pady=10)

        label_operacao_a3 = ctk.CTkLabel(frame_overview_comandante, text="Credenciar comunidades novas", font=("Arial", 18))
        label_operacao_a3.pack(pady=10)

        # Espécie
        label_especie = ctk.CTkLabel(frame_overview_comandante, text="Espécie")
        label_especie.pack(pady=(10, 0))
        entrada_especie = ctk.CTkEntry(frame_overview_comandante)
        entrada_especie.pack(pady=(0, 10))

        # Nome da comunidade
        label_nome_comunidade = ctk.CTkLabel(frame_overview_comandante, text="Nome Comunidade")
        label_nome_comunidade.pack(pady=(10, 0))
        entrada_nome_comunidade = ctk.CTkEntry(frame_overview_comandante)
        entrada_nome_comunidade.pack(pady=(0, 10))

        # Botão para atualizar dados da comunidade
        botao_atualizar_comunidade = ctk.CTkButton(frame_overview_comandante, text="Credenciar Comunidade", command=lambda: credenciar_comunidades(faccao, entrada_especie, entrada_nome_comunidade), width=400, height=40)
        botao_atualizar_comunidade.pack(pady=10)
        
        # Botão para atualizar dados da comunidade
        botao_atualizar_comunidade = ctk.CTkButton(frame_overview_comandante, text="Atualizar Comunidade", command=lambda: credenciar_comunidades(faccao, entrada_especie, entrada_nome_comunidade), width=400, height=40)
        botao_atualizar_comunidade.pack(pady=10)
        
        label_operacao_a4 = ctk.CTkLabel(frame_overview_comandante, text="Remover nação da facção", font=("Arial", 18))
        label_operacao_a4.pack(pady=10)
        
        # Nome da nacao
        label_nome_nac = ctk.CTkLabel(frame_overview_comandante, text="Nação")
        label_nome_nac.pack(pady=(10, 0))
        entrada_nome_nac = ctk.CTkEntry(frame_overview_comandante)
        entrada_nome_nac.pack(pady=(0, 10))
        
        botao_remover_nacao = ctk.CTkButton(frame_overview_comandante, text="Remover Nação", command=lambda: remover_nacao_faccao(faccao, entrada_nome_nac), width=400, height=40)
        botao_remover_nacao.pack(pady=10)
        
        # Botão para ver relatórios de líder
        botao_ver_relatorios_lider = ctk.CTkButton(frame_overview_comandante, text="Ver Relatórios de líder", command=lambda: mostrar_relatorio_lider(usuario, faccao, tipo_usuario), width=400, height=40)
        botao_ver_relatorios_lider.pack(pady=10)
    
    #inluir a sua nação em uma federacao
    label_incluir = ctk.CTkLabel(frame_overview_comandante, text="Incluir a sua nação em uma federacao")
    label_incluir.pack(pady=(10, 0))
    
    #federacao
    label_federacao = ctk.CTkLabel(frame_overview_comandante, text="Federação")
    label_federacao.pack(pady=(10, 0))
    entrada_federacao = ctk.CTkEntry(frame_overview_comandante)
    entrada_federacao.pack(pady=(0, 10))
    
    #botao para incluir nacao
    botao_incluir_nacao = ctk.CTkButton(frame_overview_comandante, text="Incluir", command=lambda: incluir_nacao(usuario, entrada_federacao), width=400, height=40)
    botao_incluir_nacao.pack(pady=10)
    
    #excluir a sua nação em uma federacao
    label_excluir = ctk.CTkLabel(frame_overview_comandante, text="Excluir a sua nação da federação")
    label_excluir.pack(pady=(10, 0))
    
    #federacao
    label_federacao_e = ctk.CTkLabel(frame_overview_comandante, text="Federação")
    label_federacao_e.pack(pady=(10, 0))
    entrada_federacao_e = ctk.CTkEntry(frame_overview_comandante)
    entrada_federacao_e.pack(pady=(0, 10))
    
    #botao para excluir nacao
    botao_incluir_nacao = ctk.CTkButton(frame_overview_comandante, text="Excluir", command=lambda: excluir_nacao(usuario, entrada_federacao_e), width=400, height=40)
    botao_incluir_nacao.pack(pady=10)
    
    #criar federacao com a nacao
    label_criar = ctk.CTkLabel(frame_overview_comandante, text="Criar federação com a nação")
    label_criar.pack(pady=(10, 0))
    
    #federacao
    label_federacao_c = ctk.CTkLabel(frame_overview_comandante, text="Federação")
    label_federacao_c.pack(pady=(10, 0))
    entrada_federacao_c = ctk.CTkEntry(frame_overview_comandante)
    entrada_federacao_c.pack(pady=(0, 10))
    
    #botao para criar federacao
    botao_criar_federacao = ctk.CTkButton(frame_overview_comandante, text="Criar", command=lambda: criar_federacao(usuario, entrada_federacao_c), width=400, height=40)
    botao_criar_federacao.pack(pady=10)
    
    #inserir nova dominancia de planeta
    label_criar = ctk.CTkLabel(frame_overview_comandante, text="Inserir nova dominancia de planeta")
    label_criar.pack(pady=(10, 0))
    
    #planeta
    label_planeta = ctk.CTkLabel(frame_overview_comandante, text="Planeta")
    label_planeta.pack(pady=(10, 0))
    entrada_planeta = ctk.CTkEntry(frame_overview_comandante)
    entrada_planeta.pack(pady=(0, 10))
    
    #botao para inserir dominancia
    botao_inserir_dominancia = ctk.CTkButton(frame_overview_comandante, text="Inserir dominancia", command=lambda: inserir_dominancia(usuario, entrada_planeta), width=400, height=40)
    botao_inserir_dominancia.pack(pady=10)
    
    label_entry_distancia = ctk.CTkLabel(frame_overview_comandante, text="Distancia máxima")
    label_entry_distancia.pack(pady=5)
    entry_distancia = ctk.CTkEntry(frame_overview_comandante, width=400)
    entry_distancia.pack(pady=5)
    
    # Botão para ver relatórios
    botao_ver_relatorios = ctk.CTkButton(frame_overview_comandante, text="Ver Relatórios", command=lambda: mostrar_relatorio_comandante(usuario, faccao[0], tipo_usuario, entry_distancia.get()), width=400, height=40)
    botao_ver_relatorios.pack(pady=10)

    # Botão para voltar à tela de login
    botao_voltar_login = ctk.CTkButton(frame_overview_comandante, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)

    return frame_overview_comandante