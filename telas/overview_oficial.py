import customtkinter as ctk

def criar_overview_oficial(app, mostrar_tela_inicial, usuario, faccao):
    frame_overview_oficial = ctk.CTkScrollableFrame(app, width=1600, height=900)
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
        botao_atualizar_faccao = ctk.CTkButton(frame_overview_oficial, text="Atualizar Facção", width=400, height=40)
        botao_atualizar_faccao.pack(pady=10)

        label_operacao_a2 = ctk.CTkLabel(frame_overview_oficial, text="Indicar novo líder", font=("Arial", 18))
        label_operacao_a2 .pack(pady=10)
        # Novo líder
        label_novo_lider = ctk.CTkLabel(frame_overview_oficial, text="Novo Líder")
        label_novo_lider.pack(pady=(10, 0))
        entrada_novo_lider = ctk.CTkEntry(frame_overview_oficial)
        entrada_novo_lider.pack(pady=(0, 10))

        # Botão para atualizar novo líder
        botao_atualizar_lider = ctk.CTkButton(frame_overview_oficial, text="Atualizar Líder", width=400, height=40)
        botao_atualizar_lider.pack(pady=10)

        label_operacao_a3 = ctk.CTkLabel(frame_overview_oficial, text="Credenciar comunidades novas", font=("Arial", 18))
        label_operacao_a3 .pack(pady=10)
        # Facção
        label_faccao = ctk.CTkLabel(frame_overview_oficial, text="Facção")
        label_faccao.pack(pady=(10, 0))
        entrada_faccao = ctk.CTkEntry(frame_overview_oficial)
        entrada_faccao.pack(pady=(0, 10))

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
        botao_atualizar_comunidade = ctk.CTkButton(frame_overview_oficial, text="Atualizar Comunidade", width=400, height=40)
        botao_atualizar_comunidade.pack(pady=10)

    # Botão para ver relatórios
    botao_ver_relatorios = ctk.CTkButton(frame_overview_oficial, text="Ver Relatórios", width=400, height=40)
    botao_ver_relatorios.pack(pady=10)

    # Botão para voltar à tela de login
    botao_voltar_login = ctk.CTkButton(frame_overview_oficial, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)

    return frame_overview_oficial