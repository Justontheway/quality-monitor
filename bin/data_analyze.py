#-*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.path.join(os.getenv("MONITOR_HOME", ".."), "lib"))

from data_gen import data_gen
from model import Statistic, Precision, LinearAggregation


def model_test():
    period = 20
    d = data_gen()
    model1 = Statistic.Statistic()
    model2 = Precision.Precision()
    model3 = LinearAggregation.LinearAggregation()
    for key in sorted(d.keys()):
        value = d[key]
        last = value[0]
        #print key, last[1],
        #print model1.evaluate(map(lambda v:v[1], value[1:period]))
        #print model2.evaluate(map(lambda v:v[1], value[1:period]))
        m, v = model1.evaluate(map(lambda v:v[1], value[1:period]))
        p, l = model2.evaluate(map(lambda v:v[1], value[1:period]))
        model3.train(map(lambda v:v[1], value[1:period])[::-1])
        predict = model3.predict(len(value[1:period]) + 1)

        value = float(last[1])
        mean = float(m)
        var = float(v)
        times = (value - mean) / var if var != 0 else 0
        vart = var / mean if mean != 0 else 0
        print key, "\033[33m", value, predict[0], "\033[0m", mean, var, p,
        if abs(times) >= 1.96:
            print "\033[31m", times, "\033[0m",
        else:
            print times,
        if abs(vart) >= 1:
            print "\033[32m", vart, "\033[0m", predict
        else:
            print vart


if __name__ == "__main__":
    model_test()

