# SPDX-FileCopyrightText: ASSUME Developers
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from importlib.metadata import version

from sparkle.common import MarketConfig, MarketProduct
from sparkle.scenario.loader_csv import (
    load_custom_units,
    load_scenario_folder,
)
from sparkle.world import World

__version__ = version("sparkle")

__author__ = "ASSUME Developers: Nick Harder, Kim Miskiw, Florian Maurer, Manish Khanra"
__copyright__ = "AGPL-3.0 License"
