from .init import *

router  = APIRouter(
    prefix='/barang',
    tags=['barang'],
    responses={404: {'msg': 'Not Found'}}
)

@router.get('/', response_model=List[schema.Barang])
async def get_all_barang(nama: Optional[str] = None, db: Session = Depends(get_db)):
    if nama:
        item = []
        item.append(rpBarang.RepoBarang.barang_by_name(db,nama))
        return item
    else:
        return rpBarang.RepoBarang.get_all(db)

@router.get('/{id}')
async def get_by_idBarang(id:str, db: Session = Depends(get_db)):
    return rpBarang.RepoBarang.barang_by_id(db, id)

@router.post('/', response_model=schema.Barang, status_code=201)
async def create_barang(item_request: schema.TambahBarang, db: Session = Depends(get_db)):
    return await rpBarang.RepoBarang.create_barang(db=db, item=item_request)

@router.delete('/{id}')
async def delete_barang(id: str, db: Session = Depends(get_db)):
    barang = rpBarang.RepoBarang.barang_by_id(db, id)
    if barang:
        await rpBarang.RepoBarang.delete(db, id)
        return {'msg': 'Delete Success'}
    else:
        return HTTPException(404, f'Barang tidak ditemukan dengan id_barang {id}')

@router.put('/{id}', response_model=schema.Barang)
async def update_barang(id: str, item_request: schema.Barang, db: Session = Depends(get_db)):
    barang = rpBarang.RepoBarang.barang_by_id(db, id)
    if barang:
        update = jsonable_encoder(item_request)
        barang.id_barang = barang.id_barang
        barang.nama = update['nama']
        barang.harga = update['harga']
        barang.kategori = update['kategori']
        return await rpBarang.RepoBarang.update(db, barang)
    else:
         return HTTPException(404, f'Barang tidak ditemukan dengan id_barang {id}')

# @router.get('/')
# def test():
#     return {'msg': 'masuk juga'}