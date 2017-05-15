#-*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.path.join(os.getenv("MONITOR_HOME", ".."), "lib"))

from data_gen import data_gen
from model import Statistic, Precision, LinearRegression, SinRegression


def model_test():
    period = 260
    d = data_gen()
    model1 = Statistic.Statistic()
    model2 = Precision.Precision()
    model3 = LinearRegression.LinearRegression()
    model4 = SinRegression.SinRegression()
    for key in sorted(d.keys()):
        value = d[key]
        last = value[0]
        if len(value) < 3:
            print "*" * 10, value, "*" * 10
            continue
        m, v = model1.evaluate(map(lambda v:v[1], value[1:period]))
        p, l = model2.evaluate(map(lambda v:v[1], value[1:period]))
        model3.train(map(lambda v:v[1], value[1:period])[::-1])
        predict3 = model3.predict(len(value[1:period]) + 1)
        model4.train(map(lambda v:v[1], value[1:period])[::-1])
        predict4 = model4.predict_range(len(value[1:period]) + 1)
        print len(value[1:period]) + 1, period

        value = float(last[1])
        mean = float(m)
        var = float(v)
        times = (value - mean) / var if var != 0 else 0
        vart = var / mean if mean != 0 else 0
        if value != 0 and (abs(predict3[0]/value) > 1.1 or abs(predict3[0]/value) < 0.9):
            print key, "\033[33m", value, predict3[0], predict4, "\033[0m", mean, var, p,
        else:
            print key, value, predict3[0], predict4, mean, var, p,

        if abs(times) >= 1.96:
            print "\033[31m", times, "\033[0m",
        else:
            print times,

        if abs(vart) >= 1:
            print "\033[32m", vart, "\033[0m", predict3
        else:
            print vart



if __name__ == "__main__":
    model_test()

