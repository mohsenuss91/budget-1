import matplotlib.pyplot as plt
import numpy as np

dict = {'A': 40, 'B': 70, 'C': 30, 'D': 85, 'E': 85, 'F': 85, 'G': 85, 'H': 85, 'I': 85}
for i, key in enumerate(dict): 
	plt.bar(i, dict[key])
plt.xticks(np.arange(len(dict))+0.4, dict.keys());
plt.yticks(dict.values());
plt.show()
