#-*- coding:utf-8 -*-
import numpy as np
from scipy.optimize import curve_fit

from BaseModel import BaseModel


class SinRegression(BaseModel):
    def __init__(self, param = {}):
        BaseModel.__init__(self, "sin-regression", param)
        self.coefs = None
        self._predict = None

    def _sin_func(self, x, a, b, c, T=2*np.pi/23):
        return a * np.sin(T*x) + b * x + c

    def train(self, Y, T = 2 * np.pi / 23):
        '''
        Train the SinRegression model.
        '''
        if len(Y) < 2:
            return False
        y_label = np.array([ float(ele) for ele in Y ])
        x_label = np.linspace(1, y_label.size, y_label.size)

        cnt_max = y_label.size * T / (2 * np.pi) + 1
        y_sorted = np.sort(y_label)
        y_max_mean = y_sorted[-cnt_max:].mean()
        y_min_mean = y_sorted[:cnt_max].mean()
        a = -(y_max_mean - y_min_mean) / 2
        b = 0
        c = y_min_mean - a

        def fit_func(x, alpha, beta):
            return a * np.sin(T * (x+alpha)) + b * x + c + beta
        coefs, _ = curve_fit(fit_func, x_label, y_label)

        def sin_predict(x):
            return fit_func(x, coefs[0], coefs[1])
        self.coefs = coefs
        self._predict = sin_predict
        margin = np.sqrt((sin_predict(x_label)-y_label).var())
        self.margin = margin
        return True

    def predict(self, X):
        '''
        '''
        if isinstance(X, int):
            x_label = np.array(X)
        else:
            x_label = np.array([ float(ele) for ele in X ]).reshape(-1, 1)
        if self._predict:
            return self._predict(x_label)
        else:
            return None

    def predict_range(self, X): 
        y_predict = self.predict(X)
        y_upper = y_predict + self.margin
        y_lower = y_predict - self.margin
        return (y_lower, y_upper)

