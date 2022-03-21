from sqlalchemy import create_engine, Column, Integer, Sequence, String, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Wombat(Base):
    __tablename__ = 'wombats'
    id = Column(Integer, Sequence('wombat_id'), primary_key=True)
    name = Column(String(50))
    dob = Column(Date)

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return f"<Wombat {self.name}, born: {self.dob}>"

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'dob': self.dob.isoformat()
        }
        return data
