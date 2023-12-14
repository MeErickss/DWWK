from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def criar():
    try:
        engine = create_engine('postgresql://postgres:caquidecalcinha123@localhost:5432/4BM')
        Base = declarative_base()
        Session = sessionmaker(bind=engine)
        session = Session()

        return [engine, Base, Session, session]
    except Exception as error:
        return error