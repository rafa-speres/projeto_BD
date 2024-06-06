import customtkinter as ctk
from tkinter import messagebox
from database import conectar_bd

def login_usuario(entry_login_usuario, entry_login_senha, app, mostrar_tela_lider, mostrar_tela_cientista, mostrar_tela_comandante, mostrar_tela_oficial):
    usuario = entry_login_usuario.get()
    senha = entry_login_senha.get()

    if usuario and senha:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT TIPO_USUARIO FROM USERS WHERE USUARIO = :usuario AND SENHA = :senha", [usuario, senha])
        result = cursor.fetchone()

        if result:
            tipo_usuario = result[0]
            if tipo_usuario == "Líder de Facção":
                mostrar_tela_lider()
            elif tipo_usuario == "Cientista":
                mostrar_tela_cientista()
            elif tipo_usuario == "Comandante":
                mostrar_tela_comandante()
            elif tipo_usuario == "Oficial":
                mostrar_tela_oficial()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
        cursor.close()
        conn.close()
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

def criar_tela_login(app, mostrar_tela_inicial, mostrar_tela_lider, mostrar_tela_cientista, mostrar_tela_comandante, mostrar_tela_oficial):
    frame_tela_login = ctk.CTkFrame(app)
    label_login_usuario = ctk.CTkLabel(frame_tela_login, text="Usuário:", font=("Arial", 14))
    label_login_usuario.pack(pady=5)
    entry_login_usuario = ctk.CTkEntry(frame_tela_login, width=500, height=30)
    entry_login_usuario.pack(pady=5)

    label_login_senha = ctk.CTkLabel(frame_tela_login, text="Senha:", font=("Arial", 14))
    label_login_senha.pack(pady=5)
    entry_login_senha = ctk.CTkEntry(frame_tela_login, show="*", width=500, height=30)
    entry_login_senha.pack(pady=5)

    botao_login = ctk.CTkButton(frame_tela_login, text="Login", command=lambda: login_usuario(entry_login_usuario, entry_login_senha, app, mostrar_tela_lider, mostrar_tela_cientista, mostrar_tela_comandante, mostrar_tela_oficial), width=400, height=40)
    botao_login.pack(pady=20)
    botao_voltar_login = ctk.CTkButton(frame_tela_login, text="Voltar", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)

    return frame_tela_login