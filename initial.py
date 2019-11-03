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
v = [0.0] * 20
d = [0.0] * 20
# Desired output
while i < len(x):
    d[i] = (1 + 0.6 * math.sin(2 * math.pi * x[i] / 0.7)) + 0.3 * (math.sin(2 * math.pi * x[i])) / 2
    i = i + 1
i = 0
q = 0
e = [0.0] * 20
actual = [0.0] * 20
tmp = [0.0] * 20
# calculating actual output
while i < 20:
    while q < 5:
        v[q] = x[i] * w[q] + b[q]
        tmp[q] = 1 / (1 + math.exp(v[q]))
        actual[i] = actual[i] + tmp[q]
        q = q + 1
    # Calculating error
    e[i] = d[i] - actual[i]
    i = i + 1
    if q == 5:
        q = 0
e_total = sum(e)
e_total = round(e_total, 0)  # rounded so there's no additional numbers after comma
#Learning algorithm
iterations = 2000 #times we will execute this
i = 0
r = 0
q = 0
de = [0.0] * 20
while i < iterations:
    r = 0
    q = 0
    while r < 20:
        actual[r] = 0
        while q < 5:
            #Updating weights
            st = (-1)*(x[r]*w[q]-b[q])
            #delta parameter
            de[q] = (1/(1 + math.exp(st)))*(1-(1/(1+math.exp(st))))*e[r]
            #rest of the weights
            w[q] = w[q]+eta*de[q]*x[r]
            b[q] = b[q] + eta*de[q]
            # calculating y and error with updated weights
            st = (-1) * x[r] * w[q] - b[q]
            tmp[q] = 1/(1+math.exp(st))
            actual[r] = actual[r] + tmp[q]
            q = q + 1
        e[r] = d[r] - actual[r]
        r = r + 1
        if q == 5:
            q = 0
    #total error
    e_total = sum(e)
    e_total = round(e_total, 0)
    #print(e_total) # for debug
    i = i + 1
    if(e_total <= 0 and e_total > -0.01):
        print("Learning algorithm has found the 0 error solution and it took only %d executions" % (i))
        break
    if(i == iterations):
        print("Could not find a solution.")
