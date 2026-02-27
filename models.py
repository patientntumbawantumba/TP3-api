from sqlalchemy import Column, Integer, String, Float
from database import Base

class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    location = Column(String, nullable=False)
    imageUrl = Column(String, nullable=True)