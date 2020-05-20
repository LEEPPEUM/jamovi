from django.shortcuts import render

import pandas as pd

bike = pd.read_csv('day.csv')
bike = pd.DataFrame(bike)
bike_y = bike['cnt']
bike_x = bike[['hum','windspeed','atemp','season','weathersit']]
bike_x = pd.get_dummies(bike_x, prefix=['season','weathersit'], drop_first=True)

train_bike_x[0] = x1
train_bike_x[1] = x2
train_bike_x[2] = x3
train_bike_x[3] = x4
train_bike_x[4] = x5
train_bike_x[5] = x6
train_bike_x[6] = x7
train_bike_x[7] = x8
train_bike_y = y

from sklearn.model_selection import train_test_split
train_bike_x, test_bike_x, train_bike_y, test_bike_y = train_test_split(bike_x, bike_y, test_size=0.3)

from sklearn.linear_model import Lasso

lasso = Lasso()
lasso.fit(train_bike_x, train_bike_y)
lasso.score(test_bike_x, test_bike_y)
lasso.intercept_, lasso.coef_

class BIKE:
    def __init__(self,x1,x2,x3,x4,x5,x6,x7,x8,y):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.x6 = x6
        self.x7 = x7
        self.x8 = x8
        self.y = y
    def calculate(self)
        lasso = Lasso()
        y = lasso.intercept_ + lasso.coef_[0]*x1 + lasso.coef_[1]*x2 + lasso.coef_[2]*x3 + lasso.coef_[3]*x4 + lasso.coef_[4]*x5 + lasso.coef_[5]*x6 + lasso.coef_[6]*x7 + lasso.coef_[7]*x8

b = BIKE()
b.calculate()
print(b.calculate())

import pickle
from django.http import JsonResponse

pickle.dump(b, open("./bike.pkl", "wb"))
b_pkl = pickle.load(open("./bike.pkl", "rb"))
b_pkl.calculate()

def home(request):
    x1_ = request.GET['x1']
    x2_ = request.GET['x2']
    x3_ = request.GET['x3']
    x4_ = request.GET['x4']
    x5_ = request.GET['x5']
    x6_ = request.GET['x6']
    x7_ = request.GET['x7']
    x8_ = request.GET['x8']
    b_pkl = pickle.load(open("./bike.pkl", "rb"))
    b_pkl = BIKE(int(x1_),int(x2_))
    result = b_pkl.calculate()
    requestDict = {'result_response':result}
    return JsonResponse(requestDict)



# class BIKE_2():
#     def __init__(self, train_bike_x, train_bike_y):
#         self.train_bike_x = train_bike_x
#         self.train_bike_y = train_bike_y
#     def calculate(self)6
#         train_bike_y = lasso.intercept_ + train_bike_x



