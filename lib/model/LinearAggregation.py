from decimal import Decimal
import numpy as np
from sklearn.linear_model import LinearRegression


from BaseModel import BaseModel


class LinearAggregation(BaseModel):
    def __init__(self, param = {}):
        BaseModel.__init__(self, "linear-aggregation", param)

    def train(self, dataset):
        '''
        Train the linearaggregation model.
        '''
        if len(dataset) < 2:
            return False
        y_label = np.array([ Decimal(ele) for ele in dataset ])
        x_label = np.linspace(1, y_label.size, y_label.size)
        model = LinearRegression()
        model.fit(x_label.reshape(-1, 1), y_label)
        self.model = model
        return True

    def predict(self, dataset):
        '''
        '''
        if isinstance(dataset, int):
            x_label = np.array(dataset)
        else:
            x_label = np.array([ Decimal(ele) for ele in dataset ]).reshape(-1, 1)
        if self.model:
            return self.model.predict(x_label)
        else:
            return None

    def evaluate(self, dataset):
        '''Return E(x), Var(x)'''
        return None

