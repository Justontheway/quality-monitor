from BaseModel import BaseModel

class Precision(BaseModel):
    def __init__(self, param = {}):
        BaseModel.__init__(self, "precision", param)

    def get_precision(self, number):
        strs = str(number).rstrip('0').split(".")
        try:
            return len(strs[1])
        except:
            return 0

    def evaluate(self, dataset):
        '''If all data in dataset are numeric, then return 1,1.
        Else return 0.1**len(precision), len(precision)'''
        size = max(map(self.get_precision, dataset))
        return 0.1**size, max(1, size)

