import customtkinter as ctk
from tkinter import messagebox
from database import conectar_bd

def alterar_nome_faccao(faccao, nova_faccao):
    nova_faccao = nova_faccao.get()
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute(f"""
            BEGIN
                PacoteLiderFaccao.AlterarNomeFaccao('{faccao}', '{nova_faccao}');
            END;
        """)
        conn.commit()
        messagebox.showinfo("Sucesso", "Nome de facção alterado!")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Erro", f"Falha ao alterar nome da facção: {e}")
    finally:
        cursor.close()
        conn.close()
        
def alterar_lider(faccao, novo_lider):
    novo_lider = novo_lider.get()
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute(f"""
            BEGIN
                PacoteLiderFaccao.IndicarNovoLiderFaccao('{faccao}', '{novo_lider}');
            END;
        """)
        conn.commit()
        messagebox.showinfo("Sucesso", "Lider alterado!")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Erro", f"Falha ao alterar lider: {e}")
    finally:
        cursor.close()
        conn.close()
        
def credenciar_comunidades(faccao, especie, comunidade):
    especie = especie.get()
    comunidade = comunidade.get()
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute(f"""
            BEGIN
                PacoteLiderFaccao.CredenciarComunidadesNovas('{faccao}', '{especie}', '{comunidade}');
            END;
        """)
        conn.commit()
        messagebox.showinfo("Sucesso", "Lider alterado!")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Erro", f"Falha ao alterar lider: {e}")
    finally:
        cursor.close()
        conn.close()

def criar_overview_cientista(app, mostrar_tela_inicial, usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_lider, mostrar_tela_cientista):
    tipo_usuario = "cientista"
    frame_overview_cientista = ctk.CTkScrollableFrame(app, width=1400, height=800)
    label_oficial = ctk.CTkLabel(frame_overview_cientista, text=f"Bem-vindo Cientista {usuario}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    if(faccao != 0):   
        label_operacao_a1 = ctk.CTkLabel(frame_overview_cientista, text="Alterar nome da Facção", font=("Arial", 18))
        label_operacao_a1 .pack(pady=10)
        
        # Nome novo da facção
        label_nome_novo = ctk.CTkLabel(frame_overview_cientista, text="Novo nome para facção")
        label_nome_novo.pack(pady=(10, 0))
        entrada_nome_novo = ctk.CTkEntry(frame_overview_cientista)
        entrada_nome_novo.pack(pady=(0, 10))

        # Botão para atualizar nome da facção
        botao_atualizar_faccao = ctk.CTkButton(frame_overview_cientista, text="Atualizar Facção", command=lambda: alterar_nome_faccao(faccao, entrada_nome_novo), width=400, height=40)
        botao_atualizar_faccao.pack(pady=10)

        label_operacao_a2 = ctk.CTkLabel(frame_overview_cientista, text="Indicar novo líder", font=("Arial", 18))
        label_operacao_a2 .pack(pady=10)
        # Novo líder
        label_novo_lider = ctk.CTkLabel(frame_overview_cientista, text="Novo Líder")
        label_novo_lider.pack(pady=(10, 0))
        entrada_novo_lider = ctk.CTkEntry(frame_overview_cientista)
        entrada_novo_lider.pack(pady=(0, 10))

        # Botão para atualizar novo líder
        botao_atualizar_lider = ctk.CTkButton(frame_overview_cientista, text="Atualizar Líder", command=lambda: alterar_lider(faccao, entrada_novo_lider), width=400, height=40)
        botao_atualizar_lider.pack(pady=10)

        label_operacao_a3 = ctk.CTkLabel(frame_overview_cientista, text="Credenciar comunidades novas", font=("Arial", 18))
        label_operacao_a3 .pack(pady=10)

        # Espécie
        label_especie = ctk.CTkLabel(frame_overview_cientista, text="Espécie")
        label_especie.pack(pady=(10, 0))
        entrada_especie = ctk.CTkEntry(frame_overview_cientista)
        entrada_especie.pack(pady=(0, 10))

        # Nome da comunidade
        label_nome_comunidade = ctk.CTkLabel(frame_overview_cientista, text="Comunidade")
        label_nome_comunidade.pack(pady=(10, 0))
        entrada_nome_comunidade = ctk.CTkEntry(frame_overview_cientista)
        entrada_nome_comunidade.pack(pady=(0, 10))

        # Botão para atualizar dados da comunidade
        botao_atualizar_comunidade = ctk.CTkButton(frame_overview_cientista, text="Atualizar Comunidade", command=lambda:  credenciar_comunidades(faccao, entrada_especie, entrada_nome_comunidade),width=400, height=40)
        botao_atualizar_comunidade.pack(pady=10)
        
        # Botão para ver relatórios de lider
        botao_ver_relatorios_lider = ctk.CTkButton(frame_overview_cientista, text="Ver Relatórios de Líder", command=lambda: mostrar_relatorio_lider(usuario, faccao, tipo_usuario), width=400, height=40)
        botao_ver_relatorios_lider.pack(pady=10)
    
    # Adicionar Estrela
    label_adicionar_estrela = ctk.CTkLabel(frame_overview_cientista, text="Adicionar Estrela", font=("Arial", 18))
    label_adicionar_estrela.pack(pady=10)
    entry_adicionar_estrela = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_adicionar_estrela.pack(pady=5)
    label_entry_adicionar_estrela = ctk.CTkLabel(frame_overview_cientista, text="Estrela")
    label_entry_adicionar_estrela.pack(pady=5)
    botao_adicionar_estrela = ctk.CTkButton(frame_overview_cientista, text="Adicionar", width=400)
    botao_adicionar_estrela.pack(pady=5)
    
    # Remover Estrela
    label_remover_estrela = ctk.CTkLabel(frame_overview_cientista, text="Remover Estrela", font=("Arial", 18))
    label_remover_estrela.pack(pady=10)
    entry_remover_estrela = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_remover_estrela.pack(pady=5)
    label_entry_remover_estrela = ctk.CTkLabel(frame_overview_cientista, text="Estrela")
    label_entry_remover_estrela.pack(pady=5)
    botao_remover_estrela = ctk.CTkButton(frame_overview_cientista, text="Remover", width=400)
    botao_remover_estrela.pack(pady=5)
    
    # Editar Estrela
    label_editar_estrela = ctk.CTkLabel(frame_overview_cientista, text="Editar Estrela", font=("Arial", 18))
    label_editar_estrela.pack(pady=10)
    entry_nome_atual_estrela = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_nome_atual_estrela.pack(pady=5)
    label_nome_atual_estrela = ctk.CTkLabel(frame_overview_cientista, text="Nome Atual da Estrela")
    label_nome_atual_estrela.pack(pady=5)
    entry_novo_nome_estrela = ctk.CTkEntry(frame_overview_cientista, width=400)
    entry_novo_nome_estrela.pack(pady=5)
    label_novo_nome_estrela = ctk.CTkLabel(frame_overview_cientista, text="Novo Nome da Estrela")
    label_novo_nome_estrela.pack(pady=5)
    botao_editar_estrela = ctk.CTkButton(frame_overview_cientista, text="Editar", width=400)
    botao_editar_estrela.pack(pady=5)
    
    # Botão para ver relatórios
    botao_ver_relatorios = ctk.CTkButton(frame_overview_cientista, text="Ver Relatórios", command=lambda: mostrar_relatorio_cientista(usuario, faccao), width=400, height=40)
    botao_ver_relatorios.pack(pady=10)

    # Botão para voltar à tela de login
    botao_voltar_login = ctk.CTkButton(frame_overview_cientista, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)
    return frame_overview_cientista