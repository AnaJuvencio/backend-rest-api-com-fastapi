from models import db
from sqlalchemy.orm import sessionmaker

def pegar_sessao():
    Session = sessionmaker(bind=db) # cria a sessão
    session = Session() # instancia a sessão
   
    return session