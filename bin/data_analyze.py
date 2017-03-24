#-*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.path.join(os.getenv("MONITOR_HOME", ".."), "lib"))

from data_gen import data_gen
from model import Statistic


if __name__ == "__main__":
    period = 20
    d = data_gen()
    models = Statistic.Statistic()
    for key in sorted(d.keys()):
        value = d[key]
        last = value[0]
        print key, last,
        print models.evaluate(map(lambda v:v[1], value[1:period]))

