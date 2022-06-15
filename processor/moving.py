from processor import Processor
from world import World

import numpy


class Moving(Processor):
    def process(self, world: World):
        for ent in world.entities:
            if hasattr(ent, "Position") and hasattr(ent, "Velocity"):  # TODO:需要NP完整解决方案
                ent.Position = numpy.array((ent.Position)) + numpy.array((ent.Velocity))
