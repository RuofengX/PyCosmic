from esper import Processor
from components.base import Position, Velocity

from objprint import op
class MoveProcessor(Processor):
    def process(self):
        for entity, (p, v) in self.world.get_components(Position, Velocity):
            p += v
            