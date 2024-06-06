import customtkinter as ctk
from tkinter import messagebox
from database import cadastrar_usuario_bd

def cadastrar_usuario(entry_cadastro_usuario, entry_cadastro_senha, dropdown_tipo_usuario):
    usuario = entry_cadastro_usuario.get()
    senha = entry_cadastro_senha.get()
    tipo_usuario = dropdown_tipo_usuario.get()
    if usuario and senha and tipo_usuario:
        try:
            cadastrar_usuario_bd(usuario, senha, tipo_usuario)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

def criar_tela_cadastro(app, mostrar_tela_inicial):
    frame_tela_cadastro = ctk.CTkFrame(app)
    label_cadastro_usuario = ctk.CTkLabel(frame_tela_cadastro, text="Usuário:", font=("Arial", 14))
    label_cadastro_usuario.pack(pady=5)
    entry_cadastro_usuario = ctk.CTkEntry(frame_tela_cadastro, width=300, height=30)
    entry_cadastro_usuario.pack(pady=5)

    label_cadastro_senha = ctk.CTkLabel(frame_tela_cadastro, text="Senha:", font=("Arial", 14))
    label_cadastro_senha.pack(pady=5)
    entry_cadastro_senha = ctk.CTkEntry(frame_tela_cadastro, show="*", width=300, height=30)
    entry_cadastro_senha.pack(pady=5)

    label_tipo_usuario = ctk.CTkLabel(frame_tela_cadastro, text="Tipo de Usuário:", font=("Arial", 14))
    label_tipo_usuario.pack(pady=5)
    dropdown_tipo_usuario = ctk.CTkOptionMenu(frame_tela_cadastro, values=["Líder de Facção", "Cientista", "Comandante", "Oficial"], width=300, height=30)
    dropdown_tipo_usuario.pack(pady=5)

    botao_cadastrar = ctk.CTkButton(frame_tela_cadastro, text="Cadastrar", command=lambda: cadastrar_usuario(entry_cadastro_usuario, entry_cadastro_senha, dropdown_tipo_usuario), width=200, height=40)
    botao_cadastrar.pack(pady=20)
    botao_voltar_cadastro = ctk.CTkButton(frame_tela_cadastro, text="Voltar", command=mostrar_tela_inicial, width=200, height=40)
    botao_voltar_cadastro.pack(pady=10)

    return frame_tela_cadastro
