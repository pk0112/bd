from fastapi import APIRouter
from app.dao import CustomersDAO, PartsDAO, OrdersDAO


router = APIRouter(
    prefix='/crud',
    tags=['Операции']
)


@router.get('/customers')
async def read_data():
    data = await CustomersDAO.get_object()
    return data


@router.delete('/delete/customers')
async def delete(id: int):
    await CustomersDAO.delete(id = id)
    return 'deleted'


@router.get('/parts')
async def read_data():
    data = await PartsDAO.get_object()
    return data


@router.delete('/delete/parts')
async def delete(id: int):
    await PartsDAO.delete(id = id)
    return 'deleted'


@router.get('/orders')
async def read_data():
    data = await OrdersDAO.get_object()
    return data


@router.delete('/delete/orders')
async def delete(id: int):
    await OrdersDAO.delete(id = id)
    return 'deleted'

