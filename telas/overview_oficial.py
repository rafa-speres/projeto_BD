import customtkinter as ctk

def criar_overview_oficial(app, mostrar_tela_inicial):
    frame_overview_oficial = ctk.CTkFrame(app)
    label_oficial = ctk.CTkLabel(frame_overview_oficial, text="Bem-vindo Oficial", font=("Arial", 24))
    label_oficial.pack(pady=20)
    botao_voltar = ctk.CTkButton(frame_overview_oficial, text="Voltar", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar.pack(pady=10)
    return frame_overview_oficial