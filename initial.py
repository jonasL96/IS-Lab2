import random
import numpy
import array
import math

x = [0.0] * 20
eta = 0.1  # learning rate
i = 0

# Generating the 20 x values vector
while i < 20:
    a = random.uniform(0, 1)
    x[i] = a
    i = i + 1

w = [0.0] * 5
b = [0.0] * 5

i = 0
while i < 5:
    w[i] = random.uniform(0, 1)
    b[i] = random.uniform(0, 1)
    i = i + 1
# Calculating v values
i = 0
q = 0
r = 0
v = [0.0] * (len(x) * len(w))
d = [0.0] * 20
# Desired output
while i < len(x):
    d[i] = (1 + 0.6 * math.sin(2 * math.pi * x[i] / 0.7)) + 0.3 * (math.sin(2 * math.pi * x[i])) / 2
    i = i + 1
i = 0
q = 0
p = len(x) * len(w)
y = [0.0] * p
e = [0.0] * p
# calculating actual output
while i < 20:
    while q < 5:
        v[q] = x[i] * w[q] + b[q]
        y[i] = 1 / (1 + math.exp(v[q]))
        q = q + 1
    # Calculating error
    e[i] = d[i] - y[i]
    i = i + 1
    if q == 5:
        q = 0
e_total = sum(e)
e_total = round(e_total, 0)  # rounded so there's no additional numbers after comma
print(e_total)
#Learning algorithm
iterations = 2000 #times we will execute this
i = 0
r = 0
q = 0
while i < iterations:
    while e_total > 0:
        while r < 20:
            #Updating weights
            while q < 5:
                st = (-1)*(x[r]*w[q]-b[q])
                de[q] = (1/(1 + math.exp(st)))*(1-(1/(1+math.exp(st)*e[r])))
                w[q] = w[q]+eta*de[q]*x[r]
                b[q] = b[q] + eta*de[q]
               q = q + 1
            r = r + 1
            if q == 5:
                q = 0

        #calculating y and error with updated weights
        while o < 20: #to be continued
            #st = 
            y[o] = 1/(1+math.exp(st))
            #error
            e[o] = d[o] - y[o]
        #total error
        e_total = sum(e)
        e_total = round(e_total, 0)
        print(e_total)

