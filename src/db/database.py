from sqlmodel import Session, SQLModel, create_engine
from src.utils.logger import logger


try:
    engine = create_engine("postgresql+psycopg2://example:example@db:5432/example")
    SQLModel.metadata.create_all(engine)
except Exception as e:
    pass

class DB:
    def _create_session():
        return Session(bind=engine)

    def insert(self, object):
        try:
            with self._create_session() as session:
                session.add(object)
                logger.debug(f"{object} insertado")
                session.commit()
        except Exception as e:
            logger.error(f"Error en insert: {e}")
