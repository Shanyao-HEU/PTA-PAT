#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def warmUpExercise():
    print(np.eye(5))

def plotData(x, y):
    plt.figure()
    plt.plot(x, y, 'rx')
    plt.ylabel('Profit in $10,000s')
    plt.xlabel('Population of City in 10,000s')
    plt.show()

def computeCost(X, y, theta):
    y = y.reshape(-1, 1)
    m = y.shape[0]
    J = np.sum(np.power((np.dot(X, theta)-y), 2))/(2*m)

    return J

def gradientDescent(X, y, theta, alpha, iterations):

    y = y.reshape(-1, 1)
    m = y.shape[0]
    J_history = np.zeros((iterations, 1))

    theta_s = theta

    for iter in range(iterations):
        theta[0] = theta[0] - alpha/m*np.sum(np.dot(X, theta_s)-y)
        theta[1] = theta[1] - alpha/m*np.sum((np.dot(X, theta_s)-y) * X[:, 1])

        theta_s = theta
        J_history[iter] = computeCost(X, y, theta_s)

    return J_history

if __name__ == '__main__':
    # Part 1: Basic Function
    warmUpExercise()

    # Part 2: Plotting
    data = pd.read_csv("ex1data1.txt")
    X = data.iloc[:, 0].values
    y = data.iloc[:, 1].values
    m = X.shape[0]

    #plotData(X, y)
    # Part 3: Gradient descent

    columnOnes = np.ones((m, 1))
    X_addOnes = np.column_stack((columnOnes, X))

    theta = np.zeros((2, 1))
    iterations = 1500
    alpha = 0.01
    print(X_addOnes.shape, y.shape, theta.shape)
    print("The initial cost of func is: {}".format(computeCost(X_addOnes, y, theta)))

    theta = gradientDescent(X_addOnes, y, theta, alpha, iterations)
    print("Theta found by gradient descent:{}".format(theta))
    # Part 4: Visualizing J(theta_0, theta_1)


