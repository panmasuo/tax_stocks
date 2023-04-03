from decimal import Decimal
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

from .exchange import Currency


class Activity(Enum):
    BUY = "BUY"  # Buy
    BUY_MARKET = "BUY - MARKET"  # new Revolut Buy
    SELL = "SELL"  # Sell
    SELL_MARKET = "SELL - MARKET"  # new Revolut Sell
    DIV = "DIVIDEND"  # Dividend
    SSP = "STOCK SPLIT"  # Stock Split


@dataclass
class Transaction:
    trade_date: datetime
    settle_date: datetime
    currency: Currency
    activity: Activity
    symbol: str  # 'TSLA'
    quantity: Decimal
    price: Decimal
    amount: Decimal
    dividend_tax_deducted: Decimal
