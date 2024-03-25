class LR():
    def f0(stock_symbol="2330.tw", start_date="2021-01-01", end_date="2021-12-31"):
        import yfinance, time, os
        import pandas as pd
        from sklearn.model_selection import train_test_split 
        from sklearn.linear_model import LinearRegression
        n0 = yfinance.download(stock_symbol, start=start_date, end=end_date)
        x = len(n0.iloc[:, 4].tolist())
        n1, n2 = n0.iloc[:x-1, 3].values, n0.iloc[1:, 3].values
        n3 = pd.DataFrame({"indep": n1, "dep": n2})
        n3.to_csv('tempf0.csv')
        n0=pd.read_csv('tempf0.csv')
        n1, n2 = n0['indep'].values.reshape(-1,1), n0['dep'].values.reshape(-1,1)
        X_train, X_test, y_train, y_test = train_test_split(n1, n2, test_size=0.2, random_state=0)
        regressor = LinearRegression()  
        reg=regressor.fit(X_train, y_train)
        print("R_squared: ", regressor.score(X_train, y_train))
        print("coeficient: ", reg.coef_)
        print("intercept: ", reg.intercept_)
        os.remove('tempf0.csv')
        n3 = reg.coef_.tolist()
        return n3[0], [list(n0['indep'].values)], reg.intercept_[0]
    def f0m(stock_symbol="2330.tw", index_symbol='0050.tw',\
              start_date="2021-01-01", end_date="2021-11-30"):
        import yfinance, os
        import pandas as pd
        from sklearn.model_selection import train_test_split 
        from sklearn.linear_model import LinearRegression
        n0 = yfinance.download(stock_symbol, start=start_date, end=end_date)
        n1 = yfinance.download(index_symbol, start=start_date, end=end_date)
        x = len(n0.iloc[:, 4].tolist())
        n1, n2 = n1.iloc[:x-1, 3].values, n0.iloc[1:, 3].values
        n3 = pd.DataFrame({"indep": n1, "dep": n2})
        n3.to_csv('tempf0m.csv')
        n0=pd.read_csv('tempf0m.csv')
        n1, n2 = n0['indep'].values.reshape(-1,1), n0['dep'].values.reshape(-1,1)
        X_train, X_test, y_train, y_test = train_test_split(n1, n2, test_size=0.2, random_state=0)
        regressor = LinearRegression()  
        reg=regressor.fit(X_train, y_train)
        print("R_squared: ", regressor.score(X_train, y_train))
        print("coeficient: ", reg.coef_)
        print("intercept: ", reg.intercept_)
        os.remove('tempf0m.csv')
        n3 = reg.coef_.tolist()
        return n3[0], [list(n0['indep'].values)], reg.intercept_[0]
    def f0m2(stock_symbol='2330.tw', index_symbol_1='0050.tw', index_symbol_2='^GSPC',\
              start_date='2021-01-01', end_date="2021-11-30"):
        import yfinance, os
        import pandas as pd
        from sklearn.model_selection import train_test_split 
        from sklearn.linear_model import LinearRegression
        n0 = yfinance.download(stock_symbol, start=start_date, end=end_date)
        n1 = yfinance.download(index_symbol_1, start=start_date, end=end_date)
        n1s = yfinance.download(index_symbol_2, start=start_date, end=end_date)
        x = len(n0.iloc[:, 4].tolist())
        n1, n2, n3 = n1.iloc[:x-1, 3].values, n1s.iloc[:x-1, 3].values, n0.iloc[1:, 3].values
        n4 = pd.DataFrame({'indep1': n1, 'indep2': n2, 'dep': n3})
        n4.to_csv('tempf0m.csv')
        n0=pd.read_csv('tempf0m.csv')
        n1, n2 = n0.iloc[:, 1:3].values, n0['dep'].values.reshape(-1,1)
        X_train, X_test, y_train, y_test = train_test_split(n1, n2, test_size=0.2, random_state=0)
        regressor = LinearRegression()  
        reg=regressor.fit(X_train, y_train)
        print("R_squared: ", regressor.score(X_train, y_train))
        print("coeficient: ", reg.coef_)
        print("intercept: ", reg.intercept_)
        os.remove('tempf0m.csv')
        n3 = reg.coef_.tolist()
        return n3[0], [list(n0['indep1'].values), list(n0['indep2'].values)], reg.intercept_[0]
    def f1(stock_symbol="2330.tw", start_date="2021-01-01", end_date="2021-12-31"):
        import yfinance, os
        import pandas as pd
        from sklearn.model_selection import train_test_split 
        from sklearn.linear_model import LinearRegression
        n0 = yfinance.download(stock_symbol, start=start_date, end=end_date)
        x = len(n0.iloc[:, 4].tolist())
        n1, n2= n0.iloc[1:x-1, 3].values, n0.iloc[2:, 3].values#n1: y_t-1, n2: y_t
        n3 = n0["Volume"].shift(1) - n0["Volume"]#n3: dummy variable for difference of volume
        n3 = n3.dropna().tolist()
        n3 = n3[:len(n3)-1]
        for i in range(0, len(n3)):
            if n3[i]>=0: n3[i]=1
            else: n3[i]=0
        n4 = pd.DataFrame({"indep1": n1, "indep2": n3, "dep": n2})
        n4.to_csv('tempf1.csv')
        n0=pd.read_csv('tempf1.csv')
        n1, n2=n0.iloc[:, 1:3].values,n0['dep'].values.reshape(-1,1)
        X_train, X_test, y_train, y_test = train_test_split(n1, n2, test_size=0.2, random_state=0)
        regressor = LinearRegression()  
        reg = regressor.fit(X_train, y_train)
        print("R_squared: ", regressor.score(X_train, y_train))
        print("coeficient: ", reg.coef_)
        print("intercept", reg.intercept_)
        os.remove('tempf1.csv')
        n3 = reg.coef_.tolist()
        n4 = [list(n0['indep1'].values), list(n0['indep2'].values)]
        return n3[0], n4
    def f3(stock_symbol="2330.tw", start_date="2021-01-01", end_date="2021-12-31"):
        import yfinance, os
        import pandas as pd
        import numpy as np
        from sklearn.model_selection import train_test_split 
        from sklearn.linear_model import LinearRegression
        n0 = yfinance.download(stock_symbol, start=start_date, end=end_date)
        n1 = (n0['Close'].shift(1) - n0['Close'])
        n2 = (n1/n0['Close'])*100
        n1 = n1.dropna().tolist()
        n3 = (n0['Volume'].shift(1) - n0['Volume']).dropna().tolist()
        if len(n1)==len(n3):
            list0, list1, list2 = [0]*len(n1), [0]*len(n1), [0]*len(n1)
            for i in range(0, len(n1)):  
                if n1[i]>=0 and n3[i]>0: list0[i] = 1
                elif n1[i]>=0 and n3[i]<0: list1[i] = 1
                elif n1[i]<=0 and n3[i]>0: list2[i] = 1
        n6 = pd.DataFrame({'d1': list0, 'd2': list1, 'd3': list2, 'dep': n2.dropna()})
        n6.to_csv('tempf3.csv')
        n0=pd.read_csv('tempf3.csv')
        c = len(n0.iloc[:, 0].tolist())
        n1, n2=n0.iloc[:c-1, 1:4].values, n0.iloc[1:, 4].values.reshape(-1,1)
        X_train, X_test, y_train, y_test = train_test_split(n1, n2, test_size=0.2, random_state=0)
        regressor = LinearRegression()  
        reg = regressor.fit(X_train, y_train)
        print("R_squared: ", regressor.score(X_train, y_train))
        print("coeficient: ", reg.coef_)
        print("intercept", reg.intercept_)
        os.remove('tempf3.csv')
        n3 = reg.coef_.tolist()
        n4 = [list(n0['d1'].values), list(n0['d2'].values), list(n0['d3'].values)]
        return n3[0], n4, reg.intercept_[0]
    def f4(stock_symbol="2330.tw", start_date="2021-01-01", end_date="2021-12-31"):
        import yfinance, os
        import pandas as pd
        import numpy as np
        from sklearn.model_selection import train_test_split 
        from sklearn.linear_model import LinearRegression
        n0 = yfinance.download(stock_symbol, start=start_date, end=end_date)
        n1 = (n0['Close'].shift(1) - n0['Close'])
        n2 = (n1/n0['Close']).dropna().tolist()
        n1 = n1.dropna().tolist()
        n3 = (n0['Volume'].shift(1) - n0['Volume']).dropna().tolist()
        if len(n1)==len(n3) and len(n1)==len(n2):
            list0, list1, list2, list3 = [0]*len(n1), [0]*len(n1), [0]*len(n1), [0]*len(n1)
            for i in range(0, len(n1)):
                if n2[i] >= 0: list3[i] = 1
            for i in range(0, len(n1)):  
                if n1[i]>=0 and n3[i]>0: list0[i] = 1
                elif n1[i]>=0 and n3[i]<0: list1[i] = 1
                elif n1[i]<=0 and n3[i]>0: list2[i] = 1
        n6 = pd.DataFrame({'d1': list0, 'd2': list1, 'd3': list2, 'dep': list3})
        n6.to_csv('tempf4.csv')
        n0=pd.read_csv('tempf4.csv')
        c = len(n0.iloc[:, 0].values)
        n1, n2=n0.iloc[:c-1, 1:4].values, n0.iloc[1:, 4].values.reshape(-1,1)
        X_train, X_test, y_train, y_test = train_test_split(n1, n2, test_size=0.2, random_state=0)
        regressor = LinearRegression()  
        reg = regressor.fit(X_train, y_train)
        print("coeficient: ", reg.coef_)
        print("intercept", reg.intercept_)
        os.remove('tempf4.csv')
        n3 = reg.coef_.tolist()
        n4 = [list(n0['d1'].values), list(n0['d2'].values), list(n0['d3'].values)]
        return n3[0], n4
if __name__ == "__main__":
    print("The default takes the close price of 2330.tw during 2021/01/01 to 2021/12/31")
    LR.f0()
    LR.f0m()
    LR.f0m2()
    LR.f1()
    LR.f3()
    LR.f4()
