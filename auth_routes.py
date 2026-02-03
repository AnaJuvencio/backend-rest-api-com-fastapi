from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"mensagem": "Vc acessou a rota de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session=Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first() # verifica se já existe o email
    if usuario:
        return {"mensagem": "Email já cadastrado"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "Usuario cadastrado com sucesso!"}