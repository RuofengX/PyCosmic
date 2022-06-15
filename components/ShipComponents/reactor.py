# 反应堆组件
 
from dataclasses import dataclass

from things import energy, items
from components.base import ShipComponent


@dataclass
class NuclearReactor(ShipComponent):
    fuel = items.ReactorFuel
    out = energy.energy
    cost: 1
    efficiency: float = 1.0
