from sqlmodel import Session, SQLModel, create_engine
from src.model.coins import CoinHistory
from src.utils.logger import log


try:
    engine = create_engine("postgresql+psycopg2://example:example@db:5432/example")
    SQLModel.metadata.create_all(engine)
except Exception as e:
    pass
    
def create_session():
    return Session(bind=engine)

def insert(object):
    try:
        with create_session() as session:
            session.add(object)
            log(msj=f"{object} insertado", type="info")
            session.commit()
    except Exception as e:
        log(msj=f"Error en insert: {e}", type="error")
