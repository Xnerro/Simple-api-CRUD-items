from sqlalchemy import Column, Integer,  Date, ForeignKey, String
from sqlalchemy.orm import relationship
from ..Barang.model import Barang
from ..db import Base

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, index=True)
    tanggal = Column(Date)
    idBarang = Column(String(10), ForeignKey('barang.id_barang'))
    barang = relationship('Barang', back_populates='items')

    def __repr__(self):
        return 'Order(tanggal%s, idBarang%s)' %(self.tanggal, self.idBarang)