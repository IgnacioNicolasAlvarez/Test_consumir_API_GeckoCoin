from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel



class CoinHistoryBase(SQLModel):
    id_coin: str
    symbol: str
    name: str
    current_price_usd: float
    market_cap_usd: float
    total_volume_usd: float
    json_response: str
    date_added: datetime = Field(default=datetime.now())


class CoinHistory(CoinHistoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CoinHistoryRead(CoinHistoryBase):
    pass
    
class CoinHistoryCreate(CoinHistoryBase):
    pass