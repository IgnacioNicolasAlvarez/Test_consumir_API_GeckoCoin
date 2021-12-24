from typing import Optional, Text
from datetime import datetime
from sqlmodel import Field, SQLModel

from sqlalchemy import Column, TEXT

class CoinHistoryBase(SQLModel):
    id_coin: str
    symbol: str
    name: str
    current_price_usd: float
    market_cap_usd: float
    total_volume_usd: float
    #json_response: str = Field(sa_column=Column(TEXT))
    date_added: datetime = Field(default=datetime.now())


class CoinHistory(CoinHistoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CoinHistoryRead(CoinHistoryBase):
    pass
    
class CoinHistoryCreate(CoinHistoryBase):
    pass