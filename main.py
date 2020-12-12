from db.usuario_db import UsuarioInDB
from db.usuario_db import update_usuario, get_usuario
from db.partida_db import PartidaInDB
from db.partida_db import save_partida, update_partida
from models.usuario_models import UsuarioIn, UsuarioOut
from models.partida_models import PartidaIn, PartidaOut


from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI() ## Crea la aplicacion FastAPI



##########################################################
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080","https://cajero-app13.herokuapp.com/" # TODO actualizar con el link real en heroku
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
##############################################################

@api.post("/usuario/auth/")
async def auth_usuario(usuario_in: UsuarioIn):
    usuario_in_db = get_usuario(usuario_in.nombre)
    if usuario_in_db == None:
        return {"Autenticado": True }##"Cuenta creada en desarrolo"})
                           
    if usuario_in_db.password != usuario_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}


"""
@api.get("/usuario/balance/{usuarioname}")
async def get_balance(usuarioname: str):
    usuario_in_db = get_usuario(usuarioname)
    if usuario_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    usuario_out = usuarioOut(**usuario_in_db.dict())## el ** es mapear
    return usuario_out

@api.put("/user/partida/")
async def make_partida(partida_in: partidaIn):
    user_in_db = get_user(partida_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.balance < partida_in.value:
        raise HTTPException(status_code=400,
                            detail="Sin fondos suficientes")
    user_in_db.balance = user_in_db.balance - partida_in.value
    update_user(user_in_db)
    partida_in_db = partidaInDB(**partida_in.dict(),
                            actual_balance = user_in_db.balance)
    partida_in_db = save_partida(partida_in_db)
    partida_out = partidaOut(**partida_in_db.dict())
    return partida_out

## verificar con Postman
## python -m uvicorn main:api --reload
"""

