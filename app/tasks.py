from sqlalchemy import func, select
from app.models import Employee, Salary
from daobase import async_session_maker


async def task1():
    async with async_session_maker() as session:

        min_salary_subquery = (
            select(
                Employee.position,
                func.min(Salary.salary_amount).label('min_salary')
            )
            .join(Salary, Employee.employee_id == Salary.employee_id)
            .group_by(Employee.position)
            .subquery()
        )

        query = (
            select(
                Employee.first_name,
                Employee.last_name,
                Employee.position,
                Salary.salary_amount,
                (Salary.salary_amount - min_salary_subquery.c.min_salary).label('salary_diff')
            )
            .join(Salary, Employee.employee_id == Salary.employee_id)
            .join(min_salary_subquery, Employee.position == min_salary_subquery.c.position)
            .order_by('salary_diff')
            .limit(3)
        )

        result = await session.execute(query)

        rows = result.all()

        result_list = [
            {
                'first_name': row.first_name,
                'last_name': row.last_name,
                'position': row.position,
                'salary_amount': row.salary_amount,
                'salary_diff': row.salary_diff
            }
            for row in rows
        ]

        return result_list
    

async def task2():
    async with async_session_maker() as session:
        # Подсчёт количества каждого имени
        name_counts = (
            select(
                Employee.first_name,
                func.count(Employee.first_name).label('name_count')
            )
            .group_by(Employee.first_name)
            .order_by(func.count(Employee.first_name).desc())
            .limit(1)
        )

        result = await session.execute(name_counts)
        row = result.first()

        if row:
            return {
                'first_name': row.first_name,
                'count': row.name_count
            }
        else:
            return None