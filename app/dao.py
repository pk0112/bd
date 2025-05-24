from daobase import DAOBase
from app.models import Players, Matches, Teams, Goals


class PlayersDAO(DAOBase):
    model = Players

class MatchesDAO(DAOBase):
    model = Matches

class TeamsDAO(DAOBase):
    model = Teams

class GoalsDAO(DAOBase):
    model = Goals