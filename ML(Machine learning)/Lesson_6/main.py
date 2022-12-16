from random import random

data_x = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
]

data_y = [0, 1, 1, 0]

class LinearLayer:
    def __init__(self, x_size, y_size):
        
        self.x_size = x_size
        self.y_size = y_size

        # INPUT DATA
        self.x = [0 for i in range(x_size)]

        # PARAMETS
        self.w = [[random() for i in range(x_size)] for j in range(y_size)]
        self.b = [random() for i in range(y_size)]

        # OUTPUT DATA
        self.y = [0 for i in range(y_size)]

    def forward(self, x):
        self.x = x
        
        for j in range(self.y_size):
            self.y[j] = self.b[j]
            for i in range(self.x_size):
                self.y[j] += self.x[i] * self.w[j][i]
            
        return self.y

    def backward(self, DELTA, lr):
        self.b = [ self.b[j] - lr * DELTA[j] for j in range(self.y_size) ]
        
        self.w = [
            [self.w[j][i] - lr * self.x[i] * DELTA[j] for i in range(self.x_size)] for j in range(self.y_size)
        ]

        return [
            sum([ DELTA[j] * self.w[j][i] for j in range(self.y_size) ]) for i in range(self.x_size)
        ]

    def __str__(self):
        
        out = "\n---------------------" + '-'*(self.y_size * 13) + '\n'
        for i in range(self.x_size):
            out += f"X: {self.x[i]:12.5f} >  W: "
            for j in range(self.y_size):
                out += f"{self.w[j][i]:12.5f}" + ' '
            out += '\n'

        out += ' '*19 + "B: "
        
        for i in range(self.y_size):
            out += f"{self.b[i]:12.5f}" + ' '

        out += '\n' + "---------------------" + '-'*(self.y_size * 13) + '\n'
        out += ' '*30
        for j in range(self.y_size):
            out += 'v' + ' '*12
        out += '\n' + ' '*19 + "Y: "

        for i in range(self.y_size):
            out += f"{self.y[i]:12.5f}" + ' '

        return out

class ActivationLayer:
    def __init__(self, x_size):
        self.x_size = x_size
        self.x = [0 for i in range(x_size)]
        self.y = [0 for i in range(x_size)]
    
    def forward(self, X):
        self.x = X
        for i in range(self.x_size):
            self.y[i] = self.sigmoid(self.x[i])
        return self.y
    
    def sigmoid(self, x):
        return 1 / (1 + 2.7 ** -x)
    
    def backward(self, DELTA):
        return [ DELTA[i] * self.sigmoid_prime(self.x[i]) for i in range(self.x_size) ]

    def sigmoid_prime(self, delta):
        return self.sigmoid(delta) * (1 - self.sigmoid(delta))

    def __str__(self):
        out = "\n--" + '-'*(self.x_size * 13) + "\n"

        out += "X: "
        for i in range(self.x_size):
            out += f"{self.x[i]:12.5f}" + ' '
        
        out += "\n--" + '-'*(self.x_size * 13) + "\n"
        out += ' '*11
        for i in range(self.x_size):
            out += 'v' + ' '*12
        out += '\n'

        out += "Y: "
        for j in range(self.x_size):
            out += f"{self.sigmoid(self.x[j]):12.5f}" + ' '
        out += '\n'

        return out

def loss(y, yp):
    return yp - y

lr = 0.1

lin0 = LinearLayer(2, 3)
act1 = ActivationLayer(3)
lin2 = LinearLayer(3, 1)
act3 = ActivationLayer(1)

for epoch in range(100_000):
    mean_error = 0
    for i in range(len(data_x)):
        
        # training loop
        x = data_x[i]
        y = data_y[i]

        #FORWARD
        X0 = x
        Y0 = lin0.forward(X0)
        X1 = Y0
        Y1 = act1.forward(X1)
        X2 = Y1
        Y2 = lin2.forward(X2)
        X3 = Y2
        Y3 = act3.forward(X3)
        Yp = Y3

        #BACKWARD
        delta3 = [loss(y, Yp[0])]
        delta2 = act3.backward(delta3)
        delta1 = lin2.backward(delta2, lr)
        delta0 = act1.backward(delta1)
        delta = lin0.backward(delta0, lr)

        mean_error += delta3[0]
    mean_error /= len(data_x)
    print(f"epoch = {epoch:5} loss = {mean_error:12.6f}")