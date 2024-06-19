import customtkinter as ctk
from database import conectar_bd

def read_estrela(frame, estrela):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM TABLE(PACOTE_CIENTISTA.ler_estrela('{estrela}'))")
    result = cursor.fetchall()
    if result:
        colunas = [col[0] for col in cursor.description]
        
        # Criando uma subframe para usar grid
        subframe = ctk.CTkFrame(frame)
        subframe.pack(pady=10)
        
        for col_num, col_name in enumerate(colunas):
            header_geral = ctk.CTkLabel(subframe, text=col_name, font=("Arial", 12, "bold"))
            header_geral.grid(row=0, column=col_num, padx=5, pady=5)
        
        for row_num, row_data in enumerate(result, start=1):
            for col_num, cell_data in enumerate(row_data):
                cell = ctk.CTkLabel(subframe, text=cell_data, font=("Arial", 12))
                cell.grid(row=row_num, column=col_num, padx=5, pady=5)
    cursor.close()
    conn.close()


def relatorio_estrelas(frame):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM TABLE(PACOTE_CIENTISTA.obterEstrelas)")
    result = cursor.fetchall()
    if result:
        colunas = [col[0] for col in cursor.description]
        
        # Criando uma subframe para usar grid
        subframe = ctk.CTkFrame(frame)
        subframe.pack(pady=10)
        
        for col_num, col_name in enumerate(colunas):
            header_geral = ctk.CTkLabel(subframe, text=col_name, font=("Arial", 12, "bold"))
            header_geral.grid(row=0, column=col_num, padx=5, pady=5)
        
        for row_num, row_data in enumerate(result, start=1):
            for col_num, cell_data in enumerate(row_data):
                cell = ctk.CTkLabel(subframe, text=cell_data, font=("Arial", 12))
                cell.grid(row=row_num, column=col_num, padx=5, pady=5)
    cursor.close()
    conn.close()

def relatorio_planetas(frame):

    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM TABLE(PACOTE_CIENTISTA.obterPlanetas)")
    result = cursor.fetchall()
    if result:
        colunas = [col[0] for col in cursor.description]
        
        # Criando uma subframe para usar grid
        subframe = ctk.CTkFrame(frame)
        subframe.pack(pady=10)
        
        for col_num, col_name in enumerate(colunas):
            header_geral = ctk.CTkLabel(subframe, text=col_name, font=("Arial", 12, "bold"))
            header_geral.grid(row=0, column=col_num, padx=5, pady=5)
        
        for row_num, row_data in enumerate(result, start=1):
            for col_num, cell_data in enumerate(row_data):
                cell = ctk.CTkLabel(subframe, text=cell_data, font=("Arial", 12))
                cell.grid(row=row_num, column=col_num, padx=5, pady=5)
    
    cursor.close()
    conn.close()

def relatorio_sistemas(frame):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM TABLE(PACOTE_CIENTISTA.obterSistemas)")
    result = cursor.fetchall()
    if result:
        colunas = [col[0] for col in cursor.description]
        
        # Criando uma subframe para usar grid
        subframe = ctk.CTkFrame(frame)
        subframe.pack(pady=10)
        
        for col_num, col_name in enumerate(colunas):
            header_geral = ctk.CTkLabel(subframe, text=col_name, font=("Arial", 12, "bold"))
            header_geral.grid(row=0, column=col_num, padx=5, pady=5)
        
        for row_num, row_data in enumerate(result, start=1):
            for col_num, cell_data in enumerate(row_data):
                cell = ctk.CTkLabel(subframe, text=cell_data, font=("Arial", 12))
                cell.grid(row=row_num, column=col_num, padx=5, pady=5)
                    
    cursor.close()
    conn.close()


def criar_relatorio_cientista(app, mostrar_tela_inicial, usuario, faccao, mostrar_tela_cientista, mostrar_relatorio_cientista, mostrar_relatorio_lider, tipo_usuario, id_estrela):
    frame_relatorio_cientista = ctk.CTkScrollableFrame(app, width=1400, height=800)
    # Bem-vindo 
    label_oficial = ctk.CTkLabel(frame_relatorio_cientista, text=f"Bem-vindo Cientista {usuario}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    if(id_estrela == ""):
        #Relatorio Estrelas
        label_relatorio_estrelas = ctk.CTkLabel(frame_relatorio_cientista, text="Relatório de estrelas com massa nula", font=("Arial", 20))
        label_relatorio_estrelas.pack(pady=10)
        relatorio_estrelas(frame_relatorio_cientista)
        linha_horizontal0 = ctk.CTkFrame(frame_relatorio_cientista, height=2, width=1400, fg_color="gray")
        linha_horizontal0.pack(pady=20)
        
        #Relatorio planetas
        label_relatorio_planetas = ctk.CTkLabel(frame_relatorio_cientista, text="Relatório de planetas com massa nula", font=("Arial", 20))
        label_relatorio_planetas.pack(pady=10)
        relatorio_planetas(frame_relatorio_cientista)
        linha_horizontal1 = ctk.CTkFrame(frame_relatorio_cientista, height=2, width=1400, fg_color="gray")
        linha_horizontal1.pack(pady=20)
        
        #Relatorio Sistemas
        label_relatorio_sistemas = ctk.CTkLabel(frame_relatorio_cientista, text="Relatório de sistemas com nome nulo", font=("Arial", 20))
        label_relatorio_sistemas.pack(pady=10)
        relatorio_sistemas(frame_relatorio_cientista)
        linha_horizontal2 = ctk.CTkFrame(frame_relatorio_cientista, height=2, width=1400, fg_color="gray")
        linha_horizontal2.pack(pady=20)
        
        # Botão para voltar à tela de Cientista
        botao_voltar_cientista = ctk.CTkButton(frame_relatorio_cientista, text="Voltar à Tela de Cientista", command=lambda: mostrar_tela_cientista(usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_cientista), width=400, height=40)
        botao_voltar_cientista.pack(pady=10)
        botao_voltar_login = ctk.CTkButton(frame_relatorio_cientista, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
        botao_voltar_login.pack(pady=10)
    
    else:
        #Relatorio Estrela (CRUD)
        label_relatorio_estrela = ctk.CTkLabel(frame_relatorio_cientista, text="Relatório da estrela", font=("Arial", 20))
        label_relatorio_estrela.pack(pady=10)
        read_estrela(frame_relatorio_cientista, id_estrela)
        
        # Botão para voltar à tela de Cientista
        botao_voltar_cientista = ctk.CTkButton(frame_relatorio_cientista, text="Voltar à Tela de Cientista", command=lambda: mostrar_tela_cientista(usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_cientista), width=400, height=40)
        botao_voltar_cientista.pack(pady=10)
        botao_voltar_login = ctk.CTkButton(frame_relatorio_cientista, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
        botao_voltar_login.pack(pady=10)

    
    return frame_relatorio_cientista