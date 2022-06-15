# 基本物品的组件

from dataclasses import dataclass

@dataclass
class Item():
    name: str = "空"
    stack_size: int = 1

@dataclass
class ItemStack():
    item: ItemBase
    num: int = 0
    
    
    
@dataclass
class Fuel(ItemBase):
    name = "燃料"
    pass

@dataclass
class ReactorFuel(FuelBase):
    name = "反应堆燃料"
    pass
