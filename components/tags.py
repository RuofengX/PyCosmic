# 标签系统
from dataclasses import dataclass, field

from typing import Dict, Type, NewType, Optional, Any, List
from collections import namedtuple

from components import base


@dataclass
class Tag:
    tags: dict = field(default_factory={name: ""})
