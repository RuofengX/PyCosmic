from world import World
from processor import moving, logging
from entity import ships

if __name__ == "__main__":
    w = World("debug")
    # w.register_processor(moving.Moving())
    w.register_processor(logging.Logger())
    
    w.create_entity(ships.Ship(
        Position=(0, 0),
        Velocity=(1, 0),
        tag={
            "name": "秋风之墩"
        }
    ))
    
    w.run_endless()