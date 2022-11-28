"""import libraries"""
import numpy as np
import matplotlib.pyplot as plt

"""Fuctions"""
def h(x, theta):                                        
    return [[i] for i in np.dot(x,theta)]
    
"""mean squared error code"""
def mean_squared_error(y_pred, y_label):                
    return ((y_pred - y_label)**2).mean()

"""A function that adds one to each instance"""
def bias_column(x):                                     
    X = np.size(x, 0)
    return np.hstack((np.ones((X, 1)), x))

"""optimize"""
def optimize(self, iterations):
    for i in range(iterations):
        return self.step()
      

"""auxiliary function f"""
def f(x):
    f = 3 + np.dot(np.transpose(x - np.array([2, 6])), (x - np.array([2, 6])))
    return f
    
"""auxiliary function fprime"""
def fprime(x):
    fprime = 2*x - np.array([4, 12])
    return fprime

"""Find the least squares regression"""
class LeastSquaresRegression:                          
  def __init__(self):
      self.theta_ = None
  def fit(self, X_new, y):
    X = np.hstack((y, np.ones((100, 1))))
    a = np.dot(np.transpose(X),X_new)
    b = np.dot(np.linalg.inv(a), np.transpose(X))
    self.theta_ = np.dot(b, y)
  def predict(self, X_new):                            
    return np.dot(X_new, self.theta_)

"""Gradient Descent Optimizer class"""
class GradientDescentOptimizer:                         
  def __init__(self, f, fprime, start, learning_rate = 0.1):
    history = []
    self.history_ = history
    self.f_      = f                      
    self.fprime_ = fprime                 
    self.current_ = start                  
    self.learning_rate_ = learning_rate    
  def step(self):
    new_value = self.current_ - (self.learning_rate_ * fprime(self.current_))
    self.current_ = new_value
    self.history_.append(self.current_)
  def optimize(self, iterations):
    for i in range(iterations):
        self.step()
    
  def getCurrentValue(self):
    uservalue = [1.8, 5.2]
    return uservalue
