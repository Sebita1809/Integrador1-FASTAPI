from typing import List, Optional

from app.modules.producto.schemas import ProductRead
from .schemas import ClienteCreate, ClienteRead, ClienteUpdate

db_clientes: List[ClienteRead] = []
id_counter = 1

def crear(data: ClienteCreate) -> ClienteRead:
    global id_counter
    nuevo = ClienteRead(id= id_counter, **data.model_dump())
    db_clientes.append(nuevo)
    id_counter += 1
    return nuevo

def obtener_todos(skip: int, limit: int) -> List[ClienteRead]:
    return db_clientes[skip : skip + limit];

def obtener_por_id(id: int) -> Optional[ClienteRead]:
    for c in db_clientes:
        if c.id == id:
            return c
    return None

def actualizar_cliente(id: int, cliente: ClienteUpdate) -> Optional[ClienteRead]:
    for index, c in enumerate(db_clientes):
        if c.id == id:
            datos_actuales = c.model_dump()
            cambios = cliente.model_dump(exclude_unset=True)
            datos_actuales.update(cambios)
            cliente_actualizado = ClienteRead(**datos_actuales)
            db_clientes[index] = cliente_actualizado
            return cliente_actualizado
    return None

def desactivar(id: int) -> Optional[ClienteRead]:
    for index, c in enumerate(db_clientes):
        if c.id == id:
            c_dict = c.model_dump()
            c_dict["activo"] = False
            cliente_desactivado = ClienteRead(**c_dict)
            db_clientes[index] = cliente_desactivado
            return cliente_desactivado
    return None