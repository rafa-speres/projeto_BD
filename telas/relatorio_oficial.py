import customtkinter as ctk
from database import conectar_bd
from tkinter import messagebox


def relatorio_comunidades_oficial(usuario, frame):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT agrupamento as COMUNIDADE, total_habitantes, data_ini as DATA_INICIO, data_fim FROM TABLE(pkg_oficial.relatorio_oficial('{usuario}'))")
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
    
def relatorio_comunidades_oficial_faccao(usuario, frame):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT agrupamento as FACCAO, qtd_comunidades, total_habitantes FROM TABLE(pkg_oficial.relatorio_oficial('{usuario}', 'FACCAO'))")
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
    
def relatorio_comunidades_oficial_especie(usuario, frame):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT agrupamento as ESPECIE, qtd_comunidades, total_habitantes FROM TABLE(pkg_oficial.relatorio_oficial('{usuario}', 'ESPECIE'))")
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
    
def relatorio_comunidades_oficial_planeta(usuario, frame):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT agrupamento as PLANETA, qtd_comunidades, total_habitantes FROM TABLE(pkg_oficial.relatorio_oficial('{usuario}', 'PLANETA'))")
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
    
def relatorio_comunidades_oficial_sistema(usuario, frame):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT agrupamento as SISTEMA, qtd_comunidades, total_habitantes FROM TABLE(pkg_oficial.relatorio_oficial('{usuario}', 'SISTEMA'))")
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
    
def recolhe_nacao_oficial(usuario):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT NACAO FROM LIDER WHERE CPI = :1", [usuario])
    result = cursor.fetchone()
    if result:
            nacao = result[0]
            return nacao
    else:
        messagebox.showerror("Erro", "Oficial nao tem nacao")  
        
    

def criar_relatorio_oficial(app, mostrar_tela_inicial, usuario, faccao, mostrar_tela_oficial, mostrar_relatorio_oficial, mostrar_relatorio_lider, tipo_usuario):
    frame_relatorio_oficial = ctk.CTkScrollableFrame(app, width=1400, height=800)
    nacao = recolhe_nacao_oficial(usuario)
    # Bem-vindo
    label_oficial = ctk.CTkLabel(frame_relatorio_oficial, text=f"Bem-vindo Oficial {usuario}, da nação {nacao}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    #Relatorio de habitantes da própria nação
    label_relatorio_ = ctk.CTkLabel(frame_relatorio_oficial, text="Relatorio de habitantes da própria nação", font=("Arial", 20))
    label_relatorio_.pack(pady=10)
    relatorio_comunidades_oficial(usuario, frame_relatorio_oficial)
    linha_horizontal0 = ctk.CTkFrame(frame_relatorio_oficial, height=2, width=1400, fg_color="gray")
    linha_horizontal0.pack(pady=20)
    
    #Relatorio de habitantes da própria nação agrupado por faccao
    label_relatorio_ = ctk.CTkLabel(frame_relatorio_oficial, text="Relatorio de habitantes da própria nação agrupado por faccao", font=("Arial", 20))
    label_relatorio_.pack(pady=10)
    relatorio_comunidades_oficial_faccao(usuario, frame_relatorio_oficial)
    linha_horizontal1 = ctk.CTkFrame(frame_relatorio_oficial, height=2, width=1400, fg_color="gray")
    linha_horizontal1.pack(pady=20)
    
    #Relatorio de habitantes da própria nação agrupado por especie
    label_relatorio_ = ctk.CTkLabel(frame_relatorio_oficial, text="Relatorio de habitantes da própria nação agrupado por especie", font=("Arial", 20))
    label_relatorio_.pack(pady=10)
    relatorio_comunidades_oficial_especie(usuario, frame_relatorio_oficial)
    linha_horizontal2 = ctk.CTkFrame(frame_relatorio_oficial, height=2, width=1400, fg_color="gray")
    linha_horizontal2.pack(pady=20)
    
    #Relatorio de habitantes da própria nação agrupado por planeta
    label_relatorio_ = ctk.CTkLabel(frame_relatorio_oficial, text="Relatorio de habitantes da própria nação agrupado por planeta", font=("Arial", 20))
    label_relatorio_.pack(pady=10)
    relatorio_comunidades_oficial_planeta(usuario, frame_relatorio_oficial)
    linha_horizontal3 = ctk.CTkFrame(frame_relatorio_oficial, height=2, width=1400, fg_color="gray")
    linha_horizontal3.pack(pady=20)
    
    #Relatorio de habitantes da própria nação agrupado por sistema
    label_relatorio_ = ctk.CTkLabel(frame_relatorio_oficial, text="Relatorio de habitantes da própria nação agrupado por sistema", font=("Arial", 20))
    label_relatorio_.pack(pady=10)
    relatorio_comunidades_oficial_sistema(usuario, frame_relatorio_oficial)
    linha_horizontal4 = ctk.CTkFrame(frame_relatorio_oficial, height=2, width=1400, fg_color="gray")
    linha_horizontal4.pack(pady=20)
    
    # Botão para voltar à tela de Oficial
    botao_voltar_oficial = ctk.CTkButton(frame_relatorio_oficial, text="Voltar à Tela de Oficial", command=lambda: mostrar_tela_oficial(usuario,faccao, mostrar_relatorio_oficial, mostrar_relatorio_lider), width=400, height=40)
    botao_voltar_oficial.pack(pady=10)
    botao_voltar_login = ctk.CTkButton(frame_relatorio_oficial, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)
    
    return frame_relatorio_oficial