from dataclasses import dataclass

from entity import Entity


class Item(Entity):  # 物品
    pass


@dataclass
class ItemStack:  # 物品堆叠
    item: items.Item
    num: int = 0


@dataclass
class Energy:  # 能量
    # 最小单位
    pass


@dataclass
class Fuel(Item):
    heat: int = 0  # 多少份能量


@dataclass
class NuclearFuel(Fuel):
    heat: int = 1


@dataclass
class Container(Item):
    slots: List[ItemStack]


@dataclass
class EnergyContainer(Container):
    slots: List[ItemStack]
