#-*- coding:utf-8 -*_

from jinja2 import Environment, PackageLoader

import sys

import os
sys.path.append(os.getenv("MONITOR_HOME", ".."))


class AnalysisResult(object):
    def __init__(self, ar = ()):
        self.key = ar[0]
        self.value = ar[1]
        self.rule = ar[2]
        self.mean = ar[3]
        self.var = ar[4]
        self.times = ar[5]
        self.count = ar[6]
        self.status = ar[7]
        self.color = ar[8]


def render_result(raw_data):
    env = Environment(loader=PackageLoader('templates', 'templates'))
    template = env.get_template('default.html')
    return template.render(dataset = [ AnalysisResult(rd) for rd in raw_data])

def test():
    raw_data = [
        ("all_1",  231.0, u"最小精度", 230.65, 0.48, 0.3500, 20, u"很好", "#02DF82"),
        ("all_20", 41.0,  u"最小精度", 41.00,  0.00, 0.0000, 20, u"很好", "#02DF82"),
        ("all_5",  99.0,  u"最小精度", 98.65,  0.48, 0.3500, 20, u"很好", "#02DF82"),
        ("all_50", 15.0,  u"最小精度", 15.00,  0.00, 0.0000, 20, u"很好", "#02DF82"),
        ("all_80", 5.0,   u"最小精度", 5.00,   0.00, 0.0000, 20, u"很好", "#02DF82")
    ]
    return render_result(raw_data)

if __name__ == "__main__":
    print test()

