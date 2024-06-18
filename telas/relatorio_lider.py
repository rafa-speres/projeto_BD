import customtkinter as ctk
from database import conectar_bd

def relatorio_comunidades(usuario, frame):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT agrupamento AS COMUNIDADE, especie, total_habitantes FROM TABLE(relatorio_lider_faccao(p_lider_id => '{usuario}'))")
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

def relatorio_comunidades_por_especie(usuario, frame):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT agrupamento AS ESPECIE, qtd_comunidades, total_habitantes FROM TABLE(relatorio_lider_faccao(p_lider_id => '{usuario}', p_agrupamento => 'ESPECIE'))")
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

def relatorio_comunidades_por_planeta(usuario, frame):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT agrupamento AS PLANETA, qtd_comunidades, total_habitantes FROM TABLE(relatorio_lider_faccao(p_lider_id => '{usuario}', p_agrupamento => 'PLANETA'))")
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
                    
def relatorio_comunidades_por_sistema(usuario, frame):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT agrupamento AS SISTEMA, qtd_comunidades, total_habitantes FROM TABLE(relatorio_lider_faccao(p_lider_id => '{usuario}', p_agrupamento => 'SISTEMA'))")
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
                    
def relatorio_comunidades_por_nacao(usuario, frame):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT agrupamento AS NACAO, qtd_comunidades, total_habitantes FROM TABLE(relatorio_lider_faccao(p_lider_id => '{usuario}', p_agrupamento => 'NACAO'))")
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

def criar_relatorio_lider(app, mostrar_tela_inicial, mostrar_tela_cientista, mostrar_tela_comandante, mostrar_tela_oficial, usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_comandante, mostrar_relatorio_oficial, mostrar_relatorio_lider, tipo_usuario):
    
    frame_relatorio_lider = ctk.CTkScrollableFrame(app, width=1400, height=800)
    # Bem-vindo 
    label_lider = ctk.CTkLabel(frame_relatorio_lider, text=f"Bem-vindo Líder {usuario}, da faccao {faccao}", font=("Arial", 20))
    label_lider.pack(pady=10)
    
    #Relatorio comunidades
    label_relatorio_comunidades = ctk.CTkLabel(frame_relatorio_lider, text="Relatório de comunidades da faccao", font=("Arial", 20))
    label_relatorio_comunidades.pack(pady=10)
    relatorio_comunidades(usuario, frame_relatorio_lider)
    linha_horizontal0 = ctk.CTkFrame(frame_relatorio_lider, height=2, width=1400, fg_color="gray")
    linha_horizontal0.pack(pady=20)
    
    #Relatorio comunidades por especie
    label_relatorio_comunidades_por_especie = ctk.CTkLabel(frame_relatorio_lider, text="Relatório de comunidades da facção por espécie", font=("Arial", 20))
    label_relatorio_comunidades_por_especie.pack(pady=10)
    relatorio_comunidades_por_especie(usuario, frame_relatorio_lider)
    linha_horizontal1 = ctk.CTkFrame(frame_relatorio_lider, height=2, width=1400, fg_color="gray")
    linha_horizontal1.pack(pady=20)
    
    #Relatorio comunidades por planeta
    label_relatorio_comunidades_por_planeta = ctk.CTkLabel(frame_relatorio_lider, text="Relatório de comunidades da facção por planeta", font=("Arial", 20))
    label_relatorio_comunidades_por_planeta.pack(pady=10)
    relatorio_comunidades_por_planeta(usuario, frame_relatorio_lider)
    linha_horizontal2 = ctk.CTkFrame(frame_relatorio_lider, height=2, width=1400, fg_color="gray")
    linha_horizontal2.pack(pady=20)
    
    #Relatorio comunidades por sistema
    label_relatorio_comunidades_por_sistema = ctk.CTkLabel(frame_relatorio_lider, text="Relatório de comunidades da facção por sistema", font=("Arial", 20))
    label_relatorio_comunidades_por_sistema.pack(pady=10)
    relatorio_comunidades_por_sistema(usuario, frame_relatorio_lider)
    linha_horizontal3 = ctk.CTkFrame(frame_relatorio_lider, height=2, width=1400, fg_color="gray")
    linha_horizontal3.pack(pady=20)
    
    #Relatorio comunidades por nacao
    label_relatorio_comunidades_por_nacao = ctk.CTkLabel(frame_relatorio_lider, text="Relatório de comunidades da facção por nação", font=("Arial", 20))
    label_relatorio_comunidades_por_nacao.pack(pady=10)
    relatorio_comunidades_por_nacao(usuario, frame_relatorio_lider)
    linha_horizontal4 = ctk.CTkFrame(frame_relatorio_lider, height=2, width=1400, fg_color="gray")
    linha_horizontal4.pack(pady=20)
    
    if tipo_usuario == "oficial":
        botao_voltar_oficial = ctk.CTkButton(frame_relatorio_lider, text="Voltar à Tela de Oficial", command=lambda: mostrar_tela_oficial(usuario, faccao, mostrar_relatorio_oficial, mostrar_relatorio_lider), width=400, height=40)
        botao_voltar_oficial.pack(pady=10)
    elif tipo_usuario == "comandante":
        botao_voltar_comandante = ctk.CTkButton(frame_relatorio_lider, text="Voltar à Tela de Comandante", command=lambda: mostrar_tela_comandante(usuario, faccao, mostrar_relatorio_comandante, mostrar_relatorio_lider), width=400, height=40)
        botao_voltar_comandante.pack(pady=10)
    elif tipo_usuario == "cientista":
        botao_voltar_cientista = ctk.CTkButton(frame_relatorio_lider, text="Voltar à Tela de Cientista", command=lambda: mostrar_tela_cientista(usuario, faccao, mostrar_relatorio_cientista, mostrar_relatorio_cientista), width=400, height=40)
        botao_voltar_cientista.pack(pady=10)

    botao_voltar_login = ctk.CTkButton(frame_relatorio_lider, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)
    
    return frame_relatorio_lider