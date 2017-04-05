#-*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.path.join(os.getenv("MONITOR_HOME", ".."), "lib"))

from data_gen import data_gen
from model import Statistic, Precision


def model_test()
    period = 20
    d = data_gen()
    model1 = Statistic.Statistic()
    model2 = Precision.Precision()
    for key in sorted(d.keys())[:2]:
        value = d[key]
        last = value[0]
        print key, last,
        print model1.evaluate(map(lambda v:v[1], value[1:period]))
        print model2.evaluate(map(lambda v:v[1], value[1:period]))

if __name__ == "__main__":
    model_test()

