import customtkinter as ctk

def criar_overview_comandante(app, mostrar_tela_inicial, usuario, faccao):
    frame_overview_comandante = ctk.CTkScrollableFrame(app, width=1600, height=900)
    label_comandante = ctk.CTkLabel(frame_overview_comandante, text="Bem-vindo Comandante", font=("Arial", 24))
    label_comandante.pack(pady=20)
    
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
    
    botao_voltar = ctk.CTkButton(frame_overview_comandante, text="Voltar", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar.pack(pady=10)
    return frame_overview_comandante