from cmath import pi
import numpy as np
import matplotlib as plt

jPerp = input("J_perp")
jPar = input("J_par")

k = np.arange(-pi, pi, 0.1)

def f(k):
    return np.sqrt(jPerp**2 + 2 * jPerp * jPar * np.cos(k))

def g(k):
    return jPerp + jPar * np.cos(k)

plt.figure()
plt.plot(k, f(k), k, g(k))
plt.show()