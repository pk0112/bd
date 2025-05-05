from daobase import DAOBase
from app.models import Vessel, Voyage, Personnel, Shipment, Port, PortCall


class VesselDAO(DAOBase):
    model = Vessel

class VoyageDAO(DAOBase):
    model = Voyage

class PersonnelDAO(DAOBase):
    model = Personnel

class ShipmentDAO(DAOBase):
    model = Shipment

class PortDAO(DAOBase):
    model = Port

class PortCallDAO(DAOBase):
    model = PortCall