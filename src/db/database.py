from sqlmodel import Session, SQLModel, create_engine
from src.utils.config import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER
from src.utils.logger import logger
from src.model.coins import CoinHistory
from src.utils.config import *

engine = create_engine(F"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}")
SQLModel.metadata.create_all(engine)

    
class DB:
    def _create_session(self):
        return Session(bind=engine)

    def insert(self, coin_history_create):
        try:
            with self._create_session() as session:
                object = CoinHistory.from_orm(coin_history_create)
                session.add(object)
                logger.debug(f"{object} insertado")
                session.commit()
        except Exception as e:
            logger.error(f"Error en insert: {e}")
