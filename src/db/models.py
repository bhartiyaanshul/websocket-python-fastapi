from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.database import Base
import sqlalchemy as db

class Message(Base):
    __tablename__ = "db_websocket"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer,nullable=True)
    content = Column(String(250), nullable=True)
    time = Column(DateTime(timezone=True),server_default=func.now())