from optparse import Option
from typing import List, Optional
from .schemas import ProductCreate, ProductRead

db_productos: List[ProductRead] = []
id_counter = 1

def crear(data: ProductCreate) -> ProductRead:
    global id_counter
    nuevo = ProductRead(id=id_counter, **data.model_dump())
    db_productos.append(nuevo)
    id_counter += 1
    return nuevo

def obtener_todos(skip: int, limit: int) -> List[ProductRead]:
    return db_productos[skip: skip + limit]

def obtener_por_id(id: int) -> Optional[ProductRead]:
    for p in db_productos:
        if p.id == id:
            return p
    return None

def actualizar_total(id: int, data: ProductCreate) -> Optional[ProductRead]:
    for index, p in enumerate(db_productos):
        if p.id == id:
            producto_actualizado = ProductRead(id=id, **data.model_dump())
            db_productos[index] = producto_actualizado
            return producto_actualizado
    return None

def desactivar(id: int) -> Optional[ProductRead]:
    for index, p in enumerate(db_productos):
        if p.id == id:
            p_dict = p.model_dump()
            p_dict["active"] = False
            productos_actualizado = ProductRead(**p_dict)
            db_productos[index] = productos_actualizado
            return productos_actualizado
    return None

def obtener_estado_stock(id: int) -> Optional[dict]:
    producto = obtener_por_id(id)
    if not producto:
        return None
    alerta_stock = producto.stock < producto.stock_minimo
    return {
        "stock": producto.stock,
        "bajo_stock_minimo": alerta_stock,
        "activo": producto.activo
    }