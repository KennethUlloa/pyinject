from pyinject import Dependency, inject


class DB:
    def __init__(self, con_str: str):
        self.con_str = con_str


class Service:
    def __init__(self, db: DB):
        self.db = db


db_dep = Dependency(DB, "a str")
serv = Dependency(Service, db=db_dep.inject())


@inject
def function(service: Service = serv):
    print(service.db.con_str)

function()
