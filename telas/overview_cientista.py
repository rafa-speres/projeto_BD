import customtkinter as ctk

def criar_overview_cientista(app, mostrar_tela_inicial):
    frame_overview_cientista = ctk.CTkFrame(app)
    label_cientista = ctk.CTkLabel(frame_overview_cientista, text="Bem-vindo Cientista", font=("Arial", 24))
    label_cientista.pack(pady=20)
    botao_voltar = ctk.CTkButton(frame_overview_cientista, text="Voltar", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar.pack(pady=10)
    return frame_overview_cientista