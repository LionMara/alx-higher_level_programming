#!/usr/bin/env python3

import sqlalchemy
from sqlalchemy import create_engine
from  sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name={}, fullname={}, nickname={}>".format(
            self.name, self.fullname, self.nickname)

Base.metadata.create_all(engine)


ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)
session.add_all([
    User(name='wendy',fullname='Wendy Williams', nickname='windy'),
    User(name='mary',fullname='Mary Contrares', nickname='ri'),
    User(name='fred',fullname='Fred Flintstone', nickname='papa freddy')])
fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
#session.add(fake_user)

session.commit()

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)
