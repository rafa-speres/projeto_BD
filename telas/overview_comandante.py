import customtkinter as ctk

def criar_overview_comandante(app, mostrar_tela_inicial):
    frame_tela_comandante = ctk.CTkFrame(app)
    label_comandante = ctk.CTkLabel(frame_tela_comandante, text="Bem-vindo Comandante", font=("Arial", 24))
    label_comandante.pack(pady=20)
    botao_voltar = ctk.CTkButton(frame_tela_comandante, text="Voltar", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar.pack(pady=10)
    return frame_tela_comandante