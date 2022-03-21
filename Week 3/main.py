<<<<<<< HEAD
import math , os  , glob
=======
#https://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/
>>>>>>> 0298984345d3458bb0c9680d96369bad4ce5e346

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

<<<<<<< HEAD
dataSets = {}
nodes = []
bias  = node("bias",0,0,0)
target = 0


=======

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
>>>>>>> 0298984345d3458bb0c9680d96369bad4ce5e346

  @staticmethod
  def sigmoidFunction(net): #Transfer neuron activation
    return 1/(1+exp(-net))
  
  def transferDerivative(self,output):
    return output*(1.0-output)

  def forwardPropagate(self,network , row): #Forward propagation input to a network layer , returns the outputs from the last layer (output layer)
    inputs = row
    for layer in network:
      newInputs = []
      for neuron in layer:
        activation = self.netFunction(inputs,neuron['weights'])
        neuron['output'] = self.sigmoidFunction(activation)
        newInputs.append(neuron['output'])
      inputs = newInputs
    return inputs
  
  def backPropagate_error(self,network , expected): #Back propagation error
    for i in reversed(range(len(network))) :
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
      
      for j in range(len(layer)):
        neuron = layer[j]
        neuron['delta'] = errors[j] * self.transferDerivative(neuron['output'])
        
  def updateWeights(self,network,row,learningRate):
    for i in range(len(network)):
      inputs  = row[:-1]
      if i !=0:
        inputs = [neuron['output'] for neuron in network[i-1]]
      for neuron in network[i]:
        for j in range(len(inputs)):
          neuron['weights'][j] -= learningRate * neuron['delta'] * inputs[j]
        neuron['weights'][-1] -= learningRate * neuron['delta']
  
  def trainNetwork(self,network,train,learningRate,nEpoch,nOutputs):
    for epoch in range(nEpoch):
      sumError = 0
      for row in train:
        outputs = self.forwardPropagate(network,row)
        expected = [0 for i in range(nOutputs)]
        expected[row[-1]] = 1
        sumError += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
        self.backPropagate_error(network,expected)
        self.updateWeights(network,row,learningRate)
      print(f">Epoch {epoch} , Learning Rate = {learningRate} , Error = {sumError}")
  
  def predict(self,network,row):
    outputs = self.forwardPropagate(network,row)
    return outputs.index(max(outputs))

    
def getData(direc):
  arr = []
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

<<<<<<< HEAD

def populateDataSets(_dataSets):
  for i in range(0,len(_dataSets)):
    dataSets[f"DataSet{i}"] = _dataSets[i]
=======
'''
def populateNodes(dataSet):
  for i in range(0, len(dataSet)):
    Nodes.append(Node(f"{i}",dataSet[0],))
'''
    
>>>>>>> 0298984345d3458bb0c9680d96369bad4ce5e346

populateDataSets(getData(chooseDirectory()))

<<<<<<< HEAD
print(dataSets)
=======
seed(1)
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]
n = Network(0,0,0)
network = [[{'weights': [-1.482313569067226, 1.8308790073202204, 1.078381922048799]}, {'weights': [0.23244990332399884, 0.3621998343835864, 0.40289821191094327]}],
	[{'weights': [2.5001872433501404, 0.7887233511355132, -1.1026649757805829]}, {'weights': [-2.429350576245497, 0.8357651039198697, 1.0699217181280656]}]]
for row in dataset:
	prediction = n.predict(network, row)
	print('Expected=%d, Got=%d' % (row[-1], prediction))
>>>>>>> 0298984345d3458bb0c9680d96369bad4ce5e346
