from enum import Enum


class DTYPE(Enum):
    STRING = 0
    INT = 1
    FLOAT = 2
    BOOL = 3
    JSON = 4

    @classmethod
    def choices(cls):
        return [(dtype.value, dtype.name) for dtype in cls]
