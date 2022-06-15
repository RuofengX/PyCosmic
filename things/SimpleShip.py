from esper import World
from components import ship
from components.ship import AvailableComponent
from components.ShipComponents import reactor, defense


class SimpleShipFactory:
    def __init__(self, world: World):
        self.world = world

    def create_ship(self):

        ship_ent = self.world.create_entity(
            ship.ShipBase(
                available_components={
                    AvailableComponent(reactor.NuclearReactor, 1),
                    AvailableComponent(defense.Armor, 2),
                },
                velocity=(10, 0, 0),
                position=(0, 0, 0),
                name="秋风之墩号",
            )
        )
        
