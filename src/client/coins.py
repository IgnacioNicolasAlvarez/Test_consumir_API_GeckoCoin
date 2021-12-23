import json

import requests
from src.utils.coins import get_coins
from src.utils.date import get_dates_in_interval
from src.utils.logger import logger
from time import sleep


def get_history_coin(coins_id, date: str) -> dict:
    data = {}
    try:
        res = requests.get(
            f"https://api.coingecko.com/api/v3/coins/{coins_id}/history?date={date}"
        )
        if res.status_code == 200:
            data = json.loads(res.text)
            data['json_response'] = res.text
    except Exception as e:
        logger.error(e)
    return data


def get_history_coin(coins_id, start_date: str, end_date: str) -> list:

    data_list = []
    for date in get_dates_in_interval(start_date, end_date):
        try:
            sleep(1)
            res = requests.get(
                f"https://api.coingecko.com/api/v3/coins/{coins_id}/history?date={date}"
            )
            if res.status_code == 200:
                data = json.loads(res.text)
                data['json_response'] = res.text
                data_list.append((date, data))
        except Exception as e:
            logger.error(e)
    return data_list


def get_coins_id(is_filter_coins=False) -> list:
    res = requests.get(
        "https://api.coingecko.com/api/v3/coins/list?include_platform=false"
    )
    coins_data = json.loads(res.text)
    coins_list = get_coins(
        is_filter_coins=is_filter_coins, coins_list=coins_data)
    return coins_list
