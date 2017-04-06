from decimal import Decimal
import numpy as np

from BaseModel import BaseModel


class Statistic(BaseModel):
    def __init__(self, param = {}):
        BaseModel.__init__(self, "statistic", param)

    def calc_variance(self, dataset):
        '''Calculate E(x) and Var(x).
        If dataset has no data, then return -1, -1,
        else return E(x), Var(x).'''
        if len(dataset) < 1:
            return -1, -1
        narray = np.array([ Decimal(ele) for ele in dataset ])
        return narray.mean(), np.sqrt(narray.var())

    def evaluate(self, dataset):
        '''Return E(x), Var(x)'''
        return self.calc_variance(dataset)

