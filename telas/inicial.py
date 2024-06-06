import customtkinter as ctk

def criar_tela_inicial(app, mostrar_tela_cadastro, mostrar_tela_login):
    frame_tela_inicial = ctk.CTkFrame(app)
    label_bem_vindo = ctk.CTkLabel(frame_tela_inicial, text="Bem-vindo!", font=("Arial", 24))
    label_bem_vindo.pack(pady=20)
    botao_ir_cadastro = ctk.CTkButton(frame_tela_inicial, text="Cadastrar", command=mostrar_tela_cadastro, width=400, height=40)
    botao_ir_cadastro.pack(pady=10)
    botao_ir_login = ctk.CTkButton(frame_tela_inicial, text="Login", command=mostrar_tela_login, width=400, height=40)
    botao_ir_login.pack(pady=10)
    return frame_tela_inicial
