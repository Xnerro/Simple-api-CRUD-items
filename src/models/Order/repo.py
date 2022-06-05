from sqlalchemy.orm import Session

from . import model, schemas

class RepoOrder:
    
    async def create_order(db: Session, order: schemas.OrderCreate):
        order_item = model.Order(tanggal = order.tanggal, idBarang = order.idBarang)
        db.add(order_item)
        db.commit()
        db.refresh(order_item)
        return order_item
    
    def order_by_id(db: Session, _id):
        order = db.query(model.Order).filter(model.Order.id == _id).first()
        return order
    
    def get_all(db: Session):
        order = db.query(model.Order).all()
        return order

    async def delete(db: Session, _id):
        order = db.query(model.Order).filter(model.Order.id == _id).first()
        db.delete(order)
        db.commit()