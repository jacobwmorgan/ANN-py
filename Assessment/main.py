from math import exp
import random


class Perceptron:
  def __init__(self):
    self.weights  = [None] * 5
    for i in range(0,len(self.weights)):
      self.weights[i] = random.randrange(-1,1)
  
  def sigmoidFunc(self,net):
    return 1/(1+exp(-net))
  
  def netFunc(self,inputs):
    net = 0
    for i in range(0,len(inputs)):
        temp = inputs[i] * self.weights[i]
        print(f"{i} {inputs[i]} {temp}")
        net = net + temp
        print(net)
    return net

  def guess(self,inputs):
    sum = self.netFunc(inputs)
    output = self.sigmoidFunc(sum)
    return output
  


p = Perceptron()

inputs = [-1,0.5]
guess = p.guess(inputs)
print(guess)
  
<<<<<<< HEAD
 
=======

    










trainingInputs = [[0,0,1],
                  [1,1,1],
                  [1,0,1],
                  [0,1,1]]

trainingOutputs = [[0,1,1,0]]








>>>>>>> e1f01555f395d299a6dfbb72d31e4e8fb40efab1
  
  



#weights = [[0.9, 0.45, 0.36, 0.98,0.92],[0.74,0.13,0.68],[0.8,0.4,0.10],[0.35, 0.97, 0.96],[0.35,0.8],[0.50,0.13],[0.90,0.8]]

#print(n)
