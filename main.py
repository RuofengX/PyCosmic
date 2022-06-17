from world import World
from entity import ships


# class God(DynamicEntity):
#     def __init__(self):
#         self.add_processor(logging.Logger())


if __name__ == "__main__":
    w = World("debug")

    # w.create_entity(God())

    w.create_entity(
        ships.Ship(Position=(0, 0), Velocity=(1, 0), tag={"name": "移动测试飞船"})
    )
    for i in range(100):
        w.create_entity(
            ships.TestShip(Position=(0, 0), Velocity=(-1, 0), tag={"name": "组件测试飞船"})
        )

    w.run_endless()
