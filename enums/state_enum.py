from enum import Enum


class StateEnum(Enum):
    WITHOUT_COIN = 0
    COIN_RECEIVED = 1
    C1_SERVED = 2
    C2_SERVED = 3
    C3_SERVED = 4
