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

def criar_overview_oficial(app, mostrar_tela_inicial, usuario, faccao, mostrar_relatorio_oficial, mostrar_relatorio_lider, mostrar_tela_oficial):
    tipo_usuario = "oficial"
    frame_overview_oficial = ctk.CTkScrollableFrame(app, width=1400, height=800)
    # Bem-vindo Oficial
    label_oficial = ctk.CTkLabel(frame_overview_oficial, text=f"Bem-vindo Oficial {usuario}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    if(faccao != 0):   
        label_operacao_a1 = ctk.CTkLabel(frame_overview_oficial, text="Alterar nome da Facção", font=("Arial", 18))
        label_operacao_a1 .pack(pady=10)
        
        # Nome novo da facção
        label_nome_novo = ctk.CTkLabel(frame_overview_oficial, text="Novo nome para facção")
        label_nome_novo.pack(pady=(10, 0))
        entrada_nome_novo = ctk.CTkEntry(frame_overview_oficial)
        entrada_nome_novo.pack(pady=(0, 10))

        # Botão para atualizar nome da facção
        botao_atualizar_faccao = ctk.CTkButton(frame_overview_oficial, text="Atualizar Facção", command=lambda: alterar_nome_faccao(faccao, entrada_nome_novo), width=400, height=40)
        botao_atualizar_faccao.pack(pady=10)

        label_operacao_a2 = ctk.CTkLabel(frame_overview_oficial, text="Indicar novo líder", font=("Arial", 18))
        label_operacao_a2 .pack(pady=10)
        # Novo líder
        label_novo_lider = ctk.CTkLabel(frame_overview_oficial, text="Novo Líder")
        label_novo_lider.pack(pady=(10, 0))
        entrada_novo_lider = ctk.CTkEntry(frame_overview_oficial)
        entrada_novo_lider.pack(pady=(0, 10))

        # Botão para atualizar novo líder
        botao_atualizar_lider = ctk.CTkButton(frame_overview_oficial, text="Atualizar Líder", command=lambda: alterar_lider(faccao, entrada_novo_lider), width=400, height=40)
        botao_atualizar_lider.pack(pady=10)

        label_operacao_a3 = ctk.CTkLabel(frame_overview_oficial, text="Credenciar comunidades novas", font=("Arial", 18))
        label_operacao_a3 .pack(pady=10)

        # Espécie
        label_especie = ctk.CTkLabel(frame_overview_oficial, text="Espécie")
        label_especie.pack(pady=(10, 0))
        entrada_especie = ctk.CTkEntry(frame_overview_oficial)
        entrada_especie.pack(pady=(0, 10))

        # Nome da comunidade
        label_nome_comunidade = ctk.CTkLabel(frame_overview_oficial, text="Comunidade")
        label_nome_comunidade.pack(pady=(10, 0))
        entrada_nome_comunidade = ctk.CTkEntry(frame_overview_oficial)
        entrada_nome_comunidade.pack(pady=(0, 10))

        # Botão para atualizar dados da comunidade
        botao_atualizar_comunidade = ctk.CTkButton(frame_overview_oficial, text="Atualizar Comunidade", command=lambda:  credenciar_comunidades(faccao, entrada_especie, entrada_nome_comunidade),width=400, height=40)
        botao_atualizar_comunidade.pack(pady=10)
        
        # Botão para ver relatórios lider
        botao_ver_relatorios_lider = ctk.CTkButton(frame_overview_oficial, text="Ver Relatórios de Líder", command=lambda: mostrar_relatorio_lider(usuario, faccao, tipo_usuario), width=400, height=40)
        botao_ver_relatorios_lider.pack(pady=10)

    # Botão para ver relatórios
    botao_ver_relatorios = ctk.CTkButton(frame_overview_oficial, text="Ver Relatórios", command=lambda: mostrar_relatorio_oficial(usuario, faccao, tipo_usuario), width=400, height=40)
    botao_ver_relatorios.pack(pady=10)

    # Botão para voltar à tela de login
    botao_voltar_login = ctk.CTkButton(frame_overview_oficial, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)

    return frame_overview_oficial