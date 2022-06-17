import time
import math
import inspect
import sys

from simple_pid import PID


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class FrameControl:
    """帧率控制器

    参数:
    fps 目标帧率

    每次调用wait()时，会自动休眠，令两次wait之间的时间趋向fps
    """

    def __init__(self, fps: int):
        self.target_gap = 1 / fps
        self.gap = 0

        self._last_run = time.time()
        self._pid = PID(
            0.001, 0.005, 0.0002, setpoint=self.target_gap, output_limits=[0, 1]
        )  # TODO:波动剧烈

    def wait(self):
        # 在每一帧结束时调用，自动休眠（目标时间-已用时间）
        self.gap = time.time() - self._last_run
        # sleep_time = self._pid(self.gap)  # TODO: 实现PID调节帧率
        sleep_time = self.target_gap - self.gap

        self._last_run = time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

    @property
    def fps(self):
        if self.gap == 0:
            return math.inf
        else:
            return 1 / self.gap


class MemoryHelp:
    @staticmethod
    def get_size(obj, seen=None):
        """Recursively finds size of objects in bytes"""
        size = sys.getsizeof(obj)
        if seen is None:
            seen = set()
        obj_id = id(obj)
        if obj_id in seen:
            return 0
        # Important mark as seen *before* entering recursion to gracefully handle
        # self-referential objects
        seen.add(obj_id)
        if hasattr(obj, "__dict__"):
            for cls in obj.__class__.__mro__:
                if "__dict__" in cls.__dict__:
                    d = cls.__dict__["__dict__"]
                    if inspect.isgetsetdescriptor(d) or inspect.ismemberdescriptor(d):
                        size += MemoryHelp.get_size(obj.__dict__, seen)
                    break
        if isinstance(obj, dict):
            size += sum((MemoryHelp.get_size(v, seen) for v in obj.values()))
            size += sum((MemoryHelp.get_size(k, seen) for k in obj.keys()))
        elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
            size += sum((MemoryHelp.get_size(i, seen) for i in obj))

        if hasattr(obj, "__slots__"):  # can have __slots__ with __dict__
            size += sum(
                MemoryHelp.get_size(getattr(obj, s), seen)
                for s in obj.__slots__
                if hasattr(obj, s)
            )

        return size
