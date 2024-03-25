class TP():
    def ttest(parameter_set, x_data_set):
        from scipy.stats import sem
        if len(parameter_set)==len(x_data_set):
            list0 = [parameter_set[i]/sem(x_data_set[i]) for i in range(0, len(x_data_set))] 
            for i in range(0, len(x_data_set)): print("t-score: ", list0[i])
            return list0, len(x_data_set[0])-len(parameter_set)-1#t_score_set, degree_of_freedom
        else:
            print("abnormal length of data sets.")
            return 0
    def pvalue(t_score_set, degree_of_freedom):
        import scipy.stats
        n0 = [scipy.stats.t.sf(abs(t_score_set[i]), degree_of_freedom) for i in range(0, len(t_score_set))]
        n1 = [scipy.stats.t.sf(abs(t_score_set[i]), degree_of_freedom)*2 for i in range(0, len(t_score_set))]
        #n0: p-value for one-tail test；n1: p-value for two-tails test.
        print(n0)
        print(n1)
        return n0, n1
if __name__ == "__main__":
    print("f2_0: t-statistics for each coeficient.")
    print("f2_1: p-value for each t-score from f2_0.")
    #TP.pvalue([0.00024/0.00012], 1616)
    TP.pvalue([14.09], 3)
