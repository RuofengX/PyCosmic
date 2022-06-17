from objprint import op

from processor import ThreadSafeProcessor
from world import World


class Logger(ThreadSafeProcessor):
    def process(self, world: World, entity_index: int):
        ent = world.entities[entity_index]
        op(ent)
