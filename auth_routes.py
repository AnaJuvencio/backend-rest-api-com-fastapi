from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao, bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"mensagem": "Vc acessou a rota de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session=Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first() # verifica se já existe o email
    if usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado") # raise lança uma exceção, return devolce 200
    else:
        # Trunca senha para 72 bytes (limite do bcrypt)
        senha_truncada = usuario_schema.senha.encode('utf-8')[:72].decode('utf-8', errors='ignore')
        senha_criptografada = bcrypt_context.hash(senha_truncada)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativos, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"Usuario cadastrado com sucesso!{novo_usuario.email}"}