# 星际旅行的必备组件
from collections import namedtuple
from typing import List, NewType

from entity import Entity

AvailableComponent = namedtuple("AvailableComponent", ["ShipComponent", "max_num"])
AvailableComponents = NewType("AvailableComponents", List[AvailableComponent])


class ShipComponent(Entity):
    pass
