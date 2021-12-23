import json
from time import sleep

import requests
from src.utils.coins import get_coins
from src.utils.date import get_dates_in_interval
from src.utils.logger import logger


class ApiGeckoClient:
    def get_history_coin(self, coin_id, date: str) -> dict:
        data = {}
        try:
            res = requests.get(
                f"https://api.coingecko.com/api/v3/coins/{coin_id}/history?date={date}"
            )
            if res.status_code == 200:
                data = json.loads(res.text)
                data["json_response"] = res.text
        except Exception as e:
            logger.error(e)
        return data

    def get_history_coin(self, coin_id, start_date: str, end_date: str) -> list:

        data_list = []
        for date in get_dates_in_interval(start_date, end_date):
            try:
                sleep(1)
                res = requests.get(
                    f"https://api.coingecko.com/api/v3/coins/{coin_id}/history?date={date}"
                )
                if res.status_code == 200:
                    data = json.loads(res.text)
                    data["json_response"] = res.text
                    data_list.append((date, data))
            except Exception as e:
                logger.error(e)
        return data_list
