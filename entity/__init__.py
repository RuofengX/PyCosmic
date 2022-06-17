# 引擎内部文件
from __future__ import annotations
from dataclasses import dataclass, field

import numpy as np

from processor import Processor, moving


class EntityMeta(type):
    """实体元类"""

    pass


@dataclass
class Entity(metaclass=EntityMeta):
    """实体基类"""

    # @classmethod
    # def from_dict(cls, data: dict):
    #     """用来从data创建一个实体"""
    #     rtn = cls()
    #     rtn.__dict__ = data
    #     return rtn
    def __str__(self):
        return self.__class__.__name__


class DynamicEntity(Entity):
    _processor_list = []

    @classmethod
    def add_processor(cls, processor: Processor):
        if processor not in cls._processor_list:
            cls._processor_list.append(processor)


@dataclass
class PositionEntity(Entity):
    Position: np.ndarray = field(default_factory=np.array([0, 0]))


@dataclass
class MovingEntity(PositionEntity, DynamicEntity):
    Velocity: np.ndarray = field(default_factory=np.array([0, 0]))

    def __post_init__(self):
        self.add_processor(moving.Moving())
