from objprint import op

from processor import Processor
from world import World


class Logger(Processor):
    def process(self, world: World):
        for ent in world.entities:
            op(ent)
