from __future__ import annotations
from dataclasses import dataclass, field

import numpy as np

from processor import Processor


@dataclass
class Entity:
    pass


@dataclass
class DynamicEntity(Entity, Processor):
    # 动态实体如果有process方法则会在每一次循环中调用
    pass


@dataclass
class PositionEntity(Entity):
    Position: np.ndarray = field(default_factory=np.array([0, 0]))


@dataclass
class MovingEntity(PositionEntity, DynamicEntity):
    Velocity: np.ndarray = field(default_factory=np.array([0, 0]))

    def process(self, w):
        self.Position = np.array((self.Position)) + np.array((self.Velocity))
