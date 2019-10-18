import random
import numpy
import array
import math

x = [0.0]*20
eta = 0.1 #learning rate
i = 0

#Generating the 20 x values vector
while i < 20:
  a = random.uniform(0,1)
  x[i] = a
  i = i + 1

w = [0.0]*5
b = [0.0]*5

i = 0
while i < 5:
  w[i] = random.uniform(0,1)
  b[i] = random.uniform(0,1)
  i = i + 1
#Calculating v values
i = 0
q = 0
r = 0
v = [0.0] * (len(x)*len(w))
while i < 20:
    while q < 5:
        v[r] = x[i]*w[q]+b[q]
        r = r + 1
        q = q + 1
    i = i + 1
#Generating desired output
p = len(x)*len(w)
d = [0.0] * p
i = 0
while i < p:
    d[i] = random.choice([0,0.5,1])
#calculating actual output
i = 0
q = 0
r = 0
y = [0.0] * p
e = [0.0] * p
while i < p:
     y[i] = 1/(1+math.exp(v[i]))
     #calculating error here
     e[i] = d[i] - y[i]
     i = i + 1
e_total = sum(e)
#Learning algorithm
iterations = 2000 #times we will execute this
i = 0
while i < iterations:
    while q < 20:  
        a = a + eta*e(q)
        
    
