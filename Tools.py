class TL():
    def stdnor_cdf(inter=1, coef=[0.5, 0.4], data=[1, 0]):
        from scipy import stats
        if len(coef) == len(data):
            n0 = inter + sum([coef[i]*data[i] for i in range(0, len(data))])
        print("probit model: ", stats.norm.cdf(n0, 0, 1))
        return stats.norm.cdf(n0, 0, 1)
    def logit_model(inter=1, coef=[0.5, 0.4], data=[1, 0]):
        import math
        if len(coef) == len(data):
            n0 = inter + sum([coef[i]*data[i] for i in range(0, len(data))])
        print("logit model: ", math.exp(n0)/(1+math.exp(n0)))
        return math.exp(n0)/(1+math.exp(n0))
    def pseudo_r_squared(x, y, inter, coef, Type='logit'):
        import math
        from scipy import stats
        if Type == 'logit':
            X = []
            for i in range(0, len(x)):
                t0 = sum([x[i][j]*inter[j] for j in range(0, len(x[i]))])
                t1 = math.exp(t0)/(1+math.exp(t0))
                X.append(t1)
        if Type == 'probit':
            X = []
            for i in range(0, len(x)):
                t0 = sum([x[i][j]*inter[j] for j in range(0, len(x[i]))])
                t1 = stats.norm.cdf(t0, 0, 1)
                X.append(t1)
        lu = sum([y[i]*math.log(X)+(1-y[i])*(1-X) for i in range(0, len(x))])
        ln = sum([y[i]*math.log(inter)+(1-y[i])*(1-inter) for i in range(0, len(x))])
        print("R_squared under "+Type+" model: ", 1-lu/ln)
        return 1-(lu/ln)
if __name__=="__main__":
    TL.stdnor_cdf()
    TL.logit_model()
