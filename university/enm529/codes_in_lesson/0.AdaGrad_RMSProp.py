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

def AdaGrad(w_0, y, x, learning_rate=0.01, max_iter=1000, epsilon=1e-8):
    """
    AdaGrad optimization for SVM using deriv_SVM_i
    """
    w = np.array(w_0, dtype=float)
    m = len(y)
    n = len(x[0])
    G = np.zeros(n + 1)  # Include bias term
    
    for t in range(max_iter):
        grad = np.zeros(n + 1)
        
        # Compute gradient using deriv_SVM_i
        for i in range(m):
            grad += deriv_SVM_i(w, y, x, m, n, i)
        
        # Update accumulated squared gradients
        G += grad * grad
        
        # Update weights using AdaGrad rule
        adj_grad = grad / (np.sqrt(G) + epsilon)
        w -= learning_rate * adj_grad
        
        # Optional: add convergence check
        if np.linalg.norm(grad) < 1e-5:
            break
            
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

data=pd.read_csv("university/enm529/codes_in_lesson/diabetes2.csv")
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
    w = AdaGrad(w_0, y_train, x_train)
    CPU=timeit.default_timer()-start
    CPU_total=CPU_total+CPU
    accur_train=accuracy_SVM(w,x_train,y_train)
    accur_test=accuracy_SVM(w,x_test,y_test)
    print(count, accur_train,accur_test, CPU)
    accur_train_total=accur_train_total+accur_train
    accur_test_total = accur_test_total + accur_test
    w_total=np.add(w_total,w)
accur_train_aver=accur_train_total/count
accur_test_aver=accur_test_total/count
CPU_total_aver=CPU_total/count
w_aver=w_total/count
print(accur_train_aver,accur_test_aver,CPU_total_aver, w_aver)


