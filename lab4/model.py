import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()

class Wallet(Base):
    __tablename__ = 'wallet'
    id = Column(Integer, primary_key=True)
    address = Column(String(250), nullable=False)
    balance = Column(Integer, nullable=False)
    public_key = Column(String(250), nullable=False)

    def __repr__(self):
        return 

 