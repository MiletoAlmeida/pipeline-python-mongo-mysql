import os
from dotenv import load_dotenv
import mysql.connector
import pandas as pd

def connect_mysql():
    load_dotenv()
    mysql_password = os.getenv("MYSQL_PASSWORD")
    cnx = mysql.connector.connect(
        host="localhost",
        user="mirtilo",
        password=mysql_password
    )
    return cnx

def create_database_and_table(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS dbprodutos;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dbprodutos.tb_livros(
            id VARCHAR(100),
            Produto VARCHAR(100),
            Categoria_Produto VARCHAR(100),
            Preco FLOAT(10,2),
            Frete FLOAT(10,2),
            Data_Compra DATE,
            Vendedor VARCHAR(100),
            Local_Compra VARCHAR(100),
            Avaliacao_Compra INT,
            Tipo_Pagamento VARCHAR(100),
            Qntd_Parcelas INT,
            Latitude FLOAT(10,2),
            Longitude FLOAT(10,2),
            PRIMARY KEY (id)
        );
    """)
    cursor.execute("USE dbprodutos;")

def insert_data(cursor, df):
    lista_dados = [tuple(row) for _, row in df.iterrows()]
    sql = """
        INSERT INTO tb_livros 
        (id, Produto, Categoria_Produto, Preco, Frete, Data_Compra, Vendedor, Local_Compra, Avaliacao_Compra, Tipo_Pagamento, Qntd_Parcelas, Latitude, Longitude)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
            Produto=VALUES(Produto),
            Categoria_Produto=VALUES(Categoria_Produto),
            Preco=VALUES(Preco),
            Frete=VALUES(Frete),
            Data_Compra=VALUES(Data_Compra),
            Vendedor=VALUES(Vendedor),
            Local_Compra=VALUES(Local_Compra),
            Avaliacao_Compra=VALUES(Avaliacao_Compra),
            Tipo_Pagamento=VALUES(Tipo_Pagamento),
            Qntd_Parcelas=VALUES(Qntd_Parcelas),
            Latitude=VALUES(Latitude),
            Longitude=VALUES(Longitude);
    """
    cursor.executemany(sql, lista_dados)

def main():
    # Carrega dados do CSV
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data_python', 'tabela_livros.csv')
    df_livros = pd.read_csv(data_path)

    # Conecta ao MySQL
    cnx = connect_mysql()
    cursor = cnx.cursor()

    # Cria base e tabela
    create_database_and_table(cursor)

    # Insere dados
    insert_data(cursor, df_livros)
    cnx.commit()
    print(f"{cursor.rowcount} registros inseridos/atualizados em tb_livros.")

    # Visualiza os dados inseridos
    cursor.execute("SELECT * FROM tb_livros;")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    cnx.close()

if __name__ == "__main__":
    main()