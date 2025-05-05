import asyncpg
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import cnf


try:
    conn = asyncpg.connect(dbname="postgres", user=cnf.USER, password=cnf.PASSWORD, host=cnf.HOST)
    cursor = conn.cursor()
    conn.autocommit = True
    sql = f"CREATE DATABASE {cnf.NAME}"
    cursor.execute(sql)
    cursor.close()
    conn.close()
except: pass

URL = f"{cnf.URL}"
engine = create_async_engine(URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit = False)
class Base(DeclarativeBase):
    pass
