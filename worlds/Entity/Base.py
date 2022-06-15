from dataclasses import dataclass, field
from collections import namedtuple

@dataclass
class Entity():
    Position = field(default_factory=namedtuple("Position", ["x", "y", "z"]))
    Velocity = field(default_factory=namedtuple("Velocity", ["x", "y", "z"]))
    