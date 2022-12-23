import random , os , csv
from math import exp , log10,floor
import matplotlib.pyplot as plt

class Node:
  def __init__(self,_name,_weights,_inputs,_outputs):
    self.name = _name
    self.inputs = _inputs
    self.weights = _weights
    self.outputs = _outputs
    self.error = 0
    self.errors = []
    
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
      self.output[i].errors.append(self.output[i].error)
      #print(self.output[i].errors)
    #Hidden Errors
    for i in range(0,len(self.hidden)):
      self.hidden[i].error = (self.hidden[i].outputs * (1 - self.hidden[i].outputs) * ((self.output[0].weights[i+1] * self.output[0].error) + (self.output[1].weights[i+1] * self.output[1].error)))
      self.hidden[i].errors.append(self.hidden[i].error)
      #print(self.hidden[i].errors)
  def updateWeights(self):
    deltaWeights = {'hidden':[[],[],[]],'output':[[],[]]}
    #Hidden updated weights
    for i in range(len(self.hidden)):
      for j in range(len(self.inputs)):
        newVal = self.learningRate * self.hidden[i].error * self.inputs[j]
        deltaWeights['hidden'][i].append(newVal)
        
    #Output updated weights
    for i in range(len(self.output)):
      deltaWeights['output'][i].append(self.learningRate * self.output[i].error * 1)
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
  
  def outputErrors(self):
    newErrors = [[],[]]
    for i in range(len(self.output)):
      node = self.output[i]
      newErrors [i].append(node.errors)
    return newErrors
  
  def squaredErrors(self):
    newErrors = 0
    for i in range(0,len(self.output)):
      outputNode = self.output[i]
      newErrors += (outputNode.error ** 2)
      
    return newErrors/2



def softmax(output1,output2):
  return exp(output1)/(exp(output1) + exp(output2))

def getData(direc):
  arr = []
  with open(direc,'r') as fl:
    for line in fl:
      line.strip("\n")
      data = line.split()
      for i in range(0,len(data)):
        if data[i] != "?":
          data[i] = float(data[i])
      arr.append(data)
  return arr



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
  epochs = []
  for i in range(value):
    epochs.append(i+1)
  return epochs


def plotGraph(epochs , errors):
  plt.plot(epochs,errors)
  plt.xlabel("Epoch")
  plt.ylabel("Squared Error")

  plt.title("Learning Curve ")
  plt.show()
  
def weightTable(newWeight):
  fileExists = os.path.exists("./weights.txt")
      
  if os.stat("./weights.txt").st_size != 0:
    with open("./weights.txt","r+") as fp:
      fp.truncate(0)
  
  with open("./weights.txt","w") as fp:
    
    for step in range(0,len(newWeight['hidden'][0][0])):
      for node in newWeight:
        for l in range(len(newWeight[node])):
          for i in range(len(newWeight[node][l])):
            fp.write("{:.3f},".format(newWeight[node][l][i][step]))
      fp.write("\n")

print("~~~~~~\nTraining")

dataSet = getData("data-CMP2020M-item1-train.txt")

layers = {'hidden':3,'output': 2}

#node [ 4 , 5 , 6 ],7 8
savedWeights = {'hidden':[[[0.9],[0.74],[0.8],[0.35]],[[0.45],[0.13],[0.4],[0.97]],[[0.36],[0.68],[0.1],[0.96]]],'output':[[[0.98],[0.35],[0.5],[0.9]],[[0.92],[0.8],[0.13],[0.8]]]}
weights = {'hidden':[[0.9,0.74,0.8,0.35],[0.45,0.13,0.4,0.97],[0.36,0.68,0.1,0.96]],'output':[[0.98,0.35,0.5,0.9],[0.92,0.8,0.13,0.8]]}
errors = []
squaredErrors = [0,0]

dataSet = populateDataSet(dataSet)
epochs = getEpochs()
#print(f"New - {weights}" )

## main stuff


for i in range(0,len(epochs)):
  tempErrors = []
  for j in range(len(dataSet)):
    nodes = populateNodes(dataSet[j][0],layers,weights)
    network = Network(dataSet[j][0],dataSet[j][1],nodes['hidden'],nodes['output'],0.1)
    network.forwardStep()
    network.errorFunc()
    network.backProp()
    newErrors = network.outputErrors()
    newWeights = network.outputWeights()
    if j == len(dataSet)-1:
      for node in range(len(newWeights['hidden'])):
        for weight in range(len(newWeights['hidden'][node])):
          savedWeights['hidden'][node][weight].append(newWeights['hidden'][node][weight])

      for node in range(len(newWeights['output'])):
        for weight in range(len(newWeights['output'][node])):
          savedWeights['output'][node][weight].append(newWeights['output'][node][weight])

    
    weights = newWeights
    tempErrors.append(network.squaredErrors())
  average = 0 
  for x in tempErrors:
    average += x
  errors.append(average)




print("~~~~~~~~~~\nTime to test it")

dataSet = populateDataSet(getData("data-CMP2020M-item1-test.txt"))

nodes = populateNodes(dataSet[0][0],layers,weights)
network = Network(dataSet[0][0],dataSet[0][1],nodes['hidden'],nodes['output'],0.1)
network.forwardStep()
#print("{:.3f},{:.3f}".format(network.output[0].outputs,network.output[1].outputs))
print("Probability Distribution\n 7 : {:.3f}, 8 : {:.3f}".format(softmax(network.output[0].outputs,network.output[1].outputs),softmax(network.output[1].outputs,network.output[0].outputs)))

weightTable(savedWeights)

plotGraph(epochs,errors)