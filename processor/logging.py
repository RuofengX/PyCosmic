from esper import Processor

from objprint import op


from components.ship import ShipBase


class Logger(Processor):
    def process(self):

        for entity, (ship_components) in self.world.get_components(ShipBase):

            op(ship_components[0])
