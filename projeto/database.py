from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///spotypobre.db", echo=False)

def criando_banco():
    Base.metadata.create_all(bind=engine)

session = Session(bind=engine)