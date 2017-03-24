'''This module is used to define collector to collect data that need to be analyzed.'''
class Collector(object):
    def __init__(self, conf):
        self._conf = conf
    def __del__(self):
        return
    def __enter__(self):
        return self
    def __exit__(self, *exe_info):
        return
    def open(self):
        raise NotImplementedError
    def get_data(self):
        raise NotImplementedError

