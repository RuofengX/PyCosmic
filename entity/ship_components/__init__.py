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
    """飞船组件

    均为静态组件，以对象形式保存在飞船实例中
    """

    pass
