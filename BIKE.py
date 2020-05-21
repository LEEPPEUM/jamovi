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
        y = lasso.intercept_ + lasso.coef_[0]*self.x1 + lasso.coef_[1]*self.x2 + lasso.coef_[2]*self.x3 + lasso.coef_[3]*self.x4 + lasso.coef_[4]*self.x5 + lasso.coef_[5]*self.x6 + lasso.coef_[6]*self.x7 + lasso.coef_[7]*self.x8
        return y

b = BIKE(0.805833,0.160446,0.363625,1,0,0,0,1)
b.calculate()


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