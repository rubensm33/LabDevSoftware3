from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão para o MySQL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:Rubens1234@127.0.0.1/f_api"

# Criando o motor de conexão (sem o connect_args usado no SQLite)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para as classes ORM
Base = declarative_base()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
