#-*- coding:utf-8 -*-
from decimal import Decimal
import numpy as np
from sklearn import linear_model


from BaseModel import BaseModel


class LinearRegression(BaseModel):
    def __init__(self, param = {}):
        BaseModel.__init__(self, "linear-aggregation", param)

    def train(self, dataset):
        '''
        Train the linearaggregation model.
        '''
        if len(dataset) < 2:
            return False
        y_label_raw = np.array([ Decimal(ele) for ele in dataset ])
        mu = y_label_raw.mean()
        sigma = np.sqrt(y_label_raw.var())
        # 根据 |X - mu| / sigma <= 2 进行离群值筛选过滤
        y_label = y_label_raw[(y_label_raw <= 2 * sigma + mu) & (y_label_raw >= mu - 2 * sigma)]
        print y_label_raw.size, y_label.size,

        x_label = np.linspace(1, y_label.size, y_label.size)
        model = linear_model.LinearRegression()
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

