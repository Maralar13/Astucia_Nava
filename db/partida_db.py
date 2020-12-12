from datetime import datetime
from pydantic import BaseModel
import random



class PartidaInd(BaseModel):
    id_partida: int = 0
    nombre: str
    tableroenemigo: str = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    tableropropio: str = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    turnopropio: bool = random.choice([True, False])
    fin: bool = False


database_partidas = []
generator = {"id":0}
def save_partida(partida_in_db: partidaInDB):
    generator["id"] = generator["id"] + 1 ## le coloca el id a la transaccion
    partida_in_db.id_partida = generator["id"]
    database_partidas.append(partida_in_db)
    return partida_in_db    

def update_partida(partida_in_db: partidaInDB):
    database_partida[partida_in_db.nombre] = partida_in_db
    return partida_in_db

#Tablero 12X12
#4 tipos de barcos
    #(1)portaviones 4
    #(2)buque =3
#   (3)submarino = 3
    #(4)galeron =3
    #(5(pesquero =2
# tablero_mio = "000000000"
# tablero_enemigo =

#Convenciones
#   (1)portaviones 
#   (2)buque 
#   (3)submarino 
#   (4)galeron 
#   (5(pesquero 
#   (6)ataque perdido 
#   (7)pesquero 





