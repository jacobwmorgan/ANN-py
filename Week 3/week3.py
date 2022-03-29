from glob import glob
from random import random


class Neuron:
  def __init__(self,_value,_weights):
    self.value = _value
    self.weights = _weights
class Network:
  def __init__(self,_dataSet, _nInputs , _nHidden,_nOutputs):
    self.network = list()
    self.dataSet = _dataSet[:-1]
    self.inputLayer = []
    for i in range(0,len(self.dataSet[0])-1):
      self.inputLayer.append(Neuron(self.dataSet[0][i],[random() for i in range(0,_nInputs)]))
    self.bias = Neuron(1,[random() for i in range(_nHidden + _nOutputs)])
    self.hiddenLayer = []
    for i in range(_nHidden):
      self.hiddenLayer.append(Neuron(0,[random() for i in range(_nHidden)]))
    self.outputLayer = []
    for i in range(_nOutputs):
      self.outputLayer.append(Neuron(0,[random() for i in range(_nOutputs)]))

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
      



   

dataSet = getData(chooseDirectory())
  


network = Network(dataSet,len(dataSet[0])-1,3,2)
print(f"Input Layers")
for i in range(0,len(network.inputLayer)):
   print(f"{network.inputLayer[i].value} | {network.inputLayer[i].weights}")
print("Hidden Layers")
for i in range(0,len(network.hiddenLayer)):
   print(f"{network.hiddenLayer[i].value} | {network.hiddenLayer[i].weights}")
print("Output Layers")
for i in range(0,len(network.outputLayer)):
   print(f"{network.outputLayer[i].value} | {network.outputLayer[i].weights}")



print(f"bias = {network.bias.value} | {network.bias.weights}")




