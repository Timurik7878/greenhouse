from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func 
from sqlalchemy import Column, Integer, Float, DateTime 

DATABASE_URL = "postgresql://postgres:12345678@127.0.0.1:5433/db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
class TempLogSQLA(Base):
    __tablename__ = "temp_logs"
    id = Column(Integer, primary_key=True)
    tempval = Column(Float)
    
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
