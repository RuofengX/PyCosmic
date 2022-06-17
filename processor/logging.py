from objprint import op

from processor import Processor
from world import World


class Logger(Processor):
    def process(self, world: World, entity_index: int):
        ent = world.entities[entity_index]
        op(ent)
        # print(world.ticker.fps)
