import customtkinter as ctk
from tkinter import messagebox
from database import conectar_bd
from telas.login import criar_tela_login
from telas.overview_cientista import criar_overview_cientista
from telas.overview_comandante import criar_overview_comandante
from telas.overview_oficial import criar_overview_oficial
from telas.relatorio_cientista import criar_relatorio_cientista
from telas.relatorio_comandante import criar_relatorio_comandante
from telas.relatorio_oficial import criar_relatorio_oficial
from telas.relatorio_lider import criar_relatorio_lider

ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("green")  # Tema de cor

# Função para mostrar a tela de login
def mostrar_tela_login():
    esconder_todas_as_telas()
    frame_tela_login.pack(pady=20)

# Função para mostrar a tela de cientista
def mostrar_tela_cientista(usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_lider):
    esconder_todas_as_telas()
    frame_tela_cientista = criar_overview_cientista(app, mostrar_tela_login, usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_lider, mostrar_tela_cientista)
    frame_tela_cientista.pack(pady=20)

# Função para mostrar a tela de comandante
def mostrar_tela_comandante(usuario, faccao, mostrar_relatorio_comandante, mostrar_relatorio_lider):
    esconder_todas_as_telas()
    frame_tela_comandante = criar_overview_comandante(app, mostrar_tela_login, usuario, faccao, mostrar_relatorio_comandante, mostrar_relatorio_lider, mostrar_tela_comandante)
    frame_tela_comandante.pack(pady=20)

# Função para mostrar a tela de oficial
def mostrar_tela_oficial(usuario, faccao, mostrar_relatorio_oficial, mostrar_relatorio_lider):
    esconder_todas_as_telas()
    frame_tela_oficial = criar_overview_oficial(app, mostrar_tela_login, usuario, faccao, mostrar_relatorio_oficial, mostrar_relatorio_lider, mostrar_tela_oficial)
    frame_tela_oficial.pack(pady=20)
    
def mostrar_relatorio_cientista(usuario,faccao, tipo_usuario):
    esconder_todas_as_telas()
    frame_relatorio_cientista = criar_relatorio_cientista(app, mostrar_tela_login, usuario, faccao, mostrar_tela_cientista, mostrar_relatorio_cientista, mostrar_relatorio_lider,tipo_usuario) 
    frame_relatorio_cientista.pack(pady=20)
    
def mostrar_relatorio_comandante(usuario,faccao, tipo_usuario):
    esconder_todas_as_telas()
    frame_relatorio_comandante = criar_relatorio_comandante(app, mostrar_tela_login, usuario, faccao, mostrar_tela_comandante, mostrar_relatorio_comandante, mostrar_relatorio_lider,tipo_usuario) 
    frame_relatorio_comandante.pack(pady=20)
    
def mostrar_relatorio_oficial(usuario, faccao, tipo_usuario):
    esconder_todas_as_telas()
    frame_relatorio_oficial = criar_relatorio_oficial(app, mostrar_tela_login, usuario, faccao, mostrar_tela_oficial, mostrar_relatorio_oficial, mostrar_relatorio_lider,tipo_usuario)
    frame_relatorio_oficial.pack(pady=20)
    
def mostrar_relatorio_lider(usuario, faccao, tipo_usuario):
    esconder_todas_as_telas()
    frame_relatorio_lider = criar_relatorio_lider(app, mostrar_tela_login, mostrar_tela_cientista, mostrar_tela_comandante, mostrar_tela_oficial, usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_comandante, mostrar_relatorio_oficial, mostrar_relatorio_lider, tipo_usuario)
    frame_relatorio_lider.pack(pady=20)

# Função para esconder todas as telas
def esconder_todas_as_telas():
    for widget in app.winfo_children():
        widget.pack_forget()


# Criação da janela principal
app = ctk.CTk()
app.title("Sistema de Cadastro e Login")
app.geometry("1400x800")  # Aumenta o tamanho da janela principal

# Criação da tela de login
frame_tela_login = criar_tela_login(app, mostrar_tela_cientista, mostrar_tela_comandante, mostrar_tela_oficial, mostrar_relatorio_cientista, mostrar_relatorio_comandante, mostrar_relatorio_oficial, mostrar_relatorio_lider)

# Mostrar a tela inicial ao iniciar o aplicativo
mostrar_tela_login()

# Execução da aplicação
app.mainloop()