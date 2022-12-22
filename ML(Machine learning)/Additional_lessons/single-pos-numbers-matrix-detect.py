from os import system
import torch
from torch import tensor
from torch.nn import Linear, Sigmoid, Sequential, MSELoss
from torch.optim import SGD


system('clear')

data_x = [
    [
    [5, -1,  0],
    [2,  0, -5],
    [1,  1, -5],
    ],

    [
    [-5, -1,  0],
    [-2,  0, -5],
    [-1,  1, -5],
    ],

    [
    [-5, -1,  0],
    [ 2,  0, -5],
    [ 1,  1, -5],
    ],

    [
    [ 5, -1,  0],
    [-2,  0, -5],
    [ 1,  1, -5],
    ],

    [
    [ 5, -1,  0],
    [ 2,  0, -5],
    [-1,  1, -5],
    ],

    [
    [2, -1,  0],
    [0,  0, -5],
    [4,  1, -5],
    ],

    [
    [-2, -1,  0],
    [-3,  0, -5],
    [-4,  1, -5],
    ],

    [
    [-2, -1,  0],
    [-5,  0, -5],
    [ 0,  1, -5],
    ]
]

data_y = [[1], [0], [1], [1], [1], [1], [0], [1]]

def reshapeMatrix(X_3x3):
    X_1x3 = []
    
    for i in range(3):
        X_1x3.append(X_3x3[i][0])
        
    return X_1x3

model = Sequential(
    Linear(3, 1),
    Sigmoid()
)

criterion = MSELoss()
optimizer = SGD(model.parameters(), lr = 0.1)

for epoch in range(5000):
    avg_loss = 0
   
    for i in range(len(data_x)):
        x = tensor(reshapeMatrix(data_x[i]), dtype=torch.float)
        y = tensor(data_y[i], dtype=torch.float)

        optimizer.zero_grad()

        yp = model(x)

        loss = criterion(y, yp)
        loss.backward()

        optimizer.step()

        avg_loss += loss.item()
    avg_loss /= len(data_x)
    
    if epoch % 100 == 0:
        print(f"epoch = {epoch}, loss = {avg_loss:12.6f}")

for i in range(len(data_x)):
    x = tensor(reshapeMatrix(data_x[i]), dtype=torch.float)
    yp = model(x)

    print(x, yp)