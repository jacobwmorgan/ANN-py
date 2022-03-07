
import os , math
class Grad_Decent:
    def __init__(self,values,rate,epochs,weights):
        self.values = values[:-1]
        self.target = values[-1]
        self.rate = rate 
        self.epochs = epochs
        self.net = 0
        self.weights = weights 

    def net_function(self):
        net = 0
        for i in range(0,len(self.values)):
            temp = self.values[i] * self.weights[i]
            net = net + temp
        return net
    
    def sigmoid_function(self):
        net = self.net_function()
        return 1/(1+math.exp(-net))

    def train(self):
        print(f"Values = {self.values}\n~~~~~~")
        for j in range(0,self.epochs):
            print(f"Epoch = {j+1}")
            updatedWeights = [0] * len(self.weights)
            error = 0
            for i in range(0,len(updatedWeights)):
                sigma = self.sigmoid_function()
                updatedWeights[i] = self.rate*(self.target - sigma) * self.values[i]
                error += abs(self.target - sigma)
            for i in range(0,len(self.weights)):
                self.weights[i] = self.weights[i] + updatedWeights[i]
            print(f"Weights = {self.weights}")
            print(f"Error = {error}")
            print("\n=================")


    def test(self):
        print(f"values = {self.values}")
        print(f"target = {self.target}")
        
        


def read_txt(direc):
    arr = []
    with open(direc,'r') as fl:
       for line in fl:
           data = line.split()
           arr.append(data)
    return arr



data = read_txt("data-AND.txt")

learning_rate = 0.05
epochs = 1000
weights = [0.5,-0.1,0.2]


for i in range(0,len(data)):
    for j in range(0,len(data[i])):
        data[i][j] = float(data[i][j])
        

for i in range(0,len(data)):
    dude = Grad_Decent(data[i],learning_rate,epochs,weights)
    dude.train()
    weights = dude.weights

