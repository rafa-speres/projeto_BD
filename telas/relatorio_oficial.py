import customtkinter as ctk

def criar_relatorio_oficial(app, mostrar_tela_inicial, usuario, faccao, mostrar_tela_oficial, mostrar_relatorio_oficial, mostrar_relatorio_lider, tipo_usuario):
    frame_relatorio_oficial = ctk.CTkScrollableFrame(app, width=1400, height=800)
    # Bem-vindo
    label_oficial = ctk.CTkLabel(frame_relatorio_oficial, text=f"Bem-vindo Oficial {usuario}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    # Botão para voltar à tela de Oficial
    botao_voltar_oficial = ctk.CTkButton(frame_relatorio_oficial, text="Voltar à Tela de Oficial", command=lambda: mostrar_tela_oficial(usuario,faccao, mostrar_relatorio_oficial, mostrar_relatorio_lider), width=400, height=40)
    botao_voltar_oficial.pack(pady=10)
    botao_voltar_login = ctk.CTkButton(frame_relatorio_oficial, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)
    
    return frame_relatorio_oficial