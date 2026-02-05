# criar venv: python -m venv .venv
# ativar venv: .venv\Scripts\activate (windows) | source .venv/bin/activate (linux)
# uvicorn main:app --reload
# Vamos construir uma REST API
# endpoint: /docs, é o link do app
"""
Tipos de requisições:
    GET: Buscar informações
    POST: enviar informações/criar
    PUT/PATCH: edição
    Delete: deletar
"""

from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router
from dotenv import load_dotenv
import os

load_dotenv()  # carrega as variáveis de ambiente do arquivo .env

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)

