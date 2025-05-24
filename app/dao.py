from daobase import DAOBase
from app.models import Parts, Orders, Customers


class CustomersDAO(DAOBase):
    model = Customers

class OrdersDAO(DAOBase):
    model = Orders

class PartsDAO(DAOBase):
    model = Parts