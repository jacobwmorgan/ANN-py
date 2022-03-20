#https://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/

from glob import glob
from random import seed
from random import random
from math import exp

class Node:
  # Name(identify the Node), nValue(value of said Node) ,_fPointer(),_bPointer()
  def __init__(self,_name,_nValue,_fPointer,_bPointer):
    self.name = _name
    self.nValue = _nValue
    self.fPointer = _fPointer
    self.bPointer = _bPointer


class Network:
  def __init__(self,_ninputs , _nhidden,_noutputs):
    self.network = list()
    hiddenLayer = [{'weights':[random() for i in range(_ninputs + 1)]} for i in range(_nhidden)]  
    self.network.append(hiddenLayer)
    outputLayer = [{'weights':[random() for i in range(_nhidden + 1)]} for i in range(_noutputs)]  
    self.network.append(outputLayer)
  
  @staticmethod
  def netFunction(values,weights): #Calculating the neuron activation for an input``
    total = 0
    for i in range(0,len(values)):
      total += (values[i]*weights[i])
    return total

  @staticmethod
  def sigmoidFunction(net): #Transfer neuron activation
    return 1/(1+exp(-net))
  
  def transferDerivative(self,output):
    return output*(1.0-output)

  def forwardPropagate(self,network , row): #Forward propagation input to a network layer , returns the outputs from the last layer (output layer)
    inputs = row
    for layers in network:
      newInputs = []
      for neuron in layer:
        activation = self.netFunction(inputs,neuron['weights'])
        neuron['output'] = self.sigmoidFunction(activation)
        newInputs.append(neuron['output'])
      inputs = newInputs
    return inputs
  
  def backPropagate_error(self,network , expected): #Back propagation error
    for i in reversed(range(0,len(network))) :
      layer = network[i]
      errors = list()
      if i != len(network)-1:
        for j in range(0,len(layer)):
          error = 0
          for neuron in network[i+1]:
            error += (neuron['weights'][j] * neuron['delta'])
          errors.append(error)
      
      else:
        for j in range(0,len(layer)):
          neuron = layer[j]
          errors.append(neuron['output'] - expected[j])
      
      for i in range(len(layer)):
        neuron = layer[j]
        neuron['delta'] = errors[j] * self.transferDerivative(neuron['output'])
        
          

    
def getData(direc):
  arr = [])
  with open(direc,'r') as fl:
    for line in fl:
      data = line.split()
      arr.append(data)
  return arr

 
def chooseDirectory():
  while True:
    listOfDirs = [f for f in glob("*.txt")]
    for i in range(0,len(listOfDirs)):
      print(f"{i+1}:{listOfDirs[i]}")
    selected = input(">")
    if selected.isnumeric() == False:
      print("Invalid input\n")
    else:
      if int(selected) > len(listOfDirs) or int(selected) < 0:
        print("Invalid Input\n")
      else:
        return listOfDirs[int(selected)-1]

'''
def populateNodes(dataSet):
  for i in range(0, len(dataSet)):
    Nodes.append(Node(f"{i}",dataSet[0],))
'''
    


seed(1)
network = Network(2,1,2)




