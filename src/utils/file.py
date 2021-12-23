import json
import os
import uuid

from src.utils.logger import logger


def save_dict_to_json_in_folder(folder_path: str, data, date: str, coin: str) -> None:

    date_splited = date.split("-")
    folder_path = folder_path + \
        f'/{coin}/{date_splited[2]}/{date_splited[1]}/{date_splited[0]}/'

    file_name = f"{uuid.uuid1()}.json"
    file_path = folder_path + file_name

    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except Exception as e:
            logger.error(e)

    with open(file_path, "w") as f:
        try:
            json.dump(data.dict(), f, indent=4, default=str)
        except Exception as e:
            logger.error(e)
