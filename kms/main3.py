import os
from math import exp



class Node:
  def __init__(self,_inputs,_weights):
    self.inputs = [1] + _inputs
    self.weights = _weights
    self.bias = _inputs[0]
    print(self.inputs,'--',self.weights)
      
  def netFunc(self):
    sum = 0
    for i in range(0,len(self.inputs)):
      sum += (self.weights[i] * self.inputs[i])
    return sum
  def step(self , x):
    return 1 if x > 0 else 0
  
  def neuron(self):
    return self.step(self.netFunc())


def getData(direc):
  arr = []
  with open(direc,'r') as fl:
    for line in fl:
      data = line.split()
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

dataSet = getData(chooseDirectory())
layers = {'inputs': 3,'hidden':3,'output':2}


def populateDataSet(dataSet):
  newDataSet = []
  for i in range(0,layers['inputs']+layers['hidden']):
    newDataSet.append([[],[]])
    for j in range(0,len(dataSet[i])):
      if j > layers['inputs']-1:
        newDataSet[i][1].append(dataSet[i][j])
      else:
        newDataSet[i][0].append(dataSet[i][j])
    newDataSet[i][0] = [1] + newDataSet[i][0]
  return newDataSet      
    

dataSet = populateDataSet(dataSet)
nodes = []

nodeZero = dataSet[0][0]



