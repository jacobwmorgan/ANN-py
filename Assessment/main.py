from math import exp

#, , , , , , 


class Network:
  def __init__(self, _weights , _layers , _learningR):
    self.w = _weights
    self.layers = _layers
    self.learningR = _learningR 
    
  def __repr__(self):
    return "Network:{}".format("-".join(str(i) for i in self.layers))
  
  @staticmethod 
  def sigmoid(self,net):
    return 1.0/(1+exp(-net))

  @staticmethod
  def sigmoidDerivative(self,net):
    return net * (1 - net) 
  
  @staticmethod
  def netFunction(self,values,weights)
    net = 0
    for i in range(0,len(values)):
        temp = values[i] * weights[i]
        net = net + temp
    return net
  
  
 
  
  



weights = [[0.9, 0.45, 0.36, 0.98,0.92],[0.74,0.13,0.68],[0.8,0.4,0.10],[0.35, 0.97, 0.96],[0.35,0.8],[0.50,0.13],[0.90,0.8]]

n = Network(weights,[4,3,2],0.1)
print(n)
