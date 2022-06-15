# 飞船基本组件
from dataclasses import dataclass, field

from typing import Dict, Type, NewType, Optional, Any, List
from collections import namedtuple

from components import base
from things.ShipComponents import reactor, defense


AvailableComponent = namedtuple("available_component", ["type", "max_num"])


@dataclass
class ShipBase():

    name: str
    available_components: List[AvailableComponent]
    tags: dict = field(default_factory=dict)
    structure: defense.Structure = defense.Structure()  # TODO:需要深入了解field()
    available_components: List[AvailableComponent]  # 飞船兼容的组件和数量
