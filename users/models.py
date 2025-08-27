from sqlalchemy import Column, String, Integer,Boolean,DateTime, ForeignKey, text
from database import Base
from datetime import datetime


class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name=Column(String(40), index=True,nullable=False)
    last_name=Column(String(40), index=True,nullable=False)
    password=Column(String)
    email=Column(String, index=True, unique=True,nullable=False)
    is_superuser=Column(Boolean, server_default=text("false"),default=False,nullable=False)
    joined=Column(DateTime, default= datetime.now)
    phone_number=Column(String, nullable=False)
    country=Column(String)
    address=Column(String,nullable=False)


class OTP(Base):
    __tablename__="tokens"
    id=Column(Integer, primary_key=True, autoincrement=True, index=True)
    codigo=Column(Integer())
    exp=Column(DateTime)
    used=Column(Boolean, default=False)
    user_id=Column(Integer, ForeignKey("users.id"), nullable=False)

