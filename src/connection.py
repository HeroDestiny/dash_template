# connection.py
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()


def fetch_data_from_mysql():
    # Obter variáveis de ambiente
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    # Criar a URL de conexão do SQLAlchemy
    connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

    # Criar o engine do SQLAlchemy
    engine = create_engine(connection_string)

    # Conectar e recuperar dados
    df = pd.read_sql("SELECT * FROM historico", con=engine)
    return df
