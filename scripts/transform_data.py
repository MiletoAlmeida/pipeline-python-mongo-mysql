import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

def connect_mongo():
    load_dotenv()
    db_password = os.getenv("DB_PASSWORD")
    uri = f"mongodb+srv://almeidamirtilo:{db_password}@cluster-pipeline.mb0y6ww.mongodb.net/?retryWrites=true&w=majority&appName=cluster-pipeline"
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Conectado ao MongoDB!")
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        raise
    return client

def rename_lat_lon(collection):
    collection.update_many({}, {'$rename': {'lat': 'Latitude', 'lon': 'Longitude'}})

def get_livros(collection):
    query = { "Categoria do Produto": "livros" }
    livros = list(collection.find(query))
    df_livros = pd.DataFrame(livros)
    if not df_livros.empty:
        df_livros["Data da Compra"] = pd.to_datetime(df_livros["Data da Compra"], format="%d/%m/%Y")
        df_livros["Data da Compra"] = df_livros["Data da Compra"].dt.strftime("%Y-%m-%d")
    return df_livros

def get_produtos_2021_em_diante(collection):
    query = {"Data da Compra": {"$regex": "/202[1-9]"}}
    produtos = list(collection.find(query))
    df_produtos = pd.DataFrame(produtos)
    if not df_produtos.empty:
        df_produtos["Data da Compra"] = pd.to_datetime(df_produtos["Data da Compra"], format="%d/%m/%Y")
        df_produtos["Data da Compra"] = df_produtos["Data da Compra"].dt.strftime("%Y-%m-%d")
    return df_produtos

def main():
    client = connect_mongo()
    db = client["db_produtos"]
    collection = db["produtos"]

    # Renomear campos lat/lon
    rename_lat_lon(collection)

    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data_python')
    os.makedirs(data_dir, exist_ok=True)

    # Livros
    df_livros = get_livros(collection)
    df_livros.to_csv(os.path.join(data_dir, 'tabela_livros.csv'), index=False)
    print(f"Salvo tabela_livros.csv com {len(df_livros)} registros.")

    # Produtos vendidos a partir de 2021
    df_produtos = get_produtos_2021_em_diante(collection)
    df_produtos.to_csv(os.path.join(data_dir, 'tb_2021_em_diante.csv'), index=False)
    print(f"Salvo tb_2021_em_diante.csv com {len(df_produtos)} registros.")

    client.close()

if __name__ == "__main__": main()