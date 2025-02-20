# SPDX-FileCopyrightText: ASSUME Developers
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import logging
from datetime import datetime, timedelta

from dateutil import rrule as rr

from assume import World
from assume.common.fast_pandas import FastIndex
from assume.common.forecasts import NaiveForecast
from assume.common.market_objects import MarketConfig, MarketProduct

log = logging.getLogger(__name__)


def init(world, n=1, months=1):
    start = datetime(2019, 1, 1)
    end = datetime(2019, 1, 1) + timedelta(days=30 * months)

    index = FastIndex(start, end, freq="h")
    simulation_id = "world_script_simulation"

    world.setup(
        start=start,
        end=end,
        save_frequency_hours=480,
        simulation_id=simulation_id,
    )

    marketdesign = [
        MarketConfig(
            market_id="EOM",
            opening_hours=rr.rrule(
                rr.HOURLY, interval=24, dtstart=start, until=end, cache=True
            ),
            opening_duration=timedelta(hours=1),
            market_mechanism="pay_as_clear",
            market_products=[MarketProduct(timedelta(hours=24), 1, timedelta(hours=1))],
            additional_fields=["block_id", "link", "exclusive_id"],
        )
    ]

    mo_id = "market_operator"
    world.add_market_operator(id=mo_id)
    for market_config in marketdesign:
        world.add_market(mo_id, market_config)

    world.add_unit_operator("my_demand")
    world.add_unit(
        "demand1",
        "demand",
        "my_demand",
        # the unit_params have no hints
        {
            "min_power": 0,
            "max_power": 1000,
            "bidding_strategies": {"EOM": "naive_eom"},
            "technology": "demand",
            "price": 20,
        },
        NaiveForecast(index, demand=1000),
    )

    nuclear_forecast = NaiveForecast(index, availability=1, fuel_price=3, co2_price=0.1)
    for i in range(n):
        world.add_unit_operator(f"my_operator{i}")
        world.add_unit(
            f"nuclear{i}",
            "power_plant",
            f"my_operator{i}",
            {
                "min_power": 200 / n,
                "max_power": 1000 / n,
                "bidding_strategies": {"EOM": "naive_eom"},
                "technology": "nuclear",
            },
            nuclear_forecast,
        )


if __name__ == "__main__":
    import time

    [1, 2, 16, 64, 128, 256]  # 3 months
    [
        0.5300636291503906,
        0.5216586589813232,
        1.9283447265625,
        6.500819683074951,
        12.949028491973877,
        26.302656888961792,
        53.81222891807556,
    ]

    [1, 2, 16, 64, 128, 256]
    [
        0.9769134521484375,
        0.4847285747528076,
        3.1939425468444824,
        13.009318590164185,
        26.49550771713257,
        55.729703187942505,
    ]

    durs = []
    for i in [1]:
        t = time.time()
        db_uri = "postgresql://assume:assume@localhost:5432/assume"
        world = World(database_uri=db_uri)
        init(world, months=i)
        world.run()
        dur = time.time() - t
        durs.append(dur)
    print(durs)
