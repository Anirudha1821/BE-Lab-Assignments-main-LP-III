# WHAT WE HAVE TO FIND -> We want to find the value of x that minimizes the function y  
import numpy as np

# Define the function y = (x + 3)^2
def func(x):
    return (x + 3)**2

# Define the derivative of the function: dy/dx = 2(x + 3)
def derivative(x):
    return 2 * (x + 3)

# Implement Gradient Descent
gd=[]

# starting_x: The initial value of x where the algorithm starts.
# learning_rate: A scalar value that determines the size of the step taken towards the minimum (step size).
# num_iterations: The number of iterations (steps) the algorithm will perform to update 𝑥 and move towards the local minimum.
def gradient_descent(starting_x, learning_rate, num_iterations):
    x = starting_x  # Starting point
    gd.append(starting_x)
    for i in range(num_iterations):
        grad = derivative(x)  # Compute the gradient at x
        x = x - learning_rate * grad  # Update x based on gradient
        gd.append(x)
        print(f"Iteration {i+1}: x = {x}, f(x) = {func(x)}")
    
    return x

# Initial point, learning rate, and number of iterations
starting_x = 2
learning_rate = 0.1  # Step size
num_iterations = 50

# Perform Gradient Descent
min_x = gradient_descent(starting_x, learning_rate, num_iterations)
print(f"Local minimum occurs at x = {min_x}")

import seaborn as sns
sns.scatterplot(gd)