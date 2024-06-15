import customtkinter as ctk
from tkinter import messagebox
from database import conectar_bd

def login_usuario(entry_login_usuario, entry_login_senha, app, mostrar_tela_cientista, mostrar_tela_comandante, mostrar_tela_oficial, mostrar_relatorio_cientista, mostrar_relatorio_comandante, mostrar_relatorio_oficial, mostrar_relatorio_lider):
    usuario = entry_login_usuario.get()
    senha = entry_login_senha.get()

    if usuario and senha:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM USERS WHERE ID_LIDER = '{usuario}' AND PASSWORD = STANDARD_HASH('{senha}', 'MD5')")
        result = cursor.fetchone()

        if result:
            cursor.execute(f"SELECT CARGO FROM LIDER WHERE CPI = '{usuario}'")
            result_2 = cursor.fetchone()
            tipo_usuario = result_2[0]
            
            cursor.execute(f"SELECT NOME FROM FACCAO WHERE LIDER = '{usuario}'")
            result_3 = cursor.fetchone()
            if "CIENTISTA" in tipo_usuario:
                if result_3:
                    faccao = result_3[0]
                    mostrar_tela_cientista(usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_lider)
                else:
                    faccao = 0
                    mostrar_tela_cientista(usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_lider)
            elif "COMANDANTE" in tipo_usuario:
                if result_3:
                    faccao = result_3[0]
                    mostrar_tela_comandante(usuario, faccao, mostrar_relatorio_comandante, mostrar_relatorio_lider)
                else:
                    faccao = 0
                    mostrar_tela_comandante(usuario, faccao, mostrar_relatorio_comandante, mostrar_relatorio_lider)
            elif "OFICIAL" in tipo_usuario:
                if result_3:
                    faccao = result_3[0]
                    mostrar_tela_oficial(usuario, faccao, mostrar_relatorio_oficial, mostrar_relatorio_lider)
                else:
                    faccao = 0
                    mostrar_tela_oficial(usuario, faccao, mostrar_relatorio_oficial, mostrar_relatorio_lider)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
        cursor.close()
        conn.close()
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

def criar_tela_login(app, mostrar_tela_cientista, mostrar_tela_comandante, mostrar_tela_oficial, mostrar_relatorio_cientista, mostrar_relatorio_comandante, mostrar_relatorio_oficial, mostrar_relatorio_lider):
    frame_tela_login = ctk.CTkFrame(app)
    label_login_usuario = ctk.CTkLabel(frame_tela_login, text="Usuário:", font=("Arial", 14))
    label_login_usuario.pack(pady=5)
    entry_login_usuario = ctk.CTkEntry(frame_tela_login, width=500, height=30)
    entry_login_usuario.pack(pady=5)

    label_login_senha = ctk.CTkLabel(frame_tela_login, text="Senha:", font=("Arial", 14))
    label_login_senha.pack(pady=5)
    entry_login_senha = ctk.CTkEntry(frame_tela_login, show="*", width=500, height=30)
    entry_login_senha.pack(pady=5)

    botao_login = ctk.CTkButton(frame_tela_login, text="Login", command=lambda: login_usuario(entry_login_usuario, entry_login_senha, app, mostrar_tela_cientista, mostrar_tela_comandante, mostrar_tela_oficial, mostrar_relatorio_cientista, mostrar_relatorio_comandante, mostrar_relatorio_oficial, mostrar_relatorio_lider), width=400, height=40)
    botao_login.pack(pady=20)

    return frame_tela_login