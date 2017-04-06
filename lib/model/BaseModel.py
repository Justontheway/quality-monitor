'''Abstract Model for data processing.'''

class BaseModel(object):
    def __init__(self, name, param={}):
        self.param = param
        self.name = name
        self.model = None
    def __del__(self):
        return
    def __enter__(self):
        return self
    def __exit__(self, *exe_info):
        return
    def train(self, dataset):
        raise NotImplementedError
    def predict(self, dataset):
        raise NotImplementedError
    def evaluate(self, dataset):
        raise NotImplementedError
    def score(self, dataset):
        raise NotImplementedError

