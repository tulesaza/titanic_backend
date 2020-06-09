import numpy as np


def sigma(z):
    return 1 / (1 + np.exp(-z))


class LogisticRegression:

    def __init__(self, theta=None, eta=0.001, iterations=1000000, threshold=0.5):
        self.theta = theta
        self.eta = eta
        self.iterations = iterations
        self.threshold = threshold

    def fit(self, X, y):
        # expand by ones column
        X = np.c_[np.ones((X.shape[0], 1)), X]
        theta = np.random.rand(X.shape[1], 1)
        y = y.reshape(y.shape[0], 1)
        # batch gradient descent
        for iteration in range(self.iterations):
            gradient = 1 / len(X) * X.T.dot(sigma(X.dot(theta)) - y)
            theta = theta - self.eta * gradient
        self.theta = theta

    def predict_proba(self, X):
        X = np.c_[np.ones((X.shape[0], 1)), X]
        return sigma(X.dot(self.theta))

    def predict(self, X):
        predicted_y = self.predict_proba(X)
        predicted_y[predicted_y > self.threshold] = 1
        predicted_y[predicted_y <= self.threshold] = 0
        return predicted_y
