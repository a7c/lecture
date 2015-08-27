import matplotlib.pyplot as plt
import numpy as np

"""
	Calculates the upper bound on speedup based on Amdahl's law.
	params:
		p: number of processors
		alpha: fraction of work that is serial
"""
def amdahls(p, alpha):
	return 1. / (alpha + (1 - alpha) / p)

p = np.arange(1.0, 128.0, 1)

plt.xlabel('Number of processors')
plt.ylabel('Upper bound on speedup')
plt.xlim(0, 128)
plt.plot(p, amdahls(p, .1), 'bo')
plt.show()

print(amdahls(128, .1))