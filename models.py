# arquivo de crição do bd
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

db = create_engine("sqlite:///banco.db")  # conexão, banco de dados sqlites

Base = declarative_base()  # base do banco de dados

class Usuario(Base):
    __tablename__ = "usuarios" # nome da tabela
    
    # restrições sql
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable = False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default = False)
    
    # define oq precis acontecer ao criar o objeto
    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
        
class Pedido(Base):
    __tablename__ = "pedidos"   # nome da tabela
    
    """
    STATUS_PEDIDOS = (
        ("Pendente", "Pendente"),
        ("Cancelado", "Cancelado"),
        ("Finalizado", "Finalizado"),
    )
    """
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) # pendente, cancelado, finalizado
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    #itens =
    
    def __init__(self, usuario, status="Pendente", preco=0.0):
        self.status = status
        self.usuario = usuario
        self.preco = preco
        
class ItemPedido(Base):
    __tablename__ = "itens_pedidos"   # nome da tabela
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    pedido = Column("pedido", ForeignKey("pedidos.id"))
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", Integer)
    quantidade = Column("quantidade", Integer)
    preco_unitario = Column("preco_unitario", Float)
    
    def __init__(self, pedido, sabor, tamanho, quantidade, preco_unitario):
        self.pedido = pedido
        self.sabor = sabor
        self.tamanho = tamanho
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario