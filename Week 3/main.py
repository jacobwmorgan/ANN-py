import math , os  , glob

class node:
  # Name(identify the node), nValue(value of said node) ,_fPointer(),_bPointer()
  def __init__(self,_name,_nValue,_fPointer,_bPointer):
    self.name = _name
    self.nValue = _nValue
    self.fPointer = _fPointer
    self.bPointer = _bPointer

dataSets = {}
nodes = []
bias  = node("bias",0,0,0)
target = 0



@staticmethod
def netFunction(values,weights):
  total = 0
  for i in range(0,len(values)):
    total += (values[i]*weights[i])
  return total

@staticmethod
def sigmoidFunction(net):
  return 1/(1+math.exp(-net))

def getData(direc):
  arr = []
  with open(direc,'r') as fl:
    for line in fl:
      data = line.split()
      arr.append(data)
  return arr

def chooseDirectory():
  while True:
    listOfDirs = [f for f in glob.glob("*.txt")]
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


def populateDataSets(_dataSets):
  for i in range(0,len(_dataSets)):
    dataSets[f"DataSet{i}"] = _dataSets[i]

populateDataSets(getData(chooseDirectory()))

print(dataSets)