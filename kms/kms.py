import math
import random
 
class node:
    
    def __init__(self,_nodeNum, _weights, _inputs, _outputs):
        self.inputs = _inputs
        self.outputs = _outputs 
        self.weights = _weights
        self.nodeNum = _nodeNum

        
    def net(self):
        net_sum = 0.0
        for i in range(0,len(self.inputs)):
            net_sum += (self.weights[i] * self.inputs[i])
        return net_sum
    
    def sigmoid(self):
       return  1 / (1 + math.exp(-self.net()))
            
   
   
   
class Network():
    def __init__(self,_inputs,_hidden,_output):
        self.inputs = _inputs
        self.hidden = _hidden
        self.output = _output
    
    def forwardstep(self):
        fwoutput = []
        for node in self.hidden:
            fwoutput.append(node.sigmoid())
        fwoutput = [1] + fwoutput
        for node in self.output:
            node.input = fwoutput
            print(node.input)
        fwoutput = []
        for node in self.output:
            print(f"{node.nodeNum} | {node.net()}")
            fwoutput.append(node.net())
        print(fwoutput)
            
    def errorFunc(self):
        target = [1,0]
        for node in self.output:
            n7_error = target[0] - self.output[0]
        print (n7_error)
             
    def backwardstep(nodelist):
        pass
        
        
             

nodelist = []
node4 = node(4,[0.9,0.74,0.8,0.35],[],[])      
nodelist.append(node4)       
node5 = node(5,[0.45,0.13,0.4,0.97],[],[])
nodelist.append(node5)
node6 = node(6,[0.36,0.68,0.1,0.96],[],[])
nodelist.append(node6)
node7 = node(7,[0.98,0.35,0.5,0.9],[],[])
nodelist.append(node7)
node8 = node(8,[0.92,0.8,0.13,0.8],[],[])
nodelist.append(node8)
    

data = [[1,0.50,1.00,0.75],
    [1,1.0,0.50,0.75],
    [1,1.00,1.00,1.00],
    [1,-0.01,0.50,0.25],
    [1,0.50,-0.25,0.13],
    [1,0.01,0.02,0.05]]

for node in nodelist:
    for i in data[0]:
        node.inputs.append(i)
    
hiddenLayer = [node4,node5,node6]
outputLayer = [node7,node8]

for node in outputLayer:
  print(node.inputs)
    
n = Network(data[0],hiddenLayer,outputLayer)
n.forwardstep()

for node in outputLayer:
  print(node.inputs)