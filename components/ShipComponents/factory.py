# 制造类型组件
from dataclasses import dataclass, field
from typing import Dict, ClassVar

from components.base import ShipComponent
from components import ship
@dataclass
class Factory(ShipComponent):
    # 制造类型组件
    pass

@dataclass
class DefaultShipFactory(Factory):
    consume: Dict[item]
    # 默认制造类型组件
    pass