from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import Settings
from Db import Resources,Miner,Base
 
engine = create_engine(Settings.settings['DB']['connection'])

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

 
def addResources(results):
    newResources = Resources(otype=results['otype'],title=results['title'],priceX1=results['X1'],priceX10=results['X10'],priceX100=results['X100'])
    session.add(newResources)
 
def addMiner(results):
    newMiner = Miner(otype=results['otype'],title=results['title'],priceX1=results['X1'],priceX10=results['X10'],priceX100=results['X100'])
    session.add(newMiner)

def rollBack():
    session.rollback()

def commitDB():
    session.commit()

if __name__ == "__main__":
    pass
