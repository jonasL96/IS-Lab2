import random
import numpy
import array
import math

x = []
eta = 0.1 #learning rate
i = 0

#Generating the 20 x values vector
while i < 20:
  a = random.uniform(0,1)
  x.append(a)
  i = i + 1

print(x)
print("\n") #debug
y = []

i = 0
#Generating the desired output
while i < 20:
  #print("executed\n") #debug
  q1 = 2*math.pi*(x[i]/0.7)
  q2 = 2*math.pi*x[i]
  a1 = 1 + 0.6*math.sin(q1)
  a2 = (0.3*math.sin(q2))/2
  ind = a1+a2
  y.append(ind)
  i = i + 1

print(y)
