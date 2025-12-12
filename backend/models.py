# backend/app/models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    full_name = Column(String(200), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(200), unique=True, nullable=False)
    email = Column(String(100), unique=True)
    password = Column(String(500))
    status = Column(String(20), default='active')
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    notes = relationship("Note", back_populates="owner")

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    notes = Column(Text)  # matches DB
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    owner = relationship("User", back_populates="notes")

