from datetime import *
from typing import Any, List
from pydantic import BaseModel

from ..Barang.schema import Barang

class OrderBase(BaseModel):
    tanggal: Any
    idBarang: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    class Config:
        orm_mode = True
