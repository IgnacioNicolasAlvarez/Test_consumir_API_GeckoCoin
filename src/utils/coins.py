import toml
import requests
import json

from src.model.coins import CoinHistoryCreate

def get_coins(is_filter_coins=False, coins_list=None) -> list:
    if is_filter_coins:
        coins_id_to_filter = toml.load(f="../test_data_dev_per/list_coins.toml")['coins_to_search']['coins_id']
        coins_id = [coin['id'] for coin in coins_list if coin['id'] in coins_id_to_filter]
    else:
        coins_id = [coin['id'] for coin in coins_list]
        
    return coins_id


