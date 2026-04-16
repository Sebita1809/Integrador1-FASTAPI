from fastapi import APIRouter, HTTPException, Path, Query, status
from typing import List
from starlette.status import HTTP_404_NOT_FOUND
from . import schemas, services

router = APIRouter(prefix="/clients", tags=["clients"])

@router.post(
    "/", response_model=schemas.ClienteRead, status_code=status.HTTP_201_CREATED
)
def crear_cliente(cliente: schemas.ClienteCreate):
    return services.crear(cliente)

@router.get(
    "/", response_model=List[schemas.ClienteRead], status_code=status.HTTP_200_OK
)
def listar_clientes(skip: int = Query(0, ge=0), limit: int = Query(10, le=50)):
    return services.obtener_todos(skip, limit)

@router.get(
    "/{id}", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK
)
def encontrar_cliente(id: int = Path(..., gt=1)):
    cliente = services.obtener_por_id(id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return cliente

@router.put(
    "/{id}", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK
)
def editar_cliente(cliente: schemas.ClienteUpdate ,id: int = Path(..., gt=0)):
    cliente_actualizado = services.actualizar_cliente(id, cliente)
    if not cliente_actualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return cliente_actualizado

@router.put(
    "/{id}/desactivar", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK
)
def desactivar_cliente(id: int = Path(..., gt=0)):
    cliente_desactivado = services.desactivar(id)
    if not cliente_desactivado:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return cliente_desactivado