from os import system
import torch
from torch import tensor
from torch.nn import Linear, Sigmoid, Sequential, MSELoss
from torch.optim import SGD


system('clear')

data_x = [
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

data_y = [[1], [0], [0], [0], [0]]

def reshapeMatrix(X_3x3):
    X_1x9 = []

    for i in range(3):
        for j in range(3):
            X_1x9.append(X_3x3[i][j])
        
    return X_1x9

model = Sequential(
    Linear(9, 1),
    Sigmoid()
)

criterion = MSELoss()
optimizer = SGD(model.parameters(), lr = 0.1)

for epoch in range(5000):
    avg_loss = 0
    for i in range(len(data_x)):

        # pick up data
        x = tensor(reshapeMatrix(data_x[i]), dtype=torch.float)
        y = tensor(data_y[i], dtype=torch.float)

        # reset the optimizer
        optimizer.zero_grad()

        # predict / forward
        yp = model(x)

        # calculate loss
        loss = criterion(y, yp)

        # propagate error backward
        loss.backward()

        # optimize / update
        optimizer.step()

        avg_loss += loss.item()
    avg_loss /= len(data_x)
    if epoch % 100 == 0:
        print(f"epoch = {epoch}, loss = {avg_loss:12.6f}")
    
for i in range(len(data_x)):
    x = tensor(reshapeMatrix(data_x[i]), dtype=torch.float)
    yp = model(x)

    print(x, yp)
