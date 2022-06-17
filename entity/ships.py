from dataclasses import dataclass, field
from typing import List

from entity import MovingEntity
from entity.ship_components import (
    AvailableComponents,
    ShipComponent,
    container,
    defense,
)
from processor import logging


@dataclass
class Ship(MovingEntity):
    """尚未初始化数值和组件的飞船

    初始化属性和默认值已给出，可以根据需要在创建时动态设置
    """

    # 可用部件，随子类确定
    available_components: AvailableComponents = field(default_factory=dict, init=False)

    # tag，信息类型的属性
    tag: dict = field(default_factory=dict)

    # 船体值
    structure: defense.Structure = field(default_factory=defense.Structure)

    # 组件列表
    components: List[ShipComponent] = field(default_factory=list)

    def __post_init__(self):
        """通过继承这个方法来绑定动态逻辑的处理器Processor单例

        1. 记得调用super().__post_init__()
        2. 使用self.add_processor(p: Processor)来添加处理器，
           实例创建过程中会自动将实例index注册到对应的处理器单例中
        """
        super().__post_init__()
        return


@dataclass
class TestShip(Ship):
    """测试用的飞船模板

    实际过程中只需要通过某种工厂组件动态创建Ship实例即可
    """

    tag = {"name": "TestShip"}
    structure = defense.Structure(total=10, left=5)
    available_components: AvailableComponents = field(
        default_factory=lambda: {
            (defense.Armor, 1),
            (container.Battery, 1),
            (container.NuclearFuelTank, 1),
        }
    )
    components: List[ShipComponent] = field(
        default_factory=lambda: [
            defense.Armor(total=200, left=200),
        ]
    )

    def __post_init__(self):
        super().__post_init__()
        self.add_processor(logging.Logger())
        return
