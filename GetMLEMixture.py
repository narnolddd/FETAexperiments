import numpy as np
import math
import matplotlib.pyplot as plt
from textwrap import wrap

# set up figure
fig = plt.figure()
ax = plt.axes()
ax.xaxis.label.set_fontsize(12)
ax.yaxis.label.set_fontsize(12)
plt.xlabel('Mixture Parameter $\\beta$')
plt.ylabel('Error (RMSE)')
plt.title('Recovery performance in 10000 node network')
ax.set_ylim([0,0.1])

# set up parameter space
links = [str(k) for k in range(1,6)]
params = np.linspace(0.0, 1.0, num=11)
noparams = len(params)
experiments = 10

for link in links:
    MLEtable = np.zeros((noparams,experiments),dtype=float)
    for i in range(noparams):
        param = round(params[i],1)
        file = "BArankpref/BARank10000-"+link+"-results"+str(param)+".dat"
        with open(file,'r') as f:
            lines = f.read().splitlines()
            MLEtable[i,:] = [float(r.split()[1].strip()) for r in [lines[k] for k in range(len(lines)-10, len(lines))]]
            f.close()

    means = [sum(row)/experiments for row in MLEtable]
    sds = [math.sqrt(sum((MLEtable[i,:] - means[i])**2)/experiments) for i in range(noparams)]

    mse = [math.sqrt(sum((params[j] - MLEtable[j,:])**2)/experiments) for j in range(noparams)]
    kse = [max(abs(params[j]-MLEtable[j,:])) for j in range(noparams)]

    ax.plot(params,mse, marker='o', linestyle='-', label=link+" links",linewidth=float(link))

plt.tight_layout(h_pad=0)
plt.legend(loc='upper left')
plt.show()