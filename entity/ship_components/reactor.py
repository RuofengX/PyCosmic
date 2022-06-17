from dataclasses import dataclass

from entity.ship_components import ShipComponent, container
from entity import items


@dataclass
class ReactorBase(ShipComponent):
    fuel_type: items.Fuel
    cost_per_tick: int
    efficiency: float


@dataclass
class NuclearReactor(ReactorBase):
    fuel_type = items.NuclearFuel
    cost_per_tick = 1
    efficiency = 1.0
    input_component: container.NuclearFuelTank
    output_component: container.Battery
    
    def __post_init(self):
        self.add_processor(#TODO: 实现能量逻辑)
