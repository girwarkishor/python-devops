import sqlalchemy

from sqlalchemy import create_engine, Table, Column, String, MetaData
meta = MetaData()

employees = Table(
    "employees", meta,
    Column('name', String)
)

class AlchemyDatabase:
    def __init__(self):
        self.name = "kuna.db"

    def create_database(self):
        engine = create_engine("sqlite:///" + self.name, echo=True)
        return engine



db_object = AlchemyDatabase()
db_engine = db_object.create_database()
meta.create_all(db_engine)
conn_string = db_engine.connect()


emp_result = employees.insert().values(name="rao")
final_result = conn_string.execute(emp_result)