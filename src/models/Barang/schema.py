from enum import Enum
from pydantic import BaseModel

class Kategori(str, Enum):
    atasan= 'atasan'
    bawahan= 'bawahan'
    setelan= 'setelan'

class BaseBarang(BaseModel):
    id_barang:str
    nama: str
    harga: int
    kategori: Kategori
    class Config:
        use_enum_values= True

class TambahBarang(BaseBarang):
    pass

class Barang(BaseBarang):
    id_barang: str
    class Config:
        orm_mode = True