import customtkinter as ctk
from tkinter import messagebox
from database import conectar_bd

def criar_estrela(id_estrela, nome, massa, classificacao, cX, cY, cZ):
    id_estrela = id_estrela.get()
    nome = nome.get()
    massa = massa.get()
    classificacao = classificacao.get()
    cX = cX.get()
    cY = cY.get()
    cZ = cZ.get()
    
    if id_estrela and nome and massa and classificacao and cX and cY and cZ:
        
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
                BEGIN
                    PACOTE_CIENTISTA.criar_estrela('{id_estrela}', '{nome}', '{classificacao}', {massa}, {cX}, {cY}, {cZ});
                END;
            """)
            conn.commit()
            messagebox.showinfo("Sucesso", "Estrela criada!")
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Erro", f"Falha ao criar estrela")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
        
def deletar_estrela(id_estrela):
    id_estrela = id_estrela.get()
    
    if id_estrela:
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
                BEGIN
                    PACOTE_CIENTISTA.deletar_estrela('{id_estrela}');
                END;
            """)
            conn.commit()
            messagebox.showinfo("Sucesso", "Estrela excluida!")
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Erro", f"Falha ao excluir estrela")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
        
def atualizar_estrela(id_estrela, nome, massa, classificacao, cX, cY, cZ):
    id_estrela = id_estrela.get()
    nome = nome.get()
    massa = massa.get()
    classificacao = classificacao.get()
    cX = cX.get()
    cY = cY.get()
    cZ = cZ.get()
    
    if id_estrela and nome and massa and classificacao and cX and cY and cZ:
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
                BEGIN
                    PACOTE_CIENTISTA.atualizar_estrela('{id_estrela}', '{nome}', '{classificacao}', {massa}, {cX}, {cY}, {cZ});
                END;
            """)
            conn.commit()
            messagebox.showinfo("Sucesso", "Estrela atualizada!")
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Erro", f"Falha ao atualizar estrela")
        finally:
            cursor.close()
            conn.close()
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

def atualizar_pagina(faccao,novo_lider,app, mostrar_tela_inicial, usuario, mostrar_relatorio_cientista, mostrar_relatorio_lider, mostrar_tela_cientista):
    alterar_lider(faccao,novo_lider)
    for widget in app.winfo_children():
        widget.pack_forget()
    criar_overview_cientista(app, mostrar_tela_inicial, usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_lider, mostrar_tela_cientista)


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
            messagebox.showinfo("Sucesso", "Relação removida")
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Erro", f"Falha ao remover")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

def criar_overview_cientista(app, mostrar_tela_inicial, usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_lider, mostrar_tela_cientista):
    #faccao = [faccao]
    if not isinstance(faccao, list):
        faccao = [faccao]
    tipo_usuario = "cientista"
    frame_overview_cientista = ctk.CTkScrollableFrame(app, width=1400, height=800)
    frame_overview_cientista.pack()

    label_oficial = ctk.CTkLabel(frame_overview_cientista, text=f"Bem-vindo cientista {usuario}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    if faccao[0] != 0:
        label_operacao_a1 = ctk.CTkLabel(frame_overview_cientista, text="Alterar nome da Facção", font=("Arial", 18))
        label_operacao_a1.pack(pady=10)
        
        # Nome novo da facção
        label_nome_novo = ctk.CTkLabel(frame_overview_cientista, text="Novo nome para facção")
        label_nome_novo.pack(pady=(10, 0))
        entrada_nome_novo = ctk.CTkEntry(frame_overview_cientista)
        entrada_nome_novo.pack(pady=(0, 10))

        # Botão para atualizar nome da facção
        botao_atualizar_faccao = ctk.CTkButton(frame_overview_cientista, text="Atualizar Facção", command=lambda: alterar_nome_faccao(faccao, entrada_nome_novo), width=400, height=40)
        botao_atualizar_faccao.pack(pady=10)

        label_operacao_a2 = ctk.CTkLabel(frame_overview_cientista, text="Indicar novo líder", font=("Arial", 18))
        label_operacao_a2.pack(pady=10)
        
        # Novo líder
        label_novo_lider = ctk.CTkLabel(frame_overview_cientista, text="Novo Líder")
        label_novo_lider.pack(pady=(10, 0))
        entrada_novo_lider = ctk.CTkEntry(frame_overview_cientista)
        entrada_novo_lider.pack(pady=(0, 10))

        # Botão para atualizar novo líder
        botao_atualizar_lider = ctk.CTkButton(frame_overview_cientista, text="Atualizar Líder", command=lambda: atualizar_pagina(faccao, entrada_novo_lider, app, mostrar_tela_inicial, usuario, mostrar_relatorio_cientista, mostrar_relatorio_lider, mostrar_tela_cientista), width=400, height=40)
        botao_atualizar_lider.pack(pady=10)

        label_operacao_a3 = ctk.CTkLabel(frame_overview_cientista, text="Credenciar comunidades novas", font=("Arial", 18))
        label_operacao_a3.pack(pady=10)

        # Espécie
        label_especie = ctk.CTkLabel(frame_overview_cientista, text="Espécie")
        label_especie.pack(pady=(10, 0))
        entrada_especie = ctk.CTkEntry(frame_overview_cientista)
        entrada_especie.pack(pady=(0, 10))

        # Nome da comunidade
        label_nome_comunidade = ctk.CTkLabel(frame_overview_cientista, text="Nova Comunidade")
        label_nome_comunidade.pack(pady=(10, 0))
        entrada_nome_comunidade = ctk.CTkEntry(frame_overview_cientista)
        entrada_nome_comunidade.pack(pady=(0, 10))

        # Botão para atualizar dados da comunidade
        botao_atualizar_comunidade = ctk.CTkButton(frame_overview_cientista, text="Credenciar Comunidade", command=lambda: credenciar_comunidades(faccao, entrada_especie, entrada_nome_comunidade), width=400, height=40)
        botao_atualizar_comunidade.pack(pady=10)
        
        label_operacao_a4 = ctk.CTkLabel(frame_overview_cientista, text="Remover nação da facção", font=("Arial", 18))
        label_operacao_a4.pack(pady=10)
        
        # Nome da nacao
        label_nome_nac = ctk.CTkLabel(frame_overview_cientista, text="Nação")
        label_nome_nac.pack(pady=(10, 0))
        entrada_nome_nac = ctk.CTkEntry(frame_overview_cientista)
        entrada_nome_nac.pack(pady=(0, 10))
        
        botao_remover_nacao = ctk.CTkButton(frame_overview_cientista, text="Remover Nação", command=lambda: remover_nacao_faccao(faccao, entrada_nome_nac), width=400, height=40)
        botao_remover_nacao.pack(pady=10)
        
        # Botão para ver relatórios de líder
        botao_ver_relatorios_lider = ctk.CTkButton(frame_overview_cientista, text="Ver Relatórios de líder", command=lambda: mostrar_relatorio_lider(usuario, faccao, tipo_usuario), width=400, height=40)
        botao_ver_relatorios_lider.pack(pady=10)
    
    # Adicionar Estrela
    label_adicionar_estrela = ctk.CTkLabel(frame_overview_cientista, text="Adicionar Estrela", font=("Arial", 18))
    label_adicionar_estrela.pack(pady=10)
    
    label_entry_adicionar_id_estrela = ctk.CTkLabel(frame_overview_cientista, text="ID Estrela")
    label_entry_adicionar_id_estrela.pack(pady=5)
    entry_adicionar_estrela_id = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_adicionar_estrela_id.pack(pady=5)
    
    label_entry_adicionar_nome_estrela = ctk.CTkLabel(frame_overview_cientista, text="Nome da Estrela")
    label_entry_adicionar_nome_estrela.pack(pady=5)
    entry_adicionar_estrela_nome = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_adicionar_estrela_nome.pack(pady=5)
    
    label_entry_adicionar_classificacao_estrela = ctk.CTkLabel(frame_overview_cientista, text="Classificação")
    label_entry_adicionar_classificacao_estrela.pack(pady=5)
    entry_adicionar_estrela_classificacao = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_adicionar_estrela_classificacao.pack(pady=5)
    
    label_entry_adicionar_massa_estrela = ctk.CTkLabel(frame_overview_cientista, text="Massa")
    label_entry_adicionar_massa_estrela.pack(pady=5)
    entry_adicionar_estrela_massa = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_adicionar_estrela_massa.pack(pady=5)
    
    label_entry_adicionar_coordenadaX_estrela = ctk.CTkLabel(frame_overview_cientista, text="Coordenada X")
    label_entry_adicionar_coordenadaX_estrela.pack(pady=5)
    entry_adicionar_estrela_coordenadaX = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_adicionar_estrela_coordenadaX.pack(pady=5)
    
    label_entry_adicionar_coordenadaY_estrela = ctk.CTkLabel(frame_overview_cientista, text="Coordenada Y")
    label_entry_adicionar_coordenadaY_estrela.pack(pady=5)
    entry_adicionar_estrela_coordenadaY = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_adicionar_estrela_coordenadaY.pack(pady=5)
    
    label_entry_adicionar_coordenadaZ_estrela = ctk.CTkLabel(frame_overview_cientista, text="Coordenada Z")
    label_entry_adicionar_coordenadaZ_estrela.pack(pady=5)
    entry_adicionar_estrela_coordenadaZ = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_adicionar_estrela_coordenadaZ.pack(pady=5)
    
    botao_adicionar_estrela = ctk.CTkButton(frame_overview_cientista, text="Adicionar", command=lambda: criar_estrela(entry_adicionar_estrela_id, entry_adicionar_estrela_nome, entry_adicionar_estrela_massa, entry_adicionar_estrela_classificacao, entry_adicionar_estrela_coordenadaX, entry_adicionar_estrela_coordenadaY, entry_adicionar_estrela_coordenadaZ) , width=400)
    botao_adicionar_estrela.pack(pady=5)
    
    # Remover Estrela
    label_remover_estrela = ctk.CTkLabel(frame_overview_cientista, text="Remover Estrela", font=("Arial", 18))
    label_remover_estrela.pack(pady=10)
    
    label_entry_remover_estrela = ctk.CTkLabel(frame_overview_cientista, text="Id da Estrela")
    label_entry_remover_estrela.pack(pady=5)
    
    entry_remover_estrela_id = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_remover_estrela_id.pack(pady=5)
    
    botao_remover_estrela = ctk.CTkButton(frame_overview_cientista, text="Remover", command=lambda: deletar_estrela(entry_remover_estrela_id), width=400)
    botao_remover_estrela.pack(pady=5)
    
    # Atualizar Estrela
    label_atualizar_estrela = ctk.CTkLabel(frame_overview_cientista, text="Editar Estrela", font=("Arial", 18))
    label_atualizar_estrela.pack(pady=10)
    
    label_entry_atualizar_id_estrela = ctk.CTkLabel(frame_overview_cientista, text="ID Estrela")
    label_entry_atualizar_id_estrela.pack(pady=5)
    entry_atualizar_estrela_id = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_atualizar_estrela_id.pack(pady=5)
    
    label_entry_atualizar_nome_estrela = ctk.CTkLabel(frame_overview_cientista, text="Nome da Estrela")
    label_entry_atualizar_nome_estrela.pack(pady=5)
    entry_atualizar_estrela_nome = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_atualizar_estrela_nome.pack(pady=5)
    
    label_entry_atualizar_classificacao_estrela = ctk.CTkLabel(frame_overview_cientista, text="Classificação")
    label_entry_atualizar_classificacao_estrela.pack(pady=5)
    entry_atualizar_estrela_classificacao = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_atualizar_estrela_classificacao.pack(pady=5)
    
    label_entry_atualizar_massa_estrela = ctk.CTkLabel(frame_overview_cientista, text="Massa")
    label_entry_atualizar_massa_estrela.pack(pady=5)
    entry_atualizar_estrela_massa = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_atualizar_estrela_massa.pack(pady=5)
    
    label_entry_atualizar_coordenadaX_estrela = ctk.CTkLabel(frame_overview_cientista, text="Coordenada X")
    label_entry_atualizar_coordenadaX_estrela.pack(pady=5)
    entry_atualizar_estrela_coordenadaX = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_atualizar_estrela_coordenadaX.pack(pady=5)
    
    label_entry_atualizar_coordenadaY_estrela = ctk.CTkLabel(frame_overview_cientista, text="Coordenada Y")
    label_entry_atualizar_coordenadaY_estrela.pack(pady=5)
    entry_atualizar_estrela_coordenadaY = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_atualizar_estrela_coordenadaY.pack(pady=5)
    
    label_entry_atualizar_coordenadaZ_estrela = ctk.CTkLabel(frame_overview_cientista, text="Coordenada Z")
    label_entry_atualizar_coordenadaZ_estrela.pack(pady=5)
    entry_atualizar_estrela_coordenadaZ = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_atualizar_estrela_coordenadaZ.pack(pady=5)
    
    
    botao_atualizar_estrela = ctk.CTkButton(frame_overview_cientista, text="Atualizar", command=lambda: atualizar_estrela(entry_atualizar_estrela_id, entry_atualizar_estrela_nome, entry_atualizar_estrela_massa, entry_atualizar_estrela_classificacao, entry_atualizar_estrela_coordenadaX, entry_atualizar_estrela_coordenadaY, entry_atualizar_estrela_coordenadaZ), width=400)
    botao_atualizar_estrela.pack(pady=5)
    
    #para exposicao da estrela (CRUD)
    label_entry_estrela_read = ctk.CTkLabel(frame_overview_cientista, text="Estrela para Ler")
    label_entry_estrela_read.pack(pady=5)
    entry_estrela_read = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_estrela_read.pack(pady=5)
    
    
    # Botão para ver relatórios
    botao_ver_relatorios = ctk.CTkButton(frame_overview_cientista, text="Ver Relatórios", command=lambda: mostrar_relatorio_cientista(usuario, faccao[0], tipo_usuario, entry_estrela_read.get()), width=400, height=40)
    botao_ver_relatorios.pack(pady=10)

    # Botão para voltar à tela de login
    botao_voltar_login = ctk.CTkButton(frame_overview_cientista, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)
    return frame_overview_cientista