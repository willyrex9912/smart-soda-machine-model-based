from enums.action_enum import ActionEnum
from enums.state_enum import StateEnum


class Rule(object):

    def __init__(self, condition: StateEnum, action: ActionEnum):
        self.condition = condition
        self.action = action

