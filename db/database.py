from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


dir_name = os.path.dirname(__file__)
db_path = 'sqlite:///' + os.path.join(dir_name, 'data.db')


engine = create_engine(db_path)
db_session = scoped_session( sessionmaker(autocommit=False, autoflush=False, bind=engine) ) 

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)
    print('Database initialized')

