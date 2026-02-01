# Estudos de API REST com FastAPI

> ⚠️ **Projeto de Estudos** - Este é um projeto desenvolvido para aprendizado de APIs REST com FastAPI.

## O que foi feito até agora

- ✅ Configuração básica do FastAPI
- ✅ Estrutura de rotas com `APIRouter`
- ✅ Rotas de autenticação (`/auth`)
- ✅ Rotas de pedidos (`/pedidos`)
- ✅ Organização modular do código

## Tecnologias

- Python
- FastAPI
- Uvicorn

## Como rodar

1. **Criar ambiente virtual:**
   ```bash
   python -m venv .venv
   ```

2. **Ativar ambiente virtual:**
   - Windows: `.venv\Scripts\activate`
   - Linux/Mac: `source .venv/bin/activate`

3. **Instalar dependências:**
   ```bash
   pip install fastapi uvicorn
   ```

4. **Executar o servidor:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Acessar a documentação:**
   - Abra: `http://localhost:8000/docs`

## Conceitos aprendidos

**Tipos de requisições HTTP:**
- **GET** - Buscar informações
- **POST** - Enviar informações/criar
- **PUT/PATCH** - Edição
- **DELETE** - Deletar

## Estrutura do projeto

```
├── main.py           # Arquivo principal
├── auth_routes.py    # Rotas de autenticação
└── order_routes.py   # Rotas de pedidos
```
