# 飞船基本组件
from dataclasses import dataclass, field
from typing import Dict, Type, NewType, Optional, Any, List
from collections import namedtuple

from components import base


AvailableComponent = namedtuple("available_component", ["type", "max_num"])

@dataclass
class Ship():
    available_components: List[AvailableComponent] = field(default_factory=AvailableComponent)
    # structure: defense.Structure = defense.Structure()  # TODO:需要深入了解field()
    available_components: List[AvailableComponent]  # 飞船兼容的组件和数量
