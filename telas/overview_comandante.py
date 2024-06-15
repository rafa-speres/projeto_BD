import customtkinter as ctk

def criar_overview_comandante(app, mostrar_tela_inicial, usuario, faccao, mostrar_relatorio_comandante, mostrar_relatorio_lider):
    tipo_usuario = "comandante"
    frame_overview_comandante = ctk.CTkScrollableFrame(app, width=1400, height=800)
    label_oficial = ctk.CTkLabel(frame_overview_comandante, text=f"Bem-vindo Comandante {usuario}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    if(faccao != 0):   
        label_operacao_a1 = ctk.CTkLabel(frame_overview_comandante, text="Alterar nome da Facção", font=("Arial", 18))
        label_operacao_a1 .pack(pady=10)
        
        # Nome novo da facção
        label_nome_novo = ctk.CTkLabel(frame_overview_comandante, text="Novo nome para facção")
        label_nome_novo.pack(pady=(10, 0))
        entrada_nome_novo = ctk.CTkEntry(frame_overview_comandante)
        entrada_nome_novo.pack(pady=(0, 10))

        # Botão para atualizar nome da facção
        botao_atualizar_faccao = ctk.CTkButton(frame_overview_comandante, text="Atualizar Facção", width=400, height=40)
        botao_atualizar_faccao.pack(pady=10)

        label_operacao_a2 = ctk.CTkLabel(frame_overview_comandante, text="Indicar novo líder", font=("Arial", 18))
        label_operacao_a2 .pack(pady=10)
        # Novo líder
        label_novo_lider = ctk.CTkLabel(frame_overview_comandante, text="Novo Líder")
        label_novo_lider.pack(pady=(10, 0))
        entrada_novo_lider = ctk.CTkEntry(frame_overview_comandante)
        entrada_novo_lider.pack(pady=(0, 10))

        # Botão para atualizar novo líder
        botao_atualizar_lider = ctk.CTkButton(frame_overview_comandante, text="Atualizar Líder", width=400, height=40)
        botao_atualizar_lider.pack(pady=10)

        label_operacao_a3 = ctk.CTkLabel(frame_overview_comandante, text="Credenciar comunidades novas", font=("Arial", 18))
        label_operacao_a3 .pack(pady=10)
        # Facção
        label_faccao = ctk.CTkLabel(frame_overview_comandante, text="Facção")
        label_faccao.pack(pady=(10, 0))
        entrada_faccao = ctk.CTkEntry(frame_overview_comandante)
        entrada_faccao.pack(pady=(0, 10))

        # Espécie
        label_especie = ctk.CTkLabel(frame_overview_comandante, text="Espécie")
        label_especie.pack(pady=(10, 0))
        entrada_especie = ctk.CTkEntry(frame_overview_comandante)
        entrada_especie.pack(pady=(0, 10))

        # Nome da comunidade
        label_nome_comunidade = ctk.CTkLabel(frame_overview_comandante, text="Comunidade")
        label_nome_comunidade.pack(pady=(10, 0))
        entrada_nome_comunidade = ctk.CTkEntry(frame_overview_comandante)
        entrada_nome_comunidade.pack(pady=(0, 10))

        # Botão para atualizar dados da comunidade
        botao_atualizar_comunidade = ctk.CTkButton(frame_overview_comandante, text="Atualizar Comunidade", width=400, height=40)
        botao_atualizar_comunidade.pack(pady=10)
        
        # Botão para ver relatórios de lider
        botao_ver_relatorios_lider = ctk.CTkButton(frame_overview_comandante, text="Ver Relatórios de líder", command=lambda: mostrar_relatorio_lider(usuario, faccao, tipo_usuario), width=400, height=40)
        botao_ver_relatorios_lider.pack(pady=10)
    
    # Incluir/Excluir nação de federação
    label_incluir_excluir = ctk.CTkLabel(frame_overview_comandante, text="Incluir/Excluir nação de federação", font=("Arial", 18))
    label_incluir_excluir.pack(pady=10)
    label_federacao = ctk.CTkLabel(frame_overview_comandante, text="Federação:", font=("Arial", 14))
    label_federacao.pack(pady=5)
    entry_federacao = ctk.CTkEntry(frame_overview_comandante, width=400)
    entry_federacao.pack(pady=5)
    button_incluir_excluir = ctk.CTkButton(frame_overview_comandante, text="Incluir/Excluir")
    button_incluir_excluir.pack(pady=10)

    # Criar federação
    label_criar_federacao_texto = ctk.CTkLabel(frame_overview_comandante, text="Criar Federação", font=("Arial", 18))
    label_criar_federacao_texto.pack(pady=10)
    label_criar_federacao = ctk.CTkLabel(frame_overview_comandante, text="Federação:", font=("Arial", 14))
    label_criar_federacao.pack(pady=5)
    entry_criar_federacao = ctk.CTkEntry(frame_overview_comandante, width=400)
    entry_criar_federacao.pack(pady=5)
    button_criar_federacao = ctk.CTkButton(frame_overview_comandante, text="Criar")
    button_criar_federacao.pack(pady=10)

    # Inserir dominância
    label_inserir_dominancia_texto = ctk.CTkLabel(frame_overview_comandante, text="Inserir Dominância", font=("Arial", 18))
    label_inserir_dominancia_texto.pack(pady=10)
    label_planeta = ctk.CTkLabel(frame_overview_comandante, text="Planeta:", font=("Arial", 14))
    label_planeta.pack(pady=5)
    entry_planeta = ctk.CTkEntry(frame_overview_comandante, width=400)
    entry_planeta.pack(pady=5)
    
    # Botão para ver relatórios
    botao_ver_relatorios = ctk.CTkButton(frame_overview_comandante, text="Ver Relatórios", command=lambda: mostrar_relatorio_comandante(usuario, faccao), width=400, height=40)
    botao_ver_relatorios.pack(pady=10)

    # Botão para voltar à tela de login
    botao_voltar_login = ctk.CTkButton(frame_overview_comandante, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)
    return frame_overview_comandante