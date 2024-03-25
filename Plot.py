class PL():
    def line(coef=[0.3, 0.4], inter=1, start_date='2021-01-01',\
             end_date='2021-12-31', dep='2330.tw', indep=['2330.tw', '0050.tw']):
        import yfinance as yf
        from matplotlib import pyplot as plt
        import pandas as pd
        n0 = yf.download(dep, start_date, end_date)
        c, x = len(n0.iloc[:, 0].tolist()), inter
        if len(coef)==len(indep):
            for i in range(0, len(indep)):
                t = yf.download(indep[i], start_date, end_date)
                n1 = t.iloc[:c-1, 4]
                x += n1*coef[i]
        n2 = n0.iloc[1:, 4]
        plt.plot(x, c='blue', label='predicted data')
        plt.plot(n2, c='red', ls='--', label='real data')
        plt.legend(loc=0)
        plt.title(dep+': '+'predicted and real data')
        plt.xlabel('time')
        plt.ylabel('price', rotation=360)
        plt.show()
        return 0
    #def line_of_f1(coef=[0.3, 0.4], inter=1, start_date='2021-01-01',\
             #end_date='2021-12-31', stock='2330.tw'):
        #import yfinance as yf
        #from matplotlib import pyplot as plt
        #import pandas as pd
        #import numpy as np
        #n0 = yf.download(stock, start_date, end_date)
        #c, x, list0 = len(n0.iloc[:, 0].tolist()), inter, []
        #n1 = n0.iloc[:c-1, 3]
        #n2 = n0.iloc[2:, 3]
        #n3 = n0.iloc[:, 5]
        #print(n3)
        #n4, n5 = n3.tolist(), n3.index
        #print(n4)
        #print(n5)
        #for i in range(1, len(n3)):
            #if n3[i]>=n3[i-1]: list0.append(1)
            #else: list0.append(0)
        #print(list0)
        #n6 = pd.DataFrame({'vd':list0}, index=n3.index)
        #print(n6)
        #print(n1*coef[0], n6*coef[1])
        #print(inter+n1*coef[0]+n6*coef[1])
        #plt.plot(x, c='blue', label='predicted data')
        #plt.plot(n2, c='red', ls='--', label='real data')
        #plt.legend(loc=0)
        #plt.title(stock+': '+'predicted and real data')
        #plt.xlabel('time')
        #plt.ylabel('price', rotation=360)
        #plt.show()
        #return 0
if __name__=="__main__":
    print('plot function')
    PL.line()
    #PL.line_of_f1()
