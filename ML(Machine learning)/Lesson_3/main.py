import numpy as np

data_x = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
]

data_y = [0, 1, 1, 0]


## NN CLASS / HELPERS

class DoubtNeuron:
    def __init__(self):
        self.weights = [0 for i in range(4)]
        self.bias    = 0

    def forward(self, X):
        y = 0

        for i in range(4):
            y += X[i] * self.weights[i]
        
        y += self.bias
        return y

    def __str__(self):
        
        result = ""

        for i in range(4):
            result += f"X{i} * {self.weights[i]:<12.6f} + "
        
        return f"{result} {self.bias:<12.6f}"

def loss(y, yp):
    return y - yp

def backward(lr, e, X):
    dweights = []
    for i in range(len(X)):
        dw = lr * e * X[i]
        dweights.append(dw)

    return dweights

def activate(x):
    return 1.0 / (1.0 + np.exp(-x))


## TRAINING LOOP

model = DoubtNeuron()
lr = 0.01

for epoch in range(100):
    e_avg = 0
    for i in range(len(data_x)):
        # batch
        x = data_x[i]
        y = data_y[i]

        # prediction
        yp = activate(model.forward(x))
        
        # estimate loss
        e = loss(y, yp)
        e_avg += e

        # update parameters
        gradient = backward(lr, e, x)

        dbias = lr * e
        model.bias += dbias

        for j in range(len(model.weights)):
            model.weights[j] += gradient[j]
    e_avg /= len(data_x)

    print(f"epoch: {epoch:5} avg loss = {e_avg:<12.6f}")


## MANUAL TESTING

print("NN PARAMETERS")
print(model)

for i in range(len(data_x)):
    x = data_x[i]
    # prediction
    yp = activate(model.forward(x))
    print(x, yp)