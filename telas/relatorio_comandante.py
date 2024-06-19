import customtkinter as ctk
from database import conectar_bd

def relatorio_comandante(usuario, frame):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"""
                BEGIN
                    pkg_comandante.relatorio_planetas_dominados(p_comandante_id => '{usuario}');
                END;
            """)
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
    
def relatorio_comandante_distancia(usuario, frame, distancia):
    if usuario:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"""
                BEGIN
                    pkg_comandante.relatorio_planetas_potenciais(p_comandante_id => '{usuario}', p_distancia_maxima => {distancia});
                END;
            """)
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


def criar_relatorio_comandante(app, mostrar_tela_inicial, usuario, faccao, mostrar_tela_comandante, mostrar_relatorio_comandante, mostrar_relatorio_lider, tipo_usuario, distancia):
    
    frame_relatorio_comandante = ctk.CTkScrollableFrame(app, width=1400, height=800)
    # Bem-vindo 
    label_oficial = ctk.CTkLabel(frame_relatorio_comandante, text=f"Bem-vindo Comandante {usuario}", font=("Arial", 20))
    label_oficial.pack(pady=10)
    
    if distancia == "":
        #Relatorio comandante
        label_relatorio_comandante = ctk.CTkLabel(frame_relatorio_comandante, text="Relatório de planetas dominados", font=("Arial", 20))
        label_relatorio_comandante.pack(pady=10)
        relatorio_comandante(usuario, frame_relatorio_comandante)
        linha_horizontal0 = ctk.CTkFrame(frame_relatorio_comandante, height=2, width=1400, fg_color="gray")
        linha_horizontal0.pack(pady=20)
    
    else:  
        #Relatorio comandante
        label_relatorio_comandante_distancia = ctk.CTkLabel(frame_relatorio_comandante, text="Relatório de planetas potenciais", font=("Arial", 20))
        label_relatorio_comandante_distancia.pack(pady=10)
        relatorio_comandante_distancia(usuario, frame_relatorio_comandante, distancia)

    
    # Botão para voltar à tela de Comandante
    botao_voltar_comandante = ctk.CTkButton(frame_relatorio_comandante, text="Voltar à Tela de Comandante", command=lambda: mostrar_tela_comandante(usuario, faccao, mostrar_relatorio_comandante, mostrar_relatorio_lider), width=400, height=40)
    botao_voltar_comandante.pack(pady=10)
    botao_voltar_login = ctk.CTkButton(frame_relatorio_comandante, text="Voltar à Tela de Login", command=mostrar_tela_inicial, width=400, height=40)
    botao_voltar_login.pack(pady=10)

    
    return frame_relatorio_comandante