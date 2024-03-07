from enums.state_enum import StateEnum
from enums.action_enum import ActionEnum
from enums.perception_enum import PerceptionEnum
from model.rule import Rule
import time


class SodaMachine:

    def __init__(self):
        self.rules = [
            Rule(StateEnum.WITHOUT_COIN, ActionEnum.ASK_COIN),
            Rule(StateEnum.COIN_RECEIVED, ActionEnum.ASK_SODA_CODE),
            Rule(StateEnum.C1_SERVED, ActionEnum.SERVE_C1),
            Rule(StateEnum.C2_SERVED, ActionEnum.SERVE_C2),
            Rule(StateEnum.C3_SERVED, ActionEnum.SERVE_C3),
        ]
        self.state = None
        self.action = None

    def update_state(self, perception: PerceptionEnum) -> StateEnum:
        if self.state is None and self.action is None and perception is None:
            return StateEnum.WITHOUT_COIN
        elif self.state == StateEnum.WITHOUT_COIN and self.action == ActionEnum.ASK_COIN and perception == PerceptionEnum.COIN:
            return StateEnum.COIN_RECEIVED
        elif self.state == StateEnum.COIN_RECEIVED and self.action == ActionEnum.ASK_SODA_CODE and perception == PerceptionEnum.C1:
            return StateEnum.C1_SERVED
        elif self.state == StateEnum.COIN_RECEIVED and self.action == ActionEnum.ASK_SODA_CODE and perception == PerceptionEnum.C2:
            return StateEnum.C2_SERVED
        elif self.state == StateEnum.COIN_RECEIVED and self.action == ActionEnum.ASK_SODA_CODE and perception == PerceptionEnum.C3:
            return StateEnum.C3_SERVED
        elif self.state == StateEnum.COIN_RECEIVED and self.action == ActionEnum.ASK_SODA_CODE and perception == PerceptionEnum.COIN:
            return StateEnum.COIN_RECEIVED
        else:
            return StateEnum.WITHOUT_COIN

    def match_rule(self, state: StateEnum) -> Rule:
        for rule in self.rules:
            if rule.condition == state:
                return rule
        return self.rules[0]

    def work(self, perception: PerceptionEnum):
        self.state = self.update_state(perception)
        rule = self.match_rule(self.state)
        self.action = rule.action

        if self.action == ActionEnum.ASK_COIN:
            self.ask_coin()
        elif self.action == ActionEnum.ASK_SODA_CODE:
            self.ask_soda_code()
        elif self.action == ActionEnum.SERVE_C1:
            self.serve_c1()
        elif self.action == ActionEnum.SERVE_C2:
            self.serve_c2()
        elif self.action == ActionEnum.SERVE_C3:
            self.serve_c3()

        self.ask_and_wait_perception()

    def ask_and_wait_perception(self):
        try:
            self.watch_current_data()
            perception_number = input("(0) Insert coin\n(1) C1\n(2) C2\n(3) C3\nType perception: ")
            perception = PerceptionEnum(int(perception_number))
            self.work(perception)
        except ValueError:
            self.ask_and_wait_perception()

    def watch_current_data(self):
        print("Current State        -> " + str(self.state))
        print("Last Executed Action -> " + str(self.action))

    def ask_coin(self):
        print("Please insert a coin!")
        self.ask_and_wait_perception()

    def ask_soda_code(self):
        print("Please choose a soda!")
        self.ask_and_wait_perception()

    def serve_c1(self):
        print("Serving soda 1")
        time.sleep(3)
        print("Soda 1 served!")
        time.sleep(2)
        self.reset()

    def serve_c2(self):
        print("Serving soda 2")
        time.sleep(3)
        print("Soda 2 served!")
        time.sleep(2)
        self.reset()

    def serve_c3(self):
        print("Serving soda 3")
        time.sleep(3)
        print("Soda 3 served!")
        time.sleep(2)
        self.reset()

    def reset(self):
        self.watch_current_data()
        self.work(None)
