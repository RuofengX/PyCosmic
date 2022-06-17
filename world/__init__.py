from typing import List

from util import FrameControl
from entity import Entity, DynamicEntity
import processor as rule


class World:
    def __init__(self, name, tick_per_second=20):
        self.name = name
        self.processors: List[rule.Processor] = []
        self.entities: List[
            Entity
        ] = []  # 仅仅保存实体的__dict__数据， 逻辑请使用processor处理  # TODO: 可以优化这个数据结构

        self.tick = 0
        self.tick_per_second = tick_per_second
        self.ticker = FrameControl(tick_per_second)

    def create_entity(self, entity: Entity) -> int:
        # TODO: 需要try_catch
        index = len(self.entities)

        if isinstance(entity, DynamicEntity):
            for processor in entity._processor_list:
                processor.add_entity(index)
                self.register_processor(processor)  # 对一个实体只会调用一次

        self.entities.append(entity.__dict__)  # 只将实体的属性添加到实体列表中

        return index

    def register_processor(self, processor: rule.Processor):
        if processor not in self.processors:
            self.processors.append(processor)

    def run_one_tick(self):
        for processor in self.processors:
            processor.run_one_tick(self)

    def run_endless(self):
        while True:

            self.run_one_tick()
            self.tick += 1
            self.ticker.wait()
