from typing import Union
from sqlalchemy import select
from sqlalchemy.exc import ResourceClosedError
from sqlalchemy.orm.exc import UnmappedInstanceError

from core.psql import async_session_maker


class DAOBase:
    model = None

    @classmethod
    async def get_object(
        cls,
        **data,
    ) -> list[dict[str, Union[str, int]]] | None:
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**data)
            res = await session.execute(query)
            if res:
                return res.mappings().all()
            return None
        
    @classmethod
    async def add(
        cls,
        **data
    ) -> bool:
        async with async_session_maker() as session:
            try:
                query = cls.model(**data)
                session.add(query)
                await session.commit()
                return True
            except:
                return False
    
    @classmethod
    async def delete(
        cls,
        **data,
    ) -> bool:
        async with async_session_maker() as session:
            res = await session.execute(select(cls.model).filter_by(**data))
            if res:
                try:
                    await session.delete(res.scalars().first())
                    await session.commit()
                    return True
                except: return False
            return False