# Инструкция

## Оглавление

- [Установка](#Установка)
- [Запуск](#Запуск)

## Установка

1. Клонируйте репозиторий
     ```bash
     git clone https://github.com/pk0112/bd.git
     ```
     Вставить в терминал
   
3. Откройте проект в VSCode или Pycharm

   Создайте виртуальное окружение

   ```bash
   python -m venv .venv
   ```

   ```bash
   .venv\scripts\activate
   ```

   ```bash
   pip install -r requirements.txt
   ```

5. Создайте файл с названием `.env` в корне проекта (на том же уровне что и файл `main.py`)

   Содержание:
   
   ```bash
   HOST = localhost
   PORT = 5432
   USER = postgres
   PASSWORD = <ваш_пароль от бд (у меня 123)> 

6. Редактирование файлов

   Список файлов к редактированию (для удобства делайте все по очереди):

   - [app/models.py](#app/models.py)
   - [app/dao.py](#app/dao.py)
   - [app/router.py](#app/router.py)
   - [migrations/versions/4ca9025dd74c_.py](#migrations/versions/4ca9025dd74c_.py)

  ### app/models.py

  Возьмите сущности таблиц из ваших бд и поменяйте названия классов, названия и типы колнок, например:
  
     ``` python
     class <Ваше_название_с_большой_буквы>(Base):
      __tablename__ = '<ваше_название_с_маленькой_буквы>'
      
     <ваша_колонка_с_первичным_ключом> = Column(<тип_данных>, primary_key=True, autoincrement=True)
     <ваша_колонка2> = Column(<тип_данных>, nullable=False)
     ```
  ### app/dao.py

  Тут все просто, поменяйте во второй строке импорты на названия ваших таблиц, которые вы делали в прошлом пункте, далее поменяйте название классов и соответсвующие названия моделей

     ``` python
     from daobase import DAOBase
     from app.models import <ваша_модель>, <ваша_модель2>
     
     class <ваша_модель>DAO(DAOBase):
       model = <ваша_модель>
    
     class <ваша_модель2>DAO(DAOBase):
       model = <ваша_модель2>
    
     ...
     ```
     
  ### app/router.py

  Из файла, который вы делали в прошлом пункте имортируйте классы с названием DAO в конце, затем в декораторах с поменяйте названия путей и функций

     ``` python
     from fastapi import APIRouter
     from app.dao import <ваша_модель>DAO, <ваша_модель2>DAO
      
     router = APIRouter(
       prefix='/crud',
       tags=['Операции']
     )
       
     @router.get('/<ваша_моддель_с_маленькой_буквы>')
     async def read_data():
       data = await <ваша_модель>DAO.get_object()
       return data
      
     @router.get('/<ваша_моддель2_с_маленькой_буквы>')
     async def read_data():
       data = await <ваша_модель2>DAO.get_object()
       return data

  ### migrations/versions/4ca9025dd74c_.py

  Самое сложное, полностью скопируйте файл models.py и попросите нейросеть оформить это в виде alembic ревизии, далее вставьте данные и напишите в терминал

  ``` bash
  alembic upgrade head
  ```

## Запуск

Напишите в терминале 

``` bash
uvicorn main:app --reload
```

Далее перейдите в браузере по адресу

`http://127.0.0.1:8000/docs#/`

Готово!
