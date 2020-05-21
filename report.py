from django.shortcuts import render

import pandas as pd
bike = pd.read_csv('day.csv')
bike = pd.DataFrame(bike)
bike_y = bike['cnt']
bike_x = bike[['hum','windspeed','atemp','season','weathersit']]
bike_x = pd.get_dummies(bike_x, columns=['season','weathersit'], drop_first=True)

from sklearn.model_selection import train_test_split
train_bike_x, test_bike_x, train_bike_y, test_bike_y = train_test_split(bike_x, bike_y, test_size=0.3)

from sklearn.linear_model import Lasso
lasso = Lasso()
lasso.fit(train_bike_x, train_bike_y)
lasso.score(test_bike_x, test_bike_y)
lasso.intercept_, lasso.coef_

a = lasso.coef_[0]
b = lasso.coef_[1]
c = lasso.coef_[2]
d = lasso.coef_[3]
e = lasso.coef_[4]
f = lasso.coef_[5]
g = lasso.coef_[6]
h = lasso.coef_[7]

class BIKE:
    def __init__(self,x1,x2,x3,x4,x5,x6,x7,x8):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.x6 = x6
        self.x7 = x7
        self.x8 = x8
    def calculate(self):
        y = lasso.intercept_ + lasso.coef_[0]*self.x1 + lasso.coef_[1]*self.x2 + lasso.coef_[2]*self.x3 + lasso.coef_[3]*self.x4 
            + lasso.coef_[4]*self.x5 + lasso.coef_[5]*self.x6 + lasso.coef_[6]*self.x7 + lasso.coef_[7]*self.x8
        return y

bike = BIKE(0.677,0.888,0.146,0,0,1,1,0)
bike.calculate()
print(bike.calculate())

import pickle
from django.http import JsonResponse

pickle.dump(bike, open("./bike.pkl", "wb"))
bike_pkl = pickle.load(open("./bike.pkl", "rb"))
print(bike_pkl.calculate())



















# BIKE('hum', 'windspeed', 'atemp', 'season_spring', 'season_summer', 'season_winter', 'weathersit_light_rain', 'weathersit_mist')
# bike = BIKE(x1,x2,x3,x4,x5,x6,x7,x8)
# bike.calculate()
# print(bike.calculate())

# import pickle
# from django.http import JsonResponse

# pickle.dump(bike, open("./bike.pkl", "wb"))
# bike_pkl = pickle.load(open("./bike.pkl", "rb"))
# bike_pkl.calculate()

# print(bike_pkl.calculate())
# print(bike_pkl.calculate(0.805833,0.160446,0.363625,1,0,0,0,1))
# print(bike_pkl.calculate(0.677,0.888,0.146,0,0,1,1,0))


# a = BIKE(0.805833,0.160446,0.363625,1,0,0,0,1)
# b = BIKE(0.677,0.888,0.146,0,0,1,1,0)
# a.calculate()
# b.calculate()
# print(a.calculate())
# print(b.calculate())

# import pickle
# from django.http import JsonResponse

# pickle.dump(a, open("./bike.pkl", "wb"))
# a_pkl = pickle.load(open("./bike.pkl", "rb"))
# a_pkl.calculate()
# print(a_pkl.calculate())


# b = BIKE(0.677,0.888,0.146,0,0,1,1,0)
# b.calculate()
# # print(b.calculate())

# pickle.dump(b, open("./bike_b.pkl", "wb"))
# b_pkl = pickle.load(open("./bike_b.pkl", "rb"))
# b_pkl.calculate()
# print(b_pkl.calculate())

# def home(request):
#     x1_ = request.GET['x1']
#     x2_ = request.GET['x2']
#     x3_ = request.GET['x3']
#     x4_ = request.GET['x4']
#     x5_ = request.GET['x5']
#     x6_ = request.GET['x6']
#     x7_ = request.GET['x7']
#     x8_ = request.GET['x8']
#     b_pkl = pickle.load(open("./bike_b.pkl", "rb"))
#     b_pkl = BIKE(int(x1_),int(x2_))
#     result = b_pkl.calculate()
#     requestDict = {'result_response':result}
#     return JsonResponse(requestDict)




