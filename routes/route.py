from fastapi import APIRouter
from src.handler import barang
from src.handler import order

router = APIRouter()
router.include_router(barang.router)
router.include_router(order.router)