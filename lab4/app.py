from datetime import date
from .model import Wallet
from .model import Base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///assignment2.db')
Base.metadata.create_all(engine)

def session_factory():
    from sqlalchemy.orm import sessionmaker
    DBSession = sessionmaker(bind=engine)
    return DBSession()

def create_wallets():
    session = session_factory()
    walletA = Wallet("0x12345", 1000, "345w24qc4fa4t34rae")
    walletA = Wallet("0x67890", 2000, "345w24qc4fa4t34rae")
    session.add(walletA)
    session.add(walletB)
    session.commit()
    session.close()


def get_wallets():
    session = session_factory()
    wallet_query = session.query(Wallet)
    session.close()
    return wallet_query.all()

def update_wallets():
    """TODO"""
    pass

def delete_wallets():
    """TODO"""
    pass

if __name__ == "__main__":
    wallets = get_wallets()
    if len(wallets) == 0:
        create_wallets()
    wallets = get_wallets()

    for wallet in wallets:
        print(wallet)
