import numpy as np
import pandas as pd
import timeit
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

def AdaGrad(w_0,y,x):
    w = np.copy(w_0)
    m = len(y)
    n = len(x[0])
    iter_num=2*m
    learning_rate = 0.1
    g_k = np.zeros((n + 1), dtype=float)
    R_k = np.zeros((n + 1), dtype=float)
    for k in range(iter_num):
        i=np.random.randint(m)
        g_k=deriv_SVM_i(w,y,x,m,n,i)
        R_k=np.add(R_k,g_k**2)
        w=w-(learning_rate/(R_k**0.5+10**-8))*g_k
    return w


def RMSPRop(w_0,y,x):
    w = np.copy(w_0)
    m = len(y)
    n = len(x[0])
    iter_num=2*m
    learning_rate = 0.1
    g_k = np.zeros((n + 1), dtype=float)
    R_k = np.zeros((n + 1), dtype=float)
    gamma = 0.9
    for k in range(iter_num):
        i=np.random.randint(m)
        g_k=deriv_SVM_i(w,y,x,m,n,i)
        R_k=np.add(gamma*R_k,(1-gamma)*(g_k**2))
        w=w-(learning_rate/(R_k**0.5+10**-8))*g_k
    return w


def SVRG(w_0,y,x):
    w = np.copy(w_0)
    m = len(y)
    n = len(x[0])
    sub_m=int(m**0.5)
    iter_num=m
    subiter_num=int(m/sub_m)
    learning_rate=0.1
    g_k = np.zeros((n + 1), dtype=float)
    for k in range(iter_num):
        R_k = np.zeros((n + 1), dtype=float)
        x, y = shuffle(x, y, random_state=0)
        for i in range(sub_m):
            R_k=np.add(R_k,deriv_SVM_i(w,y,x,m,n,i))
        R_k=R_k*(1/sub_m)
        sub_w=np.copy(w)
        for j in range(subiter_num):
            k_j=np.random.randint(sub_m)
            g_k=np.add(np.subtract(R_k,deriv_SVM_i(w,y,x,m,n,k_j)),deriv_SVM_i(sub_w,y,x,m,n,k_j))
            sub_w=sub_w-learning_rate*g_k
        w=np.copy(sub_w)
    return w

def GD(w_0,iter_num,epsilon,learning_rate,y,x):
    w=np.copy(w_0)
    m=len(y)
    n=len(x[0])
    grad_SVM=np.zeros((n+1),dtype=float)
    for iter in range (iter_num):
        for i in range(m):
            grad_SVM=np.add(grad_SVM,deriv_SVM_i(w,y,x,m,n,i))
        grad_SVM=(1/m)*grad_SVM
        norm_grad=sum(grad_SVM[j]**2 for j in range(n+1))*0.5
        if norm_grad<epsilon:
            return w
        w=w-learning_rate*grad_SVM
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
    w = RMSPRop(w_0,y_train, x_train)
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

