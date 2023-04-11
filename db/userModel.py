from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db.database import Base
import uuid
import datetime

from bcrypt import hashpw, gensalt

class User(Base):
    __tablename__ = 'users'
    id = Column(String(50), primary_key=True)
    name = Column(String(50), nullable=False, default='Annonymous')
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    created_at = Column(DateTime(), nullable=False)
    modified_at = Column(DateTime(), nullable=True)

    def __init__(self, name=None, email=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()

    def __repr__(self):
        return f'<User {self.name!r}>'