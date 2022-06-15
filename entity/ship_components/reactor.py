from dataclasses import dataclass

from entity.ship_components import ShipComponent, container
from entity import items


@dataclass
class ReactorBase(ShipComponent):
    fuel_type: items.Fuel
    cost_per_tick: int
    efficiency: float

    def process(self, w):
        raise NotImplementedError


class NuclearReactor(ReactorBase):
    def __init__(
        self,
        fuel_type: items.NuclearFuel,
        input_component: container.NuclearFuelTank,
        output_component: container.Battery,
        cost_per_tick: int,
        efficiency: float,
    ):
        self.fuel_type = items.NuclearFuel
        self.input_component = input_component
        self.output_component = output_component
        self.cost_per_tick: int = 1
        self.efficiency: float = 1.0

    def process(self, w):
        if self.input_component.left > 0:
            # TODO: 添加信息和控制系统，将各组件process中的报错写入队列
            pass
