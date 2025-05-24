from fastapi import APIRouter
from app.dao import EmployeeDAO, DepartmentDAO, SalaryDAO
from app.tasks import task1, task2


router = APIRouter(
    prefix='/crud',
    tags=['Операции']
)


@router.get('/employee')
async def read_data():
    data = await EmployeeDAO.get_object()
    return data


@router.delete('/delete/employee')
async def delete(id: int):
    await EmployeeDAO.delete(id = id)
    return 'deleted'


@router.get('/department')
async def read_data():
    data = await DepartmentDAO.get_object()
    return data


@router.delete('/delete/department')
async def delete(id: int):
    await DepartmentDAO.delete(id = id)
    return 'deleted'


@router.get('/salary')
async def read_data():
    data = await SalaryDAO.get_object()
    return data


@router.delete('/delete/salary')
async def delete(id: int):
    await SalaryDAO.delete(id = id)
    return 'deleted'


@router.get('/task1')
async def task():
    return await task1()


@router.get('/task2')
async def task():
    return await task2()

