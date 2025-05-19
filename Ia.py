#perceptron
import numpy as np

def perceptron(X, y, epochs=1000, learning_rate=0.01):
    # Initialize weights and bias
    weights = np.zeros(X.shape[1])
    bias = 3

    # Training loop
    for _ in range(epochs):
        for idx, x_i in enumerate(X):
            linear_output = np.dot(x_i, weights) + bias
            y_predicted = np.where(linear_output >= 0, 1, 0)

            # Update weights and bias
            update = learning_rate * (y[idx] - y_predicted)
            weights += update * x_i
            bias += update

    return weights, bias

# Example usage
# Sample data (XOR problem)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([1, 1, 1, 0])  # XOR labels

# Train perceptron
weights, bias = perceptron(X, y)

# Test perceptron
for x in X:
    linear_output = np.dot(x, weights) + bias
    y_predicted = np.where(linear_output >= 0, 1, 0)
    print(f"Input: {x}, Predicted: {y_predicted}")

    # Output: Input: [0 0], Predicted: [0]

