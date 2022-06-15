from dataclasses import dataclass, field
from typing import List

from entity import MovingEntity
from entity.ship_components import defense, AvailableComponents, ShipComponent


@dataclass
class Ship(MovingEntity):
    tag: dict = field(default_factory=dict)
    structure: defense.Structure = field(default_factory=defense.Structure)
    available_components: AvailableComponents = field(default_factory=dict)
    components: List[ShipComponent] = field(default_factory=list)
    def process(self, w: World):
        super().process(w)
        for component in self.components:
            component.process(w)
