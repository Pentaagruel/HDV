import os
import sys
import Settings
from sqlalchemy import Column, ForeignKey, Integer, String, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import func
 
Base = declarative_base()
 
class Resources(Base):
    __tablename__ = 'Resources'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, Sequence('id_priceX_Resources_temps'), primary_key=True)
    otype = Column(String(250), nullable=True)
    title = Column(String(250), nullable=True)    
    priceX1 = Column(Integer, nullable=True)
    priceX10 = Column(Integer, nullable=True)
    priceX100 = Column(Integer, nullable=True)
    date = Column(DateTime(timezone=True), server_default=func.now())

class Miner(Base):
    __tablename__ = 'Miner'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, Sequence('id_priceX_Miner_temps'), primary_key=True)
    otype = Column(String(250), nullable=True)
    title = Column(String(250), nullable=True)    
    priceX1 = Column(Integer, nullable=True)
    priceX10 = Column(Integer, nullable=True)
    priceX100 = Column(Integer, nullable=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine(Settings.settings['DB']['connection'])
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

if __name__ == "__main__":
    pass
