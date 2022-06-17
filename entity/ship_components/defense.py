from dataclasses import dataclass

from entity.ship_components import ShipComponent


@dataclass
class DefenseBase(ShipComponent):
    total: int = 100
    left: int = total


@dataclass
class Structure(DefenseBase):
    pass


@dataclass
class Armor(DefenseBase):
    total: int = 500
    left: int = total
