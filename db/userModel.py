from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db.database import Base
import uuid
import datetime

from bcrypt import hashpw, gensalt, checkpw

class User(Base):
    __tablename__ = 'users'
    id = Column(String(50), primary_key=True)
    name = Column(String(50), nullable=False, default='Annonymous')
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    created_at = Column(DateTime(), nullable=False)
    modified_at = Column(DateTime(), nullable=True)

    def __init__(self, name=None, email=None, password=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        # no plain text passwords 
        self.password = hashpw(password.encode('utf-8'), gensalt())
        self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()

    # not sure what this is even here for
    def __repr__(self):
        return f'<User {self.name!r}>'
    
    def to_json(self):
        return {
            "id": f"{self.id}",
            "name": f"{self.name}",
            "email": f"{self.email}",
            "created_at": f"{self.created_at}",
            "modified_at": f"{self.modified_at}"
        }
    
    #takes plain text password and compares it to the hashed password
    def check_password(self, password):
        return checkpw(password.encode('utf-8'), self.password)