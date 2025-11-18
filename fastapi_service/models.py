from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, String, func
from sqlalchemy.orm import relationship
from .database import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    full_name = Column(String(200), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    user_name = Column(String(200), unique=True, nullable=False)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    status = Column(String(20), default='active')
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))


class SmartNotes(Base):
    __tablename__ = 'smartnotes'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)