import numpy as np
import math
import matplotlib.pyplot as plt
from textwrap import wrap

params = np.linspace(0.0, 1.0, num=11)
noparams = len(params)
experiments = 10
MLEtable = np.zeros((noparams,experiments),dtype=float)

for i in range(noparams):
    param = round(params[i],1)
    file = "BArankpref/BARank10000results"+str(param)+".dat"
    with open(file,'r') as f:
        MLEtable[i,:] = [float(r.split()[1].strip()) for r in f.read().splitlines()]
        f.close()

means = [sum(row)/experiments for row in MLEtable]
sds = [math.sqrt(sum((MLEtable[i,:] - means[i])**2)/experiments) for i in range(noparams)]

mse = [math.sqrt(sum((params[j] - MLEtable[j,:])**2)/experiments) for j in range(noparams)]
print(means)
kse = [max(abs(params[j]-MLEtable[j,:])) for j in range(noparams)]
fig, (ax0,ax1) = plt.subplots(nrows=2, sharex=True)

ax0.yaxis.label.set_fontsize(12)
ax1.yaxis.label.set_fontsize(12)
ax0.xaxis.label.set_fontsize(12)
ax1.xaxis.label.set_fontsize(12)

ax0.errorbar(params,means,yerr=sds, fmt='o')
ax0.plot(params,params, linestyle='--', linewidth=1, label="Correct changepoint time")

ylabel0 = "\n".join(wrap("Recovered MLE mixture parameter",20))

plt.xlabel('Mixture parameter')
ax1.plot(params,mse, marker='o')
ax0.set_ylabel(ylabel0)
ax1.set_ylabel('RMSE')

plt.tight_layout(h_pad=0)
plt.show()