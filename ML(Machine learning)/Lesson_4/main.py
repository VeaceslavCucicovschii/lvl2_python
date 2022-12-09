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
        
        out = "\n------------------------------------------------------------\n"
        for i in range(self.x_size):
            out += f"X: {self.x[i]:12.5f} >  W: "
            for j in range(self.y_size):
                out += f"{self.w[j][i]:12.5f}" + ' '
            out += '\n'

        out += ' '*19 + "B: "
        
        for i in range(self.y_size):
            out += f"{self.b[i]:12.5f}" + ' '

        out += "\n------------------------------------------------------------\n"
        out += ' '*30 + 'v' + ' '*12 + 'v' + ' '*12 + 'v\n'
        out += ' '*19 + "Y: "

        for i in range(self.y_size):
            out += f"{self.y[i]:12.5f}" + ' '

        return out + '\n'


    
hiddenLayer = LinearLayer(2, 3)

hiddenLayer.b = [1, 2, 3]
hiddenLayer.w = [
    [10, 20],
    [30, 40],
    [50, 60]
]

x = [1, 2]
y = hiddenLayer.forward(x)

print(hiddenLayer)

