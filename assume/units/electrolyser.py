import numpy as np
import pandas as pd

from assume.strategies import BaseStrategy
from assume.units.base_unit import BaseUnit


class Electrolyser(BaseUnit):
    def __init__(
        self,
        id: str,
        technology: str,
        bidding_strategies: dict,
        max_hydrogen_output: float or pd.Series,
        min_hydrogen_output: float or pd.Series,
        efficiency: float or pd.Series,
        volume: float or pd.Series = 1000,
        electricity_price: float or pd.Series = 3000,
        ramp_up: float = -1,
        ramp_down: float = 1,
        fixed_cost: float = 0,
        min_operating_time: float = 0,
        min_down_time: float = 0,
        downtime_hot_start: int = 0.001,  # hours
        downtime_warm_start: int = 0.005,  # hours
        index: pd.DatetimeIndex = None,
        location: tuple[float, float] = None,
        node: str = None,
        dr_factor=None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            technology=technology,
            node=node,
            bidding_strategies=bidding_strategies,
            index=index,
        )

        self.max_hydrogen_output = max_hydrogen_output
        self.min_hydrogen_output = min_hydrogen_output
        self.efficiency = efficiency
        self.volume = volume
        self.electricity_price = (
            electricity_price
            if electricity_price is not None
            else pd.Series(0, index=index)
        )
        self.fixed_cost = fixed_cost
        self.ramp_up = ramp_up
        self.ramp_down = ramp_down
        self.min_operating_time = min_operating_time
        self.min_down_time = min_down_time
        self.downtime_hot_start = downtime_hot_start
        self.location = location
        self.dr_factor = dr_factor

    def reset(self):
        """Reset the unit to its initial state."""
        self.current_status = 1
        self.current_down_time = self.min_down_time

    def calculate_operational_window(
        self,
        product_type: str,
        product_tuple: tuple,
    ) -> dict:
        """Calculate the operational window for the next time step.

        Returns
        -------
        operational_window : dict
            Dictionary containing the operational window for the next time step.
        """
        start, end, only_hours = product_tuple
        start = pd.Timestamp(start)
        end = pd.Timestamp(end)

        if self.current_status == 0 and self.current_down_time < self.min_down_time:
            return None

        max_power = self.max_hydrogen_output.at[start]
        min_power = self.min_hydrogen_output.at[start]

        # Adjust for ramp down speed
        if self.ramp_down != -1:
            min_power = max(0, min_power - self.ramp_down)
        else:
            min_power = min_power

        current_power_input = self.total_hydrogen_output.at[start]

        # Adjust min_power if sold negative reserve capacity on control reserve market
        min_power = min_power + self.neg_capacity_reserve.at[start]

        # Adjust for ramp up speed
        if self.ramp_up != -1:
            max_power = min(current_power_input + self.ramp_up, max_power)
        else:
            max_power = max_power

        # Adjust max_power if sold positive reserve capacity on control reserve market
        max_power = max_power - self.pos_capacity_reserve.at[start]

        operational_window = {
            "window": {"start": start, "end": end},
            "current_power": {
                "power": current_power_input,
                "marginal_cost": self.calc_marginal_cost(start),
            },
            "min_power": {
                "power": min_power,
                "marginal_cost": self.calc_marginal_cost(start),
            },
            "max_power": {
                "power": max_power,
                "marginal_cost": self.calc_marginal_cost(start),
            },
        }

        return operational_window

    def calculate_bids(
        self,
        product_type: str,
        product_tuple: tuple,
    ):
        return super().calculate_bids(
            product_type=product_type,
            product_tuple=product_tuple,
        )

    def get_dispatch_plan(self, dispatch_plan, current_time):
        if dispatch_plan["total_capacity"] > self.min_power:
            self.current_status = 1
            self.current_down_time = 0
            self.total_hydrogen_output.at[current_time] = dispatch_plan[
                "total_capacity"
            ]

        elif dispatch_plan["total_capacity"] < self.min_power:
            self.current_status = 0
            self.current_down_time += 1
            self.total_hydrogen_output.at[current_time] = 0

    def calc_marginal_cost(
        self,
        timestep: pd.Timestamp,
    ) -> float or pd.Series:
        """
        Calculate the marginal cost for the electrolyser at the given time step.

        Parameters
        ----------
        timestep : pd.Timestamp
            The current time step.

        Returns
        -------
        bid_price : float or pd.Series
            The calculated bid price.
        """
        efficiency_t = self.efficiency.loc[timestep]

        if type(self.electricity_price) == pd.Series:
            bid_price = self.electricity_price.at[timestep] / efficiency_t
        else:
            bid_price = self.electricity_price / efficiency_t

        return bid_price