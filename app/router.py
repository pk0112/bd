from fastapi import APIRouter
from app.dao import GoalsDAO, TeamsDAO, MatchesDAO, PlayersDAO


router = APIRouter(
    prefix='/crud',
    tags=['Операции']
)


@router.get('/goals')
async def read_data():
    data = await GoalsDAO.get_object()
    return data


@router.delete('/delete/goals')
async def delete(id: int):
    await GoalsDAO.delete(id = id)
    return 'deleted'


@router.get('/players')
async def read_data():
    data = await PlayersDAO.get_object()
    return data


@router.delete('/delete/players')
async def delete(id: int):
    await PlayersDAO.delete(id = id)
    return 'deleted'


@router.get('/matches')
async def read_data():
    data = await MatchesDAO.get_object()
    return data


@router.delete('/delete/matches')
async def delete(id: int):
    await MatchesDAO.delete(id = id)
    return 'deleted'


@router.get('/teams')
async def read_data():
    data = await TeamsDAO.get_object()
    return data


@router.delete('/delete/teams')
async def delete(id: int):
    await TeamsDAO.delete(id = id)
    return 'deleted'
