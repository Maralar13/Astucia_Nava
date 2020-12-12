from pydantic import BaseModel

class UsuarioIn(BaseModel):
    nombre: str
    ultimopuntaje: int

class UsuarioOut(BaseModel):
    nombre: str
    ultimopuntaje: int
    mejorpuntaje: int
