from dataclasses import dataclass
from entity.ship_components import ShipComponent


class ContainerBase(ShipComponent):
    capacity: int
    left: int = 0


@dataclass
class Battery(ContainerBase):
    capacity: int
    left: int = 0


@dataclass
class NuclearFuelTank(ContainerBase):
    capacity: int
    left: int = 0


@dataclass
class StandardBattery(Battery):
    capacity: int = 100
    left: int = 0
