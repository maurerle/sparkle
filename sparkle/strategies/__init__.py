# SPDX-FileCopyrightText: ASSUME Developers
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from sparkle.common.base import BaseStrategy, LearningStrategy
from sparkle.strategies.advanced_orders import flexableEOMBlock, flexableEOMLinked
from sparkle.strategies.extended import OTCStrategy
from sparkle.strategies.flexable import flexableEOM, flexableNegCRM, flexablePosCRM
from sparkle.strategies.flexable_storage import (
    flexableEOMStorage,
    flexableNegCRMStorage,
    flexablePosCRMStorage,
)
from sparkle.strategies.naive_strategies import (
    NaiveDADSMStrategy,
    NaiveProfileStrategy,
    NaiveRedispatchDSMStrategy,
    NaiveRedispatchStrategy,
    NaiveSingleBidStrategy,
    NaiveExchangeStrategy,
    ElasticDemandStrategy,
    DSM_PosCRM_Strategy,
    DSM_NegCRM_Strategy,
)
from sparkle.strategies.manual_strategies import SimpleManualTerminalStrategy
from sparkle.strategies.dmas_powerplant import DmasPowerplantStrategy
from sparkle.strategies.dmas_storage import DmasStorageStrategy


bidding_strategies: dict[str, BaseStrategy] = {
    "naive_eom": NaiveSingleBidStrategy,
    "naive_dam": NaiveProfileStrategy,
    "naive_pos_reserve": NaiveSingleBidStrategy,
    "naive_neg_reserve": NaiveSingleBidStrategy,
    "naive_exchange": NaiveExchangeStrategy,
    "elastic_demand": ElasticDemandStrategy,
    "otc_strategy": OTCStrategy,
    "flexable_eom": flexableEOM,
    "flexable_eom_block": flexableEOMBlock,
    "flexable_eom_linked": flexableEOMLinked,
    "flexable_neg_crm": flexableNegCRM,
    "flexable_pos_crm": flexablePosCRM,
    "flexable_eom_storage": flexableEOMStorage,
    "flexable_neg_crm_storage": flexableNegCRMStorage,
    "flexable_pos_crm_storage": flexablePosCRMStorage,
    "pos_crm_dsm": DSM_PosCRM_Strategy,
    "neg_crm_dsm": DSM_NegCRM_Strategy,
    "naive_redispatch": NaiveRedispatchStrategy,
    "naive_da_dsm": NaiveDADSMStrategy,
    "naive_redispatch_dsm": NaiveRedispatchDSMStrategy,
    "manual_strategy": SimpleManualTerminalStrategy,
    "dmas_powerplant": DmasPowerplantStrategy,
    "dmas_storage": DmasStorageStrategy,
}
