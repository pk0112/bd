from daobase import DAOBase
from app.models import Employee, Departament, Salary


class EmployeeDAO(DAOBase):
    model = Employee

class DepartmentDAO(DAOBase):
    model = Departament

class SalaryDAO(DAOBase):
    model = Salary
