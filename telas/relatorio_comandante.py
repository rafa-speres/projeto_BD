import customtkinter as ctk

def criar_relatorio_comandante(app, mostrar_tela_inicial, usuario, faccao, mostrar_tela_comandante, mostrar_relatorio_comandante, mostrar_relatorio_lider):
    frame_relatorio_comandante = ctk.CTkScrollableFrame(app, width=1400, height=800)
    # Bem-vindo 
    label_oficial = ctk.CTkLabel(frame_relatorio_comandante, text=f"Bem-vindo Comandante {usuario}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    
    # Botão para voltar à tela de Comandante
    botao_voltar_comandante = ctk.CTkButton(frame_relatorio_comandante, text="Voltar à Tela de Comandante", command=lambda: mostrar_tela_comandante(usuario, faccao, mostrar_relatorio_comandante, mostrar_relatorio_lider), width=400, height=40)
    botao_voltar_comandante.pack(pady=10)
    botao_voltar_login = ctk.CTkButton(frame_relatorio_comandante, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)

    
    return frame_relatorio_comandante