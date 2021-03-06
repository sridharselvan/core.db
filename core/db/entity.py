# -*- coding: utf-8 -*-

"""

    Module :mod:``


    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]


Base = declarative_base()

class UserEntity(Base):
    __tablename__ = 'user'

    user_idn = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    user_name = Column(String, nullable=False)
    hash1 = Column(String, nullable=False)
    hash2 = Column(String, nullable=True)
    phone_no1 = Column(String, nullable=False)
    phone_no2 = Column(String, nullable=True)
    email_id = Column(String, nullable=True)
    crt_dt = Column(DateTime, default=datetime.datetime.utcnow)
    upd_dt = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Integer, nullable=True)
    email_id = Column(String, nullable=True)

class CodeStatusEntity(Base):
    __tablename__ = 'code_status'

    status_idn = Column(Integer, primary_key=True)
    status = Column(String, nullable=False) 
    crt_dt = Column(DateTime, default=datetime.datetime.utcnow)
    upd_dt = Column(DateTime, default=datetime.datetime.utcnow)

class UserSessionEntity(Base):
    __tablename__ = 'user_session'

    user_session_idn = Column(Integer, primary_key=True)
    user_idn = Column(Integer, ForeignKey('user.user_idn'))
    client_ip = Column(String, nullable=False) 
    browser_name = Column(String, nullable=True) 
    browser_version = Column(String, nullable=True) 
    attempted_on = Column(DateTime, default=datetime.datetime.utcnow)
    status_idn = Column(Integer, ForeignKey('code_status.status_idn'))

    #user_idn = relationship('UserEntity', foreign_keys='UserEntity.user_idn') 
    #status_idn = relationship('CodeStatusEntity', foreign_keys='CodeStatusEntity.status_idn')


