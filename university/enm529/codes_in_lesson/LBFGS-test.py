import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler

# Define SVM loss function and its gradient
def svm_loss_and_grad(w, X, y, C=1.0):
    """
    SVM loss function and gradient.
    
    Parameters:
        w (np.array): Weight vector.
        X (np.array): Feature matrix.
        y (np.array): Target vector (-1 or 1).
        C (float): Regularization parameter.
    
    Returns:
        loss (float): SVM loss value.
        grad (np.array): Gradient of the loss with respect to weights.
    """
    n_samples, n_features = X.shape
    margins = 1 - y * (X @ w)
    loss = 0.5 * np.dot(w, w) + C * np.maximum(0, margins).sum()
    grad = w - C * np.dot(X.T, (margins > 0) * y)
    return loss, grad

# Define accuracy function
def compute_accuracy(w, X, y):
    """
    Compute accuracy of SVM.
    
    Parameters:
        w (np.array): Weight vector.
        X (np.array): Feature matrix.
        y (np.array): Target vector (-1 or 1).
    
    Returns:
        float: Accuracy score.
    """
    predictions = np.sign(X @ w)
    return np.mean(predictions == y)

def lbfgs_two_loop(g, s_list, y_list):
    """
    LBFGS two-loop recursion for approximating the inverse Hessian-vector product.
    
    Parameters:
        g (np.array): Gradient vector.
        s_list (list of np.array): List of position differences (x_{k+1} - x_k).
        y_list (list of np.array): List of gradient differences (g_{k+1} - g_k).
        
    Returns:
        np.array: Updated direction vector.
    """
    q = g.copy()
    alpha_list = []
    rho_list = []
    
    # Calculate step lengths
    for s, y in zip(reversed(s_list), reversed(y_list)):
        rho = 1.0 / np.dot(y, s)
        alpha = rho * np.dot(s, q)
        q -= alpha * y
        alpha_list.append(alpha)
        rho_list.append(rho)
    
    # Initial Hessian approximation as identity
    if len(s_list) > 0:
        gamma = np.dot(s_list[-1], y_list[-1]) / np.dot(y_list[-1], y_list[-1])
    else:
        gamma = 1.0  # Default scaling factor
    r = gamma * q

    # Second loop
    for s, y, alpha, rho in zip(s_list, y_list, reversed(alpha_list), reversed(rho_list)):
        beta = rho * np.dot(y, r)
        r += s * (alpha - beta)
    
    return -r  # Negative for descent direction

def lbfgs_optimize(f, grad, x0, max_iter=100, tol=1e-6, m=10):
    """
    LBFGS optimization algorithm.
    
    Parameters:
        f (function): Objective function to minimize.
        grad (function): Gradient of the objective function.
        x0 (np.array): Initial guess.
        max_iter (int): Maximum number of iterations.
        tol (float): Convergence tolerance.
        m (int): Memory size for storing past updates.
        
    Returns:
        np.array: Optimized solution.
    """
    x = x0
    s_list = []
    y_list = []
    prev_grad = grad(x)
    
    for k in range(max_iter):
        # Compute search direction using LBFGS two-loop recursion
        if k == 0:
            direction = -prev_grad  # Steepest descent for the first iteration
        else:
            direction = lbfgs_two_loop(prev_grad, s_list, y_list)
        
        # Line search (simple backtracking)
        step_size = 1.0
        while f(x + step_size * direction) > f(x) + 1e-4 * step_size * np.dot(prev_grad, direction):
            step_size *= 0.5
        
        # Update position
        x_new = x + step_size * direction
        grad_new = grad(x_new)
        
        # Update s and y
        s = x_new - x
        y = grad_new - prev_grad
        
        # Update memory
        if len(s_list) == m:
            s_list.pop(0)
            y_list.pop(0)
        s_list.append(s)
        y_list.append(y)
        
        # Check for convergence
        if np.linalg.norm(grad_new) < tol:
            break
        
        # Update for next iteration
        x = x_new
        prev_grad = grad_new
    
    return x

# Load and preprocess dataset
data = pd.read_csv(r"university/enm529/codes_in_lesson/diabetes2.csv")
X = data.drop(columns=['Outcome']).values
y = data['Outcome'].values
y = np.where(y == 0, -1, 1)  # Convert to -1 and 1 for SVM

scaler = StandardScaler()
X = scaler.fit_transform(X)

# 10-fold cross-validation
kf = KFold(n_splits=10, shuffle=True, random_state=42)
train_accuracies = []
test_accuracies = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Initialize weights
    w = np.zeros(X.shape[1])
    
    # Optimize weights using LBFGS
    def loss_func(w):
        return svm_loss_and_grad(w, X_train, y_train)[0]
    
    def grad_func(w):
        return svm_loss_and_grad(w, X_train, y_train)[1]
    
    w = lbfgs_optimize(loss_func, grad_func, w, max_iter=100, tol=1e-6, m=10)
    
    # Calculate accuracies
    train_accuracy = compute_accuracy(w, X_train, y_train)
    test_accuracy = compute_accuracy(w, X_test, y_test)
    
    train_accuracies.append(train_accuracy)
    test_accuracies.append(test_accuracy)

# Compute average accuracies
average_train_accuracy = np.mean(train_accuracies)
average_test_accuracy = np.mean(test_accuracies)

print("Average Training Accuracy:", average_train_accuracy)
print("Average Test Accuracy:", average_test_accuracy)