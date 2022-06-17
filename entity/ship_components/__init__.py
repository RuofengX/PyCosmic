# 星际旅行的必备组件
from __future__ import annotations
from collections import namedtuple
from typing import List, NewType, Tuple

from entity import Entity

AvailableComponent: Tuple[ShipComponent, int] = namedtuple(
    "AvailableComponent", ["ShipComponent", "max_num"]
)
AvailableComponents = NewType("AvailableComponents", List[AvailableComponent])


class ShipComponent(Entity):
    pass
