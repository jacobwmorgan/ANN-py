import random , os
from math import exp

class Node:
  def __init__(self,_name,_weights,_inputs,_outputs):
    self.name = _name
    self.inputs = _inputs
    self.weights = _weights
    self.outputs = _outputs
    self.error = 0
    
  def netFunc(self):
    sum = 0
    for i in range(0,len(self.inputs)):
      sum += self.weights[i] * self.inputs[i]
    return sum
  
  def sigmoid(self):
    return 1/ (1 + exp(-self.netFunc()))

class Network:
  def __init__(self,_inputs,_expected,_hidden,_output,_learningRate):
    self.inputs = _inputs
    self.expected = _expected
    self.hidden = _hidden
    self.output = _output
    self.learningRate = _learningRate
    
    '''
    print(f"=====\nNew network created\nInputs = {self.inputs}")
    print(f"Hidden Layer =")
    for node in self.hidden: print(node.name,"|",node.weights)
    print(f"Output Layer =")
    for node in self.output: print(node.name,"|",node.weights)
    '''
  
  def forwardStep(self):
    outputs = []
    for node in self.hidden:
      output = node.sigmoid()
      outputs.append(output)
      node.outputs = output
    outputs = [1] + outputs
    for node in self.output:
      node.inputs = outputs
    outputs = []
    for node in self.output:
      output = node.netFunc()
      outputs.append(output)
      node.outputs = output

  def errorFunc(self):
    #Output errors
    for i in range(len(self.output)):
      self.output[i].error = self.expected[i] - self.output[i].outputs
      
    #Hidden Errors
    for i in range(0,len(self.hidden)):
      self.hidden[i].error = (self.hidden[i].outputs * (1 - self.hidden[i].outputs) * ((self.output[0].weights[i+1] * self.output[0].error) + (self.output[1].weights[i+1] * self.output[1].error)))
      
  def updateWeights(self):
    deltaWeights = {'hidden':[[],[],[]],'output':[[],[]]}
    #Hidden updated weights
    for i in range(len(self.hidden)):
      for j in range(len(self.inputs)):
        newVal = self.learningRate * self.hidden[i].error * self.inputs[j]
        deltaWeights['hidden'][i].append(newVal)
        
    #Output updated weights
    for i in range(len(self.output)):
      deltaWeights['output'][i].append(self.learningRate * self.hidden[i].error * 1)
      for j in range(len(self.hidden)):
        newVal = self.learningRate * self.output[i].error * self.hidden[j].outputs
        deltaWeights['output'][i].append(newVal) 
    return deltaWeights  
  
  def backProp(self):
    deltaWeights = self.updateWeights()
    for i in range(len(self.hidden)):
      node = self.hidden[i]
      for j in range(len(node.weights)):
        node.weights[j] = node.weights[j]+ deltaWeights['hidden'][i][j]
        
    for i in range(len(self.output)):
      node = self.output[i]
      for j in range(0,len(node.weights)):
        node.weights[j] = node.weights[j]+ deltaWeights['output'][i][j] 

  def outputWeights(self):
    newWeights = {'hidden':[[],[],[]],'output':[[],[]]}
    for i in range(len(self.hidden)): 
      node = self.hidden[i]
      newWeights['hidden'][i] = node.weights
    for i in range(len(self.output)): 
      node = self.output[i]
      newWeights['output'][i] = node.weights
    return newWeights

def getData(direc):
  arr = []
  with open(direc,'r') as fl:
    for line in fl:
      line.strip("\n")
      data = line.split()
      for i in range(0,len(data)):
        data[i] = float(data[i])
      arr.append(data)
  return arr
 
def chooseDirectory():
  listOfDirs = []
  for(root,dirs,file) in os.walk("./"):
    for f in file:
      if '.txt' in f:
        listOfDirs.append(f)
  while True:
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

def populateDataSet(dataSet):
  newDataSet = []
  print("\n\nData Sets\n~~~~~~~~~~~~~~~~~~~~~~~~~")
  print(dataSet)
  for i in range(len(dataSet)):
    newDataSet.append([[],[]])

    for j in range(len(dataSet[i])):
      if j > layers['hidden']-1:
        newDataSet[i][1].append(dataSet[i][j])
      else:
        newDataSet[i][0].append(dataSet[i][j])
    newDataSet[i][0] = [1.00] + newDataSet[i][0]
  print("~~~~~~~~~~~~~~~~~~~~~~~~~")
  return newDataSet   

def populateNodes(dataSet,layers,weights):
  nodes = {'hidden':[],'output' : []}
  for i in nodes:
    for j in range(0,layers[i]):
      newNode = Node(f"Node{len(nodes['hidden']+nodes['output'])}",weights[i][j],dataSet,[])
      nodes[i].append(newNode)
  return nodes

def getEpochs():
  while True:
    try:
      value = int(input("\nAmount of Epochs : "))
      break
    except ValueError:
      print("Invalid Input")
      
  return value

#Testing shit
dataSet = getData(chooseDirectory())
layers = {'hidden':3,'output': 2}

#node [ 4 , 5 , 6 ],7 8
weights = {'hidden':[[0.9,0.74,0.8,0.35],[0.45,0.13,0.4,0.97],[0.36,0.68,0.1,0.96]],'output':[[0.98,0.35,0.5,0.9],[0.92,0.8,0.13,0.8]]}
dataSet = populateDataSet(dataSet)
#epochs = getEpochs()
nodes = populateNodes(dataSet[0][0],layers,weights)
network = Network(dataSet[0][0],dataSet[0][1],nodes['hidden'],nodes['output'],0.1)
print(f"Original - {weights}" )
network.forwardStep()
network.errorFunc()
network.backProp()
weights = network.outputWeights()
print(f"New - {weights}" )

## main stuff
'''
for i in range(0,len(dataSet)):
  nodes = populateNodes(dataSet[i][0],layers,weights)
  network = Network(dataSet[i][0],nodes['hidden'],nodes['output'],dataSet[i][1])
  for j in range(epochs):
    print("lmao")
    ## Do shit
    # - >> Forward 
    # - << Backward
    # - >> work out error Rate
    # - >> update weights

'''