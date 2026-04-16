from fastapi import APIRouter, HTTPException, Path, Query, status
from typing import List, Optional
from . import schemas, services


router = APIRouter(prefix="/products", tags=["Products"])

@router.post(
    "/", response_model=schemas.ProductRead, status_code=status.HTTP_201_CREATED
)
def alta_producto(producto: schemas.ProductCreate):
    return services.crear(producto)

@router.get(
    "/", response_model=schemas.ProductRead, status_code=status.HTTP_200_OK
)
def listar_productos(skip: int = Query(0, ge=0), limit: int = Query(10, le=50)):
    return services.obtener_todos(skip, limit)

@router.get(
    "/{id}", response_model=schemas.ProductRead, status_code=status.HTTP_200_OK
)
def detalle_producto(id: int = Path(..., gt=0)):
    producto = services.obtener_por_id(id)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No se encontro el producto"
        )
    return producto

@router.put(
    f"/{id}", response_model=schemas.ProductRead, status_code=status.HTTP_200_OK
)
def actualizar_producto(producto: schemas.ProductCreate, id: int = Path(..., gt=0)):
    actualizado = services.actualizar_total(id, producto)
    if not actualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
        )
    return actualizado

@router.put(
    f"/{id}/desactivar", response_model=schemas.ProductRead, status_code=status.HTTP_200_OK
)
def borrado_logico(id: int = Path(..., gt=0)):
    desactivado = services.desactivar(id)
    if not desactivado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
        )
    return desactivado

@router.get(
    f"/{id}/stock", response_model=schemas.ProductStockResponse, status_code=status.HTTP_200_OK
)
def consultar_stock(id: int = Path(..., gt=0)):
    resultado = services.obtener_estado_stock(id)
    if not resultado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
        )
    return resultado