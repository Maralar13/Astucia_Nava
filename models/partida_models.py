from pydantic import BaseModel
from datetime import datetime

class PartidaIn(BaseModel):
    username: str
    value: int

class PartidaOut(BaseModel):
    id_partida: int
    nombre: str
    turnopropio: bool 
    fin: bool
    