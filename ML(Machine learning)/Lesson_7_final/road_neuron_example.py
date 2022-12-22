from os import system
import torch
from torch import tensor
from torch.nn import Linear, Sigmoid, Sequential, MSELoss
from torch.optim import SGD


system('clear')

data_x = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
]

data_y = [[0], [1], [1], [0]]

model = Sequential(
    Linear(4, 1),
    Sigmoid()
)

criterion = MSELoss()
optimizer = SGD(model.parameters(), lr = 0.1)

for epoch in range(1000):
    avg_loss = 0
    for i in range(len(data_x)):
        x = tensor(data_x[i], dtype=torch.float)
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
    x = tensor(data_x[i], dtype=torch.float)
    yp = model(x)

    print(x, yp)