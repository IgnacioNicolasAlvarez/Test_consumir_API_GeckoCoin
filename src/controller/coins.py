from src.client.coins import ApiGeckoClient
from src.db.database import DB
from src.model.coins import CoinHistoryCreate
from src.utils.config import FILES_PATH
from src.utils.file import save_dict_to_json_in_folder
from src.utils.logger import logger


class CoinController:
    def __init__(self, coin, date, to_db) -> None:
        self.id_coin = coin
        self.date = date
        self.to_db = to_db

    def get_coin(self) -> dict:
        api_client = ApiGeckoClient()
        return api_client.get_history_coin(self.id_coin, self.date)

    def get_coins(self, end_date: str) -> list:
        api_client = ApiGeckoClient()
        return api_client.get_history_coins(self.id_coin, self.date, end_date)

    def persist_coin(self, coin_data: dict) -> None:
        coin = self._convert_to_model(coin_data)
        self._save_as_file(coin, self.date)
        if self.to_db:
            self._save_into_db(coin)

    def persist_coins(self, coins_data: list) -> None:
        for coin_data in coins_data:
            coin = self._convert_to_model(coin_data[1])
            self._save_as_file(coin, coin_data[0])
            if self.to_db:
                self._save_into_db(coin)

    def _save_as_file(self, data, date):
        save_dict_to_json_in_folder(FILES_PATH, data, date, self.id_coin)

    def _save_into_db(self, coin_history: CoinHistoryCreate):
        db = DB()
        db.insert(coin_history)

    def _convert_to_model(self, coin) -> CoinHistoryCreate:
        try:
            coin_history = CoinHistoryCreate(
                id_coin=coin["id"],
                symbol=coin["symbol"],
                name=coin["name"],
                current_price_ars=coin["market_data"]["current_price"]["ars"],
                current_price_usd=coin["market_data"]["current_price"]["usd"],
                market_cap_usd=coin["market_data"]["market_cap"]["usd"],
                market_cap_ars=coin["market_data"]["market_cap"]["ars"],
                total_volume_usd=coin["market_data"]["total_volume"]["usd"],
                total_volume_ars=coin["market_data"]["total_volume"]["ars"],
                json_response=coin["json_response"],
            )
        except Exception as e:
            logger.error(e)
            return None
        return coin_history
