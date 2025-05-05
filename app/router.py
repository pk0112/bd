from fastapi import APIRouter
from app.dao import PortDAO, VesselDAO, VoyageDAO, PortCallDAO, ShipmentDAO, PersonnelDAO

router = APIRouter(
    prefix='/crud',
    tags=['Операции']
)


@router.get('/vessels')
async def read_data():
    data = await VesselDAO.get_object()
    return data


@router.get('/ports')
async def read_data():
    data = await PortDAO.get_object()
    return data


@router.get('/voyages')
async def read_data():
    data = await VoyageDAO.get_object()
    return data


@router.get('/shipments')
async def read_data():
    data = await ShipmentDAO.get_object()
    return data


@router.get('/personnel')
async def read_data():
    data = await PersonnelDAO.get_object()
    return data


@router.get('/port_calls')
async def read_data():
    data = await PortCallDAO.get_object()
    return data
