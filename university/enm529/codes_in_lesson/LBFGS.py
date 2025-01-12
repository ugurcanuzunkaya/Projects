import numpy as np
import pandas as pd
import timeit
from regex import P
from sklearn.model_selection import KFold
from sklearn.utils import shuffle

def deriv_SVM_i(w,y,x,m,n,i):
    deriv=np.zeros((n+1),dtype=float)
    if 1-y[i]*(sum(w[j]*x[i][j] for j in range (n))+w[n])>0:
        for j in range(n):
            deriv[j]=(-y[i]*x[i][j])+((1/m)*w[j])
        deriv[n]=-y[i]
    else:
        for j in range(n):
            deriv[j]=((1/m)*w[j])
        deriv[n]=0
    return deriv

def LBFGS_two_loop(g,P_y,P_s, k, m_tilda):
    print(f"LBFGS_two_loop: k={k}")
    q = np.copy(g)
    n=len(g)
    alpha = np.zeros(k, dtype=float)
    i_upper = len(P_s) - 1
    for i in range(i_upper, -1, -1):
        alpha[i] = np.dot(P_s[i], q) / np.dot(P_y[i], P_s[i])
        q = q - alpha[i] * P_y[i]
    if k>0:
        B_k = np.dot(np.dot(P_s[i_upper], P_y[i_upper]) / np.dot(P_y[i_upper], P_y[i_upper]), np.identity(n))
    else:
        B_k = np.identity(n)
    d = np.dot(B_k, q)
    for i in range(i_upper+1):
        beta = np.dot(P_y[i], d) / np.dot(P_y[i], P_s[i])
        d = d + P_s[i] * (alpha[i] - beta)
    return d


def LBFGS(w_0,y,x):
    print("LBFGS")
    w = np.copy(w_0)
    m = len(y)
    n = len(x[0])
    P_y = []
    P_s = []
    iter_num=2*m
    learning_rate = 0.1
    m_tilda = 10
    for k in range(iter_num):
        i = np.random.randint(0, m)
        g_i = deriv_SVM_i(w, y, x, m, n, i)
        d_k = LBFGS_two_loop(g_i, P_y, P_s, k, m_tilda)
        w = w - learning_rate * d_k
        if np.mod(k, m_tilda) == 0:
            s_k = d_k * learning_rate * -1
            y_k = deriv_SVM_i(w, y, x, m, n, i) - g_i
            P_s.append(s_k)
            P_y.append(y_k)
            if k > m_tilda:
                P_s.pop(0)
                P_y.pop(0)
    return w


def accuracy_SVM(w,x,y_true):
    y_pred=list()
    m=len(x)
    n=len(x[0])
    succ=0
    for i in range(m):
        if sum(w[j]*x[i][j] for j in range (n))+w[n]>0:
            y_pred.append(1)
        else:
            y_pred.append(-1)
        if y_pred[i]==y_true[i]: succ=succ+1
    accur=succ/m
    return accur

data=pd.read_csv(r"university/enm529/codes_in_lesson/diabetes2.csv")
x_ML,y_ML=np.array(data.iloc[0:,:-1]), np.array(data.iloc[0:,-1])
m=len(y_ML)
n=len(x_ML[0])
for i in range(m):
    if y_ML[i]==0: y_ML[i]=-1
x_ML=(x_ML-x_ML.min(axis=0))/(x_ML.max(axis=0)-x_ML.min(axis=0))
"""
w_0=[1 for j in range (n+1)]
w=GD(w_0,10000,10**-5,0.1,y_ML,x_ML)
print(w)
print(accuracy_SVM(w,x_ML,y_ML))
"""
kf=KFold(n_splits=10)
per_train=0
per_test=0
CPU_total=0
count=0
accur_train_total=0
accur_test_total=0
w_total = [0 for j in range(n + 1)]
for train,test in kf.split(x_ML):
    x_train,x_test,y_train,y_test=x_ML[train],x_ML[test],y_ML[train],y_ML[test]
    w_0 = [1 for j in range(n + 1)]
    count=count+1
    start=timeit.default_timer()
    #w = GD(w_0, 10000, 10 ** -5, 0.1, y_train, x_train)
    #w = SVRG(w_0,y_train, x_train)
    # w = AdaGrad(w_0,y_train, x_train)
    # w = RMSProp(w_0,y_train, x_train)
    w = LBFGS(w_0,y_train, x_train)
    CPU=timeit.default_timer()-start
    CPU_total=CPU_total+CPU
    accur_train=accuracy_SVM(w,x_train,y_train)
    accur_test=accuracy_SVM(w,x_test,y_test)
    print("Fold: ", count, "Training accuracy: ", accur_train, "Testing accuracy: ", accur_test, "CPU time: ", CPU)
    accur_train_total=accur_train_total+accur_train
    accur_test_total = accur_test_total + accur_test
    w_total=np.add(w_total,w)
accur_train_aver=accur_train_total/count
accur_test_aver=accur_test_total/count
CPU_total_aver=CPU_total/count
w_aver=w_total/count
print(f"Average training accuracy: {accur_train_aver*100:.2f}%, Average testing accuracy: {accur_test_aver*100:.2f}%, Average CPU time: {CPU_total_aver}, Average weight: {w_aver}")

