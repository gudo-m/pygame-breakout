import time
import random
import sys

from breakout import BreakoutEnv, Breakout

env = BreakoutEnv()

env.reset()

while True:
    env.step(0 if random.randint(0, 150) < 50 else 1)
