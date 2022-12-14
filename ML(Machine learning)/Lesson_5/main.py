class LinearLayer:
    def __init__(self, x_size, y_size):
        
        self.x_size = x_size
        self.y_size = y_size

        # INPUT DATA
        self.x = [0 for i in range(x_size)]

        # PARAMETS
        self.w = [[0 for i in range(x_size)] for j in range(y_size)]
        self.b = [0 for i in range(y_size)]

        # OUTPUT DATA
        self.y = [0 for i in range(y_size)]

    def forward(self, x):
        self.x = x
        
        for j in range(self.y_size):
            self.y[j] = self.b[j]
            for i in range(self.x_size):
                self.y[j] += self.x[i] * self.w[j][i]


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
    
hiddenLayer = LinearLayer(2, 4)

hiddenLayer.b = [1, 2, 3, 4]
hiddenLayer.w = [
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80]
]

x = [1, 2, 3, 4]
y = hiddenLayer.forward(x)

print(hiddenLayer)

actv = ActivationLayer(4)

X = [-1, 0, 1, 0]
Y = actv.forward(X)

print(actv)

