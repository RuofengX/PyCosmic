from typing import List

from util import Singleton


class ProcessorMeta(Singleton):
    def __new__(metacls, name: str, bases: List[type], attrs: dict) -> type:
        cls = type.__new__(metacls, name, bases, attrs)
        if "process" not in attrs.keys():
            raise NotImplementedError("Processor must have a process method")

        return cls


class Processor(metaclass=ProcessorMeta):
    # 处理器，单例，每一个实体类型都拥有自己定制的处理器，在实体实例化过程中会自动注册
    # _target_entity_set: 需要处理的实体集合
    def __init__(self):
        self._target_entity_set: set = set()  # 需要处理的实体集合

    def add_entity(self, entity_index: int):
        """幂等的将需要被计算的实体的索引添加到处理器的目标实体集合中，以便每次计算时快速索引"""
        self._target_entity_set.add(entity_index)

    def run_one_tick(self, world):
        for entity_index in self._target_entity_set:
            self.process(world, entity_index)

    def process(self, world, entity_index: int):
        # 必须实现一个process方法，传入处理器的注册者world和当前遍历的实体entity；注册之后每tick对每个**需要的对象**调用一次；
        raise NotImplementedError


class ThreadSafeProcessor(Processor):
    """线程安全处理器"""

    def __init__(self, target_entity_list: list = None):
        super().__init__(target_entity_list)

    def process(self, world, entity_index: int):
        pass

        # TODO:让可行的处理器跨线程运行
