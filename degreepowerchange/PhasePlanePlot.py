import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.colors as colors

file = "PhasePlaneMLEs1000.txt"
noParams = 13

MLEmatrix = np.zeros((noParams, noParams), dtype=float)

def getindex(param):
    index = int(round((param-0.8)*10))
    return index

with open(file,'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        parts = line.split()
        param1, param2 = float(parts[0]), float(parts[1])
        MLEs = 10*np.array([float(x) for x in parts[2].split(',')])
        RMSE = np.sqrt(1.0/len(MLEs) * sum((MLEs - 500)**2))
        MLEmatrix[getindex(param1),getindex(param2)]=RMSE+0.0001

ax = sns.heatmap(MLEmatrix,linewidth=0.5 ,norm=colors.LogNorm(vmin=0.0001,vmax=500))
plt.show()