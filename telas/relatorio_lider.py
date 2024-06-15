import customtkinter as ctk

def criar_relatorio_lider(app, mostrar_tela_inicial, mostrar_tela_cientista, mostrar_tela_comandante, mostrar_tela_oficial, usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_comandante, mostrar_relatorio_oficial, mostrar_relatorio_lider, tipo_usuario):
    frame_relatorio_lider = ctk.CTkScrollableFrame(app, width=1400, height=800)
    # Bem-vindo 
    label_oficial = ctk.CTkLabel(frame_relatorio_lider, text=f"Bem-vindo Líder {usuario}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    if tipo_usuario == "oficial":
        botao_voltar_oficial = ctk.CTkButton(frame_relatorio_lider, text="Voltar à Tela de Oficial", command=lambda: mostrar_tela_oficial(usuario,faccao, mostrar_relatorio_oficial, mostrar_relatorio_lider), width=400, height=40)
        botao_voltar_oficial.pack(pady=10)
    elif tipo_usuario == "comandante":
        botao_voltar_comandante = ctk.CTkButton(frame_relatorio_lider, text="Voltar à Tela de Comandante", command=lambda: mostrar_tela_comandante(usuario, faccao, mostrar_relatorio_comandante, mostrar_relatorio_lider), width=400, height=40)
        botao_voltar_comandante.pack(pady=10)
    elif tipo_usuario == "cientista":
        botao_voltar_cientista = ctk.CTkButton(frame_relatorio_lider, text="Voltar à Tela de Cientista", command=lambda: mostrar_tela_cientista(usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_cientista), width=400, height=40)
        botao_voltar_cientista.pack(pady=10)
    
    botao_voltar_login = ctk.CTkButton(frame_relatorio_lider, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)
        
    
    
    return frame_relatorio_lider