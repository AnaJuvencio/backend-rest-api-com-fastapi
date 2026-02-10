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
        
class PedidoSchema(BaseModel):
    usuario: int 
    
    class Config:
        from_attributes = True
        
class LoginSchema(BaseModel):
    email: str
    senha: str
    
    class Config:
        from_attributes = True