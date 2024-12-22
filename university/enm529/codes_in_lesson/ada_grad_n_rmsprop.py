import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os
#=====================================================
# Load and Preprocess the Dataset
#=====================================================

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
current_dir = os.getcwd()

# Check if the script is being run from the correct directory
if script_dir != current_dir:
    print(f"Changing working directory from {current_dir} to {script_dir}")
    os.chdir(script_dir)

data = pd.read_csv("diabetes2.csv")
X = data.drop(columns=['Outcome']).values
y = data['Outcome'].values  # Assuming target is in {0,1}

# Standardize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#=====================================================
# Logistic Regression Loss and Gradient
#=====================================================
def logistic_loss(w, X, y):
    z = X.dot(w)
    p = 1.0/(1.0 + np.exp(-z))
    eps = 1e-12
    loss = -np.mean(y*np.log(p+eps) + (1-y)*np.log(1-p+eps))
    return loss

def logistic_grad(w, X, y):
    z = X.dot(w)
    p = 1.0/(1.0 + np.exp(-z))
    grad = X.T.dot(p - y) / X.shape[0]
    return grad

#=====================================================
# AdaGrad Implementation
#=====================================================
def adagrad(w, X, y, grad_func, alpha=0.1, epsilon=1e-8, max_iter=1000, callback=None):
    G = np.zeros_like(w, dtype=np.float64)
    for t in range(max_iter):
        g = grad_func(w, X, y)
        G += g**2
        w -= (alpha / (np.sqrt(G) + epsilon)) * g
        if callback is not None:
            callback(w, t)
    return w

#=====================================================
# RMSProp Implementation
#=====================================================
def rmsprop(w, X, y, grad_func, alpha=0.001, beta=0.9, epsilon=1e-8, max_iter=1000, callback=None):
    """
    RMSProp optimizer:
    v = beta * v + (1-beta)*g^2
    w = w - alpha * g / (sqrt(v) + epsilon)
    """
    v = np.zeros_like(w, dtype=np.float64)
    for t in range(max_iter):
        g = grad_func(w, X, y)
        v = beta * v + (1 - beta) * (g**2)
        w -= (alpha / (np.sqrt(v) + epsilon)) * g
        if callback is not None:
            callback(w, t)
    return w

#=====================================================
# Helper Functions
#=====================================================
def accuracy(w, X, y):
    z = X.dot(w)
    preds = (z >= 0).astype(int)
    return np.mean(preds == y)

def print_progress(w, iteration, X_train, y_train):
    if iteration % 100 == 0:
        current_loss = logistic_loss(w, X_train, y_train)
        print(f"Iteration {iteration}: loss = {current_loss:.4f}")

#=====================================================
# Run AdaGrad
#=====================================================
w_init = np.zeros(X_train.shape[1])
print("=== Training with AdaGrad ===")
w_adagrad = adagrad(
    w_init.copy(), X_train, y_train, logistic_grad, alpha=0.1, max_iter=1000,
    callback=lambda w, i: print_progress(w, i, X_train, y_train)
)

final_train_loss_ada = logistic_loss(w_adagrad, X_train, y_train)
final_test_loss_ada = logistic_loss(w_adagrad, X_test, y_test)
train_acc_ada = accuracy(w_adagrad, X_train, y_train)
test_acc_ada = accuracy(w_adagrad, X_test, y_test)

print("\n=== AdaGrad Results ===")
print("Optimized parameters:", w_adagrad)
print(f"Final training loss: {final_train_loss_ada:.4f}, Training accuracy: {train_acc_ada*100:.2f}%")
print(f"Final test loss: {final_test_loss_ada:.4f}, Test accuracy: {test_acc_ada*100:.2f}%")

#=====================================================
# Run RMSProp
#=====================================================
w_init = np.zeros(X_train.shape[1])
print("\n=== Training with RMSProp ===")
w_rmsprop = rmsprop(
    w_init.copy(), X_train, y_train, logistic_grad, alpha=0.001, beta=0.999, max_iter=1000,
    callback=lambda w, i: print_progress(w, i, X_train, y_train)
)

final_train_loss_rms = logistic_loss(w_rmsprop, X_train, y_train)
final_test_loss_rms = logistic_loss(w_rmsprop, X_test, y_test)
train_acc_rms = accuracy(w_rmsprop, X_train, y_train)
test_acc_rms = accuracy(w_rmsprop, X_test, y_test)

print("\n=== RMSProp Results ===")
print("Optimized parameters:", w_rmsprop)
print(f"Final training loss: {final_train_loss_rms:.4f}, Training accuracy: {train_acc_rms*100:.2f}%")
print(f"Final test loss: {final_test_loss_rms:.4f}, Test accuracy: {test_acc_rms*100:.2f}%")
