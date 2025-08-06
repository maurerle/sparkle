# SPDX-FileCopyrightText: ASSUME Developers
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from sparkle.common.base import BaseUnit
from sparkle.units.demand import Demand
from sparkle.units.exchange import Exchange
from sparkle.units.powerplant import PowerPlant
from sparkle.units.storage import Storage

unit_types: dict[str, BaseUnit] = {
    "power_plant": PowerPlant,
    "demand": Demand,
    "exchange": Exchange,
    "storage": Storage,
}
