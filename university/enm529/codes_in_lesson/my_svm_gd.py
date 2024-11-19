import numpy as np
import pandas as pd
import time
from sklearn.model_selection import KFold


def deriv_SVM_i(w, y, x, m, n, i):
    deriv = np.zeros((n + 1), dtype=float)
    if 1 - y[i] * (sum(w[j] * x[i][j] for j in range(n)) + w[n]) > 0:
        for j in range(n):
            deriv[j] = (-y[i] * x[i][j]) + ((1 / m) * w[j])
        deriv[n] = -y[i]
    else:
        for j in range(n):
            deriv[j] = ((1 / m) * w[j])
        deriv[n] = 0
    return deriv

def GD(w_0, iter_num, epsilon, learning_rate, y, x, printed=False):
    w = np.copy(w_0)
    m = len(y)
    n = len(x[0])
    grad_SVM = np.zeros((n + 1), dtype=float)
    
    for iter in range(iter_num):
        for i in range(m):
            grad_SVM = np.add(grad_SVM, deriv_SVM_i(w, y, x, m, n, i))
        grad_SVM = (1 / m) * grad_SVM
        norm_grad = sum(grad_SVM[j] ** 2 for j in range(n + 1)) * 0.5
        if norm_grad < epsilon:
            return w
        w = w - learning_rate * grad_SVM
        if printed:
            print(f"iter: {iter}, norm_grad: {norm_grad}")
    return w

data = pd.read_csv(r"university/enm529/codes_in_lesson/diabetes2.csv")
x_ML, y_ML = np.array(data.iloc[0:, :-1]), np.array(data.iloc[0:, -1])
m = len(y_ML)
n = len(x_ML[0])

for i in range(m):
    if y_ML[i] == 0:
        y_ML[i] = -1
x_ML = (x_ML - x_ML.min(axis=0)) / (x_ML.max(axis=0) - x_ML.min(axis=0))

w_0 = [1 for _ in range(n + 1)]
start = time.time()
weight = GD(w_0, 10000, 10**-5, 0.1, y_ML, x_ML)
print(f"CPU time: {time.time() - start}")

def accuracy(w, x, y_true):
    m = len(x)
    n = len(x[0])
    y_pred = np.zeros(m)
    for i in range(m):
        if sum(w[j] * x[i][j] for j in range(n)) + w[n] > 0:
            y_pred[i] = 1
        else:
            y_pred[i] = -1
    return sum(y_pred[i] == y_true[i] for i in range(m)) / m

accuracy_gd = accuracy(weight, x_ML, y_ML)

print(f"weight: {weight}, \naccuracy: {accuracy_gd}")

split_num = 10
kf_fold = KFold(n_splits=split_num, shuffle=True, random_state=42)
per_train = 0
per_test=0
CPU_total = 0
per_w = np.zeros(n + 1)
for count, (train, test) in enumerate(kf_fold.split(x_ML), start=1):
    x_train, x_test, y_train, y_test = x_ML[train], x_ML[test], y_ML[train], y_ML[test]
    w_0 = [1 for _ in range(n + 1)]
    start = time.time()
    w = GD(w_0, 10000, 10**-5, 0.1, y_train, x_train)
    cpu_time = time.time() - start
    CPU_total += round(cpu_time, 2)
    accur_train = accuracy(w, x_train, y_train)
    accur_test = accuracy(w, x_test, y_test)
    per_train += accur_train
    per_test += accur_test
    per_w += w
    print(f"Fold {count}, CPU time: {cpu_time}, accuracy_train: {accur_train}, accuracy_test: {accur_test}")
    print(f"weight: {w}")

print(f"Average CPU time: {CPU_total / split_num}, average accuracy_train: {per_train / split_num}, average accuracy_test: {per_test / split_num}")
print(f"Average weight: {per_w / split_num}")