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
d = [0.0] * 20
#Desired output
while i < len(x):
    d[i] = (1+0.6*math.sin(2*math.pi*x[i]/0.7))+0.3*(math.sin(2*math.pi*x[i]))/2
    i = i + 1
i = 0
q = 0
r = 0
p = len(x)*len(w)
y = [0.0] * p
e = [0.0] * p
#calculating actual output
while i < 20:
    while q < 5:
        v[q] = x[i]*w[q]+b[q]
        y[q] = 1/(1+math.exp(v[q]))
        q = q + 1
    #Calculating error
    e[i] = d[i] - y[i]
    i = i + 1
e_total = sum(e)
e_total = round(e_total,0) #rounded so there's no additional numbers after comma
print(e_total)

#Learning algorithm
iterations = 2000 #times we will execute this
i = 0
q = 0
r = 0
while i < iterations:
    while q < 20:
        a = a + eta*e(q)
        while r < 5:
            s = e[q]
            w[r] = w[r] + eta*s[r]*x[q]
            b[r] = w[r] + eta*s[r]
        q = q + 1
