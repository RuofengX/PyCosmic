from typing import List
import time
import math

from entity import Entity, DynamicEntity
from processor import Processor


class FrameControl:
    def __init__(self, fps: int):
        self.target_gap = 1 / fps
        self.gap = 0

        self._last_run = time.time()
        self._mark = (time.time(), time.time())

    def wait(self):
        # 在每一帧结束时调用，自动休眠（目标时间-已用时间）
        self.gap = time.time() - self._last_run

        sleep_time = self.target_gap - self.gap
        if sleep_time > 0:
            time.sleep(sleep_time)

        self._last_run = time.time()
        self._update_mark()  # fps测量，TODO:其余部分用PID重构

    def _update_mark(self):
        last2, last = self._mark
        self._mark = (last, time.time())

    @property
    def fps(self):
        last2, last = self._mark
        if last2 == last:
            return math.inf
        return 1 / (last - last2)


class World:
    def __init__(self, name, tick_per_second=20):
        self.name = name
        self.entities: List[Entity] = []  # TODO: 可以优化这个数据结构
        self.process_list: List[callable] = []

        self.tick = 0
        self.tick_per_second = tick_per_second
        self.ticker = FrameControl(tick_per_second)

    def create_entity(self, entity: Entity):
        self.entities.append(entity)
        if isinstance(entity, DynamicEntity):
            self._register_process(entity.process)

    def register_processor(self, processor: Processor):
        self._register_process(processor.process)

    def _register_process(self, process: callable):
        self.process_list.append(process)

    def run_one_tick(self):
        for process in self.process_list:
            process(self)

    def run_endless(self):
        while True:
            self.run_one_tick()
            self.tick += 1
            self.ticker.wait()
