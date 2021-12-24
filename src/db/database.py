from sqlmodel import Session, SQLModel, create_engine
from src.utils.logger import logger
from src.model.coins import CoinHistory

engine = create_engine("postgresql+psycopg2://example:example@172.25.0.2:5432/example")
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
