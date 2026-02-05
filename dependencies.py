from models import db
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db) # cria a sessão
        session = Session() # instancia a sessão
        yield session # fornece a sessão sem encerrar a execução da função
    finally: # garante que a sessão será fechada
        session.close()  # fecha a sessão após o uso