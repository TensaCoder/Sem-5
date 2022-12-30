import numpy as np
import matplotlib.pyplot as plt

def linear(x):
    ''' y = f(x) It returns the input as it is'''
    return x

x = np.linspace(-10, 10)
print(x)
plt.plot(x, linear(x))
plt.axis('tight')
plt.title('Activation Function :Linear')
plt.show()