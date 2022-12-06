import matplotlib.pyplot as plt
import numpy as np

# DATA SET

X = [
    [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
    ],

    [
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0],
    ],

    [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    ],

    [
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1],
    ],

    [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    ],
]

Y = [1, 0, 0, 0, 0]


# HELPER FUNCTION

def reshapeMatrix(X_3x3):
    X_1x9 = []

    for i in range(3):
        for j in range(3):
            X_1x9.append(X_3x3[i][j])
        
    return X_1x9

def loss(y, yp):
    return y - yp

def backward(lr, e, X):
    dweights = []
    for i in range(len(X)):
        dw = lr * e * X[i]
        dweights.append(dw)

    return dweights


# NEURON MODEL CLASS

class LinearNeuronDetect:
    def __init__(self):
        self.weights = [0 for i in range(9)]
        self.bias    = 0

    def forward(self, X):
        y = 0
        
        for i in range(9):
            y += X[i] * self.weights[i]
        y += self.bias
        
        return y
    
    def __str__(self):
        out = ""
        
        for i in range(9):
            if i % 3 == 0:
                out += "\n"
            out += f"{self.weights[i]:<10.5f}"
        
        out += "\n"
        out += f"{self.bias:<10.5f}"

        return out

def sigmoidActivation(x):
    return 1.0 / (1.0 + np.exp(-x))


# NEURON TUNNING

model = LinearNeuronDetect()

lr = 0.001
for epoch in range(20000):
    errors = []
    for i in range(len(X)):
        x = reshapeMatrix(X[i])
        y = Y[i]

        yp = model.forward(x)
        e = loss(y, yp)
        gradient = backward(lr, e, x)
        
        db = lr * e
        model.bias += db

        for j in range(len(model.weights)):
            model.weights[j] += gradient[j]
        
        errors.append(e)
    
    me = abs(sum(errors)/len(errors))
    print(f"epoch = {epoch:<5} loss = {me:<12.6f}")


# TESTING

for i in range(len(X)):
    x = reshapeMatrix(X[i])
    yp = model.forward(x)

    y = 1 if yp > 0.5 else 0
    print(yp, y)

print(model) 