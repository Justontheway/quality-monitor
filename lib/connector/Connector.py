'''Connector is an abstract class for connecting any place to get data or info.'''

class Connector(object):
    '''Abstract class for connect datastore to get information.'''
    def __init__(self, conf = {}):
        self._conf = conf
        self.open()
    def __del__(self):
        self.close()
    def __enter__(self):
        return self
    def __exit__(self, *exe_info):
        return
    def open(self):
        return
    def close(self):
        return

