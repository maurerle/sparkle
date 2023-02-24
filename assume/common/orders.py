import logging
from datetime import datetime, timedelta
from math import isclose, log10
from typing import TypedDict

from dateutil import relativedelta, rrule
from mango import Role

from assume.common.marketconfig import MarketConfig, MarketProduct, MarketOrderbook, Orderbook, Order
from assume.common.market_mechanisms import available_clearing_strategies

logger = logging.getLogger(__name__)



def is_mod_close(a, mod_b):
    """
    due to floating point, a mod b can be very close to 0 or very close to mod_b
    """
    abs_tol = 1e-14
    # abs_tol needed for comparison near zero
    return isclose(a % mod_b, 0, abs_tol=abs_tol) or isclose(
        a % mod_b, mod_b, abs_tol=abs_tol
    )


def round_digits(n, tick_size):
    """
    rounds n to the power of 10 of the needed tick_size
    Example_
    >>> round_digits(1.100001, 0.1)
    1.1
    >>> round_digits(400.1, 20)
    400
    """
    return round(n, 1-int(log10(tick_size)))


class OpeningMessage(TypedDict):
    context: str
    market_id: str
    start: float
    stop: float
    products: list[MarketProduct]


class ClearingMessage(TypedDict):
    context: str
    market_id: str
    orderbook: Orderbook


# can be extended with custom config fields


orderbook: MarketOrderbook = {
    "agent1": [
        {
            "start_time": datetime.now(),
            "end_time": datetime.now(),
            "volume": 100,
            "price": 50.4,
        },
        {
            "start_time": datetime.now(),
            "end_time": datetime.now(),
            "volume": 100,
            "price": 50.4,
        },
    ],
    "agent2": [
        {
            "start_time": datetime.now(),
            "end_time": datetime.now(),
            "volume": 100,
            "price": 50.4,
        },
        {
            "start_time": datetime.now(),
            "end_time": datetime.now(),
            "volume": 100,
            "price": 50.4,
        },
    ],
}


def get_available_products(market_products: list[MarketProduct], startdate: datetime):
    options = []
    for product in market_products:
        start = startdate + product.first_delivery_after_start
        if isinstance(product.duration, rrule.rrule):
            starts = list(product.duration.xafter(start, product.count + 1))
            for i in range(product.count):
                period_start = starts[i]
                period_end = starts[i + 1]
                options.append((period_start, period_end, product.only_hours))
        else:
            for i in range(product.count):
                period_start = start + product.duration * i
                period_end = start + product.duration * (i + 1)
                options.append((period_start, period_end, product.only_hours))
    return options