from sqlalchemy import Column, Integer, String, DateTime
from database.database import  Base
from datetime import datetime


class Model(Base):
    __tablename__ = "model_info"
    __table_args__ = {'schema': 'llmtr_data'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    creator = Column(Integer, nullable=False)
    instructions = Column(String(1000), nullable=False)
    tools = Column(String(255), nullable=False)
    model = Column(String(255), nullable=False)
    created_ts = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_ts = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
