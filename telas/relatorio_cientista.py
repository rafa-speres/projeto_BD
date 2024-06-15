import customtkinter as ctk

def criar_relatorio_cientista(app, mostrar_tela_inicial, usuario, faccao, mostrar_tela_cientista, mostrar_relatorio_cientista, mostrar_relatorio_lider):
    frame_relatorio_cientista = ctk.CTkScrollableFrame(app, width=1400, height=800)
    # Bem-vindo 
    label_oficial = ctk.CTkLabel(frame_relatorio_cientista, text=f"Bem-vindo Cientista {usuario}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    
    # Botão para voltar à tela de Cientista
    botao_voltar_cientista = ctk.CTkButton(frame_relatorio_cientista, text="Voltar à Tela de Cientista", command=lambda: mostrar_tela_cientista(usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_cientista), width=400, height=40)
    botao_voltar_cientista.pack(pady=10)
    botao_voltar_login = ctk.CTkButton(frame_relatorio_cientista, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)
    
    return frame_relatorio_cientista