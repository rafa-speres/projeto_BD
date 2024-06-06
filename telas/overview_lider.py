import customtkinter as ctk

def criar_overview_lider(app, mostrar_tela_inicial):
    frame_overview_lider = ctk.CTkFrame(app)
    label_lider = ctk.CTkLabel(frame_overview_lider, text="Bem-vindo Líder de Facção", font=("Arial", 24))
    label_lider.pack(pady=20)
    botao_voltar = ctk.CTkButton(frame_overview_lider, text="Voltar", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar.pack(pady=10)
    return frame_overview_lider