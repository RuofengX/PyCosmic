import time

import esper
from processor import logging, moving


from EntityFactory.SimpleShip import SimpleShipFactory

if __name__ == "__main__":
    world = esper.World()
    world.add_processor(logging.Logger())
    world.add_processor(moving.MoveProcessor())
    
    
    SimpleShipFactory(world).create_ship()
    
    while 1:
        world.process()
        time.sleep(1)