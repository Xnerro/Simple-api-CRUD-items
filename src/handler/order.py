from .init import *


router =  APIRouter(
    prefix='/order',
    tags=['order'],
    responses={404: {'msg': 'Not Found'}}
)

@router.get('/', response_model=List[schemas.Order])
async def get_all_order(db: Session = Depends(get_db)):
    return rpOrder.RepoOrder.get_all(db)

@router.get('/{id}', response_model=List[schemas.Order])
async def get_by_id(id: int, db: Session = Depends(get_db)):
    order = rpOrder.RepoOrder.order_by_id(db, id)
    if order:
        return order
    else:
        return HTTPException(404, f'Order tidak ditemukan dengan id {id}')

@router.post('/', response_model=schemas.Order)
async def create_order(items: schemas.OrderCreate,  db: Session = Depends(get_db)):
    return await rpOrder.RepoOrder.create_order(db, items)

@router.delete('/{id}')
async def delete_order(id: int, db: Session = Depends(get_db)):
    order = rpOrder.RepoOrder.order_by_id(db, id)
    if order:
        await rpOrder.RepoOrder.delete(db, id)
        return {'msg': 'delete success'}
    else:
        return HTTPException(404, f'Order tidak ditemukan dengan id {id}')