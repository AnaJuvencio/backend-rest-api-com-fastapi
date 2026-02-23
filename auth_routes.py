from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao, bcrypt_context
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from main import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Função para criar token JWT
# O token JWT é um padrão aberto para criar tokens de acesso que permitem a comunicação segura entre um cliente e um servidor. Ele é composto por três partes: header, payload e signature. O header contém informações sobre o tipo de token e o algoritmo de criptografia utilizado. O payload contém as informações do usuário e as permissões de acesso. A signature é gerada a partir do header e do payload usando uma chave secreta, garantindo a integridade do token.
def criar_token(id_usuario, duracao_token=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    # Versão 1: Usando o access_token_expires definido nas nossas variáveis de ambiente como 30 minutos
    # Versão 2: Usando auto refresh, ou seja, o token é renovado a cada vez que o usuário faz uma requisição, mantendo a sessão ativa enquanto o usuário estiver utilizando a aplicação.
    dict_informacoes = {"sub": id_usuario, "exp": data_expiracao}
    jwt_codificado = jwt.encode(dict_informacoes, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_codificado

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    else:
        return usuario
    
    
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
    
@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session=Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
    if not usuario:
        raise HTTPException(status_code=400, detail="Email não cadastrado") # raise lança uma exceção, return devolce 200
    else:
        access_token = criar_token(usuario.id)
        refresh_token = criar_token(usuario.id, duracao_token=timedelta(days=7)) # token de refresh com duração de 7 dias
        # JWT Bearer -> envia dentro do headers = {"Access-Token": "Bearer <token>}
        return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "Bearer"}