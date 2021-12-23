from src.utils.file import save_dict_to_json_in_folder
from src.model.coins import CoinHistoryCreate
from src.utils.logger import logger
class CoinController():

    def __init__(self, coin, date) -> None:
        self.id_coin = coin
        self.date = date

    def persist_coin(self, coin_data: dict):
        coin = self._convert_to_model(coin_data)
        self._save_as_file(coin, self.date)

    def persist_coin(self, coins_data: list):
        for coin_data in coins_data:
            coin = self._convert_to_model(coin_data[1])
            self._save_as_file(coin, coin_data[0])

    def _save_as_file(self, data, date):
        save_dict_to_json_in_folder(
                "../test_data_dev_per/Files", data, date, self.id_coin)
        
        
        
    def _convert_to_model(self, coin) -> CoinHistoryCreate:
        try:
            coin_history = CoinHistoryCreate(
                id_coin =coin['id'],
                symbol = coin['symbol'],
                name = coin['name'],
                current_price_ars = coin['market_data']['current_price']['ars'],
                current_price_usd = coin['market_data']['current_price']['usd'],
                market_cap_usd = coin['market_data']['market_cap']['usd'],
                market_cap_ars = coin['market_data']['market_cap']['ars'],
                total_volume_usd = coin['market_data']['total_volume']['usd'],
                total_volume_ars= coin['market_data']['total_volume']['ars'],
                json_response=coin['json_response']
            )
        except Exception as e:
            logger.error(e)
            return None
        return coin_history