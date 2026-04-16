from optparse import Option
from pydantic import BaseModel, Field
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str = Field(..., example="Juan")
    email: str = Field(..., example="juanito@gmail.com")
    dni: int = Field(..., example="452589684")
    activo: bool = True

class ClienteCreate(ClienteBase):
    pass 

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None

class ClienteRead(ClienteBase):
    id: int
