# Estudos de API REST com FastAPI

> ⚠️ **Projeto de Estudos** - Este é um projeto desenvolvido para aprendizado de APIs REST com FastAPI.

## O que foi feito até agora

- ✅ Configuração básica do FastAPI
- ✅ Estrutura de rotas com `APIRouter`
- ✅ Rotas de autenticação (`/auth`)
- ✅ Rotas de pedidos (`/pedidos`)
- ✅ Organização modular do código
- ✅ Modelos de banco de dados com SQLAlchemy
- ✅ Migrações com Alembic

## Tecnologias

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic

## Como rodar

1. **Criar ambiente virtual:**
   ```bash
   python -m venv .venv
   ```

2. **Ativar ambiente virtual:**
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - Windows CMD: `.venv\Scripts\activate`
   - Linux/Mac: `source .venv/bin/activate`

3. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Ou instalar manualmente:
   ```bash
   pip install fastapi uvicorn
   ```

4. **Executar o servidor:**
   ```bash
   python -m uvicorn main:app --reload
   ```
   
   Ou (se o ambiente estiver ativado):
   ```bash
   uvicorn main:app --reload
   ```

5. **Aplicar migrações do banco de dados:**
   ```bash
   alembic upgrade head
   ```

6. **Acessar a documentação:**
   - Abra: `http://127.0.0.1:8000/docs`
   - Rotas disponíveis:
     - `/docs` - Documentação interativa
     - `/pedidos` - Rota de pedidos
     - `/auth` - Rota de autenticação

## Comandos do Alembic (Migrações de Banco de Dados)

### Criar uma nova migração
Gera automaticamente um arquivo de migração baseado nas mudanças dos modelos:
```bash
alembic revision --autogenerate -m "Descrição da migração"
```

### Aplicar migrações
Aplica todas as migrações pendentes ao banco de dados:
```bash
alembic upgrade head
```

### Reverter última migração
Desfaz a última migração aplicada:
```bash
alembic downgrade -1
```

### Ver histórico de migrações
Lista todas as migrações e seus status:
```bash
alembic history
```

### Ver migração atual
Mostra qual migração está atualmente aplicada:
```bash
alembic current
```

## Problemas comuns

### Erro ao renomear pasta do projeto
Se você renomear a pasta do projeto, o ambiente virtual `.venv` ficará quebrado porque contém caminhos absolutos. 

**Solução:**
```bash
# 1. Salvar pacotes instalados
python -m pip freeze > requirements.txt

# 2. Deletar ambiente virtual antigo
Remove-Item -Recurse -Force .venv

# 3. Criar novo ambiente virtual
python -m venv .venv

# 4. Ativar o novo ambiente
.venv\Scripts\Activate.ps1

# 5. Reinstalar pacotes
pip install -r requirements.txt
```

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
