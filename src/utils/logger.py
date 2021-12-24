import logging

from src.utils.config import LOG_PATH

logging.basicConfig(
    filename=LOG_PATH,
    filemode="w",
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)
