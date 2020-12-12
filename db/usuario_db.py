from typing import Dict
from pydantic import BaseModel



class usuarioInDB(BaseModel):
    nombre: str
    mejorpuntaje: int
    ultimopuntaje: int



database_usuario = Dict[str, usuarioInDB] # {"nombre":}
database_usuario = {
    "Sebastian": usuarioInDB(**{"nombre":"Sebastian",
                            "mejorpuntaje":1000,
                            "ultimopuntaje":10}),
    "Sofia": usuarioInDB(**{"nombre":"Sofia",
                            "mejopuntaje":40,
                            "ultimopuntaje":20}),
}

def get_usuario(nombre: str):
    if nombre in database_usuario.keys():
        return database_usuario[nombre]
    else:
        return None
        
def update_usuario(usuario_in_db: usuarioInDB):
    database_usuario[usuario_in_db.nombre] = usuario_in_db
    return usuario_in_db
