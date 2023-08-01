import sys
import matplotlib
import numpy as np

# inputs represent the input nodes of the Neural Network
inputs = [1.2, 5.1, 2.1]
# weiights that hold corresponding weight values
weights = [3.1, 2.1, 8.7]

bias = 3

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
print(output)


