from sqlalchemy.orm import Session

from . import schema, model

class RepoBarang:
    async def create_barang(db: Session, item: schema.TambahBarang):
        db_item = model.Barang(id_barang= item.id_barang, nama= item.nama, harga= item.harga, kategori= item.kategori)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def barang_by_id(db: Session, _id):
        barang = db.query(model.Barang).filter(model.Barang.id_barang == _id).first()
        return barang

    def barang_by_name(db: Session, _nama):
        barang = db.query(model.Barang).filter(model.Barang.nama == _nama).first()
        return barang
    
    def get_all(db: Session):
        barang = db.query(model.Barang).all()
        return barang

    async def delete(db: Session, _id):
        barang = db.query(model.Barang).filter(model.Barang.id_barang==_id).first()
        db.delete(barang)
        db.commit()

    async def update(db: Session, item_data):
        update_barang = db.merge(item_data)
        db.commit()
        return update_barang