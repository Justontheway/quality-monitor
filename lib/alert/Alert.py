'''Abstract Alert for inform something to somebody.'''

class Alert(object):
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
    def send(self, msg, msg_info, someone):
        raise NotImplementedError

