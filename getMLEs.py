import numpy as np
import math
import matplotlib.pyplot as plt
from textwrap import wrap

experiments=10

MLEtable = np.zeros((9,experiments),dtype=float)

for ex in range(experiments):
    file = "degreepowerchange/degreepower1.2-1-1000results"+str(ex)+".dat"
    lines=[]
    with open(file,'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            lines.append(line)
    data = " ".join(lines).strip('[').strip(']')
    paramstring = data.split('][')
    params = [[float(r.strip()) for r in row.strip().split()] for row in paramstring]

    for i in range(9):
        MLEtable[i,ex]=(np.argmax(params[i])+1)*10

means = [sum(row)/experiments for row in MLEtable]
sds = [math.sqrt(sum((MLEtable[i,:] - means[i])**2)/experiments) for i in range(9)]
truevals = range(100,1000,100)
mse = [math.sqrt(sum((truevals[j] - MLEtable[j,:])**2)/experiments) for j in range(9)]
kse = [max(abs(truevals[j]-MLEtable[j,:])) for j in range(9)]

fig, (ax0,ax1) = plt.subplots(nrows=2, sharex=True)

ax0.yaxis.label.set_fontsize(12)
ax1.yaxis.label.set_fontsize(12)
ax0.xaxis.label.set_fontsize(12)
ax1.xaxis.label.set_fontsize(12)

#fig.suptitle('Barabasi-Albert to Rank Preference')
plt.xlabel('Iteration number corresponding to changepoint')

ax0.errorbar(truevals,means,yerr=sds, fmt='o')
ax0.plot(truevals,truevals, linestyle='--', linewidth=1, label="Correct changepoint time")
#ax0.set_title('Estimated change point times (averaged over 50 experiments)')
ax0.set_ylabel('MLE of change point time \n (# iterations)')

#ax2.plot(truevals,kse, marker='o')
#ax2.set_ylim(0,200)
#ax2.set_title('KS error')

ax1.plot(truevals,mse, marker='o')
#ax1.set_title('Estimation error')
ax1.set_ylim(0,100)
ax1.set_ylabel('RMSE (# iterations)')

plt.tight_layout(h_pad=0)
plt.show()