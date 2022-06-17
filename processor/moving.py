from processor import Processor

import numpy


class Moving(Processor):
    def process(self, world, entity_index: int):
        entity = world.entities[entity_index]
        entity["Position"] = numpy.add(entity["Position"], entity["Velocity"])
