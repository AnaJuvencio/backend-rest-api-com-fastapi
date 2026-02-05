# obejtivo: velocidade e integridade do sistema - não é obrigatório
from pydantic import BaseModel
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativos: Optional[bool] = True
    admin: Optional[bool] = False
    
    class Config:
        from_attributes = True # permite converter objetos ORM em modelos Pydantic