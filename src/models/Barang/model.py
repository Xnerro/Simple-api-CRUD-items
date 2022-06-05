from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.orm import relationship

from ..db import Base

class Barang(Base):
    __tablename__= 'barang'
    id_barang = Column(String(10), primary_key=True)
    nama= Column(String(100))
    harga= Column(Integer)
    kategori= Column(Enum('atasan', 'bawahan', 'setelan'))
    items = relationship('Order', back_populates='barang')

    def __repr__(self):
        return 'itemModel(nama%s, harga%s, kategori%s)' % (self.nama, self.harga, self.kategori)