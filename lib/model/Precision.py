from BaseModel import BaseModel

class Precision(BaseModel):
    def __init__(self, param = {}):
        BaseModel.__init__("precision", param)

    def get_precision(number):
        strs = str(number).rstrip('0').split(".")
        return len(strs[1])

    def evaluate(self, dataset):
        '''If all data in dataset are numeric, then return 1,1.
        Else return 0.1**len(precision), len(precision)'''
        size = max(map(get_precision, dataset))
        return 0.1**size, max(1, size)

