import matplotlib.pyplot as plt
from math import exp
import numpy as np
#https://towardsdatascience.com/inroduction-to-neural-networks-in-python-7e0b422e6c24

class NeuralNetwork:
  def __init__(self,inputs,outputs):
    self.inputs = inputs
    self.outputs = outputs
    
    self.weights = np.array([[.50],[.50],[.50],[.50],[.50],[.50]])
    self.errorHistory = []
    self.epochs = []
    
    
  def netFunc(self,inputs):
    net = 0
    for i in range(len(inputs)):
        temp = inputs[i] * self.weights[i]
        print(i,'-',len(inputs),'-',len(self.weights))
        net = net + temp
    return net  
  
  #activation function ==> S(x) = 1/1+e^(-x)
  def sigmoidFunc(self,net,deriv = False):
    if deriv == True:
      return net * (1 - net)
    return 1/(1*np.exp(-net))
  
   # data will flow through the neural network.
  def feedForward(self):
    self.hidden = self.sigmoidFunc(self.netFunc(self.inputs))
  
  def backProp(self):
    self.error = self.outputs - self.hidden
    delta = self.error * self.sigmoidFunc(self.hidden,deriv = True)
    self.weights += np.dot(self.inputs.T,delta)
    
  def train(self,epochs = 25000):
    for epoch in range(epochs):
      self.feedForward()
      self.backProp()
      self.errorHistory.append(np.average(np.abs(self.error)))
      self.epochs.append(epoch)
  
  def predict(self, newInput):
    prediction = self.sigmoidFunc(self.netFunc(newInput,self.weights))
    return prediction




inputs = np.array([[0,1,0],
          [0,1,1],
          [0,0,0],
          [1,0,0],
          [1,1,1],
          [1,0,1]])

outputs = np.array([[0],[0],[0],[1],[1],[1]])

NN = NeuralNetwork(inputs,outputs)
NN.train()

example = [[1,1,0]]
exampleTwo = [[0,1,1]]

print(NN.predict(example),'| Correct - ',example[0][0])
print(NN.predict(exampleTwo),'| Correct - ',exampleTwo[0][0])

plt.figure(figsize=(15,5))
plt.plot(NN.epochs, NN.errorHistory)

plt.xlabel('Epoch')
plt.ylabel('Error')
plt.show()