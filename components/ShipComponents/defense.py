# 防御类型组件
from dataclasses import dataclass, field
from typing import Dict, ClassVar

from components.base import ShipComponent

class DefenseBase(ShipComponent):
    pass
    
@dataclass
class Structure(DefenseBase):
    # 船体
    total: int = 100
    left: int = 100


@dataclass
class Armor(DefenseBase):
    # 装甲
    pass
