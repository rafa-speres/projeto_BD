import customtkinter as ctk
from telas.login import criar_tela_login
from telas.overview_cientista import criar_overview_cientista
from telas.overview_comandante import criar_overview_comandante
from telas.overview_oficial import criar_overview_oficial

ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("green")  # Tema de cor

# Função para mostrar a tela inicial
#def mostrar_tela_inicial():
#   esconder_todas_as_telas()
#    frame_tela_inicial.pack(pady=20)

# Função para mostrar a tela de cadastro
#def mostrar_tela_cadastro():
#    esconder_todas_as_telas()
#    frame_tela_cadastro.pack(pady=20)

# Função para mostrar a tela de login
def mostrar_tela_login():
    esconder_todas_as_telas()
    frame_tela_login.pack(pady=20)

# Função para mostrar a tela de cientista
def mostrar_tela_cientista(usuario):
    esconder_todas_as_telas()
    frame_tela_cientista = criar_overview_cientista(app, mostrar_tela_login, usuario)
    frame_tela_cientista.pack(pady=20)

# Função para mostrar a tela de comandante
def mostrar_tela_comandante(usuario):
    esconder_todas_as_telas()
    frame_tela_comandante = criar_overview_comandante(app, mostrar_tela_login, usuario)
    frame_tela_comandante.pack(pady=20)

# Função para mostrar a tela de oficial
def mostrar_tela_oficial(usuario):
    esconder_todas_as_telas()
    frame_tela_oficial = criar_overview_oficial(app, mostrar_tela_login, usuario)
    frame_tela_oficial.pack(pady=20)

# Função para esconder todas as telas
def esconder_todas_as_telas():
    frame_tela_login.pack_forget()
    frame_tela_cientista.pack_forget()
    frame_tela_comandante.pack_forget()
    frame_tela_oficial.pack_forget()

# Criação da janela principal
app = ctk.CTk()
app.title("Sistema de Cadastro e Login")
app.geometry("1000x600")  # Aumenta o tamanho da janela principal

# Criação das telas
#frame_tela_inicial = criar_tela_inicial(app, mostrar_tela_cadastro, mostrar_tela_login)
#frame_tela_cadastro = criar_tela_cadastro(app, mostrar_tela_inicial)
frame_tela_login = criar_tela_login(app, mostrar_tela_cientista, mostrar_tela_comandante, mostrar_tela_oficial)
frame_tela_cientista = criar_overview_cientista(app, mostrar_tela_login)
frame_tela_comandante = criar_overview_comandante(app, mostrar_tela_login)
frame_tela_oficial = criar_overview_oficial(app, mostrar_tela_login)

# Mostrar a tela inicial ao iniciar o aplicativo
mostrar_tela_login()
#
# Execução da aplicação
app.mainloop()