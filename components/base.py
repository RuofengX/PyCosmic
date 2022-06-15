from dataclasses import dataclass
from typing import Tuple, Dict, Type, NewType, Optional, Any
from collections import namedtuple


Position = namedtuple("Position", ["x", "y", "z"])
Velocity = namedtuple("Velocity", ["x", "y", "z"])


@dataclass
class CanMove:

    # 有速度和位置的需要渲染的实体 的组件（接口）
    position: Position
    velocity: Velocity
