import numpy as np
import matplotlib.pyplot as plt

total = "experiments/gab/aggregate_measurementsDeg.dat"
indeg = "experiments/gab/aggregate_measurements_directedInDeg.dat"
outdeg = "experiments/gab/aggregate_measurements_directedOutDeg.dat"

labels={}
labels[total]="Total"
labels[indeg]="In-Degree"
labels[outdeg]="Out-Degree"

colors={}
colors[total]='black'
colors[indeg]='red'
colors[outdeg]='blue'

for file in [total, indeg, outdeg]:
    with open(file,'r') as f:
        frequencies = [int(a) for a in f.read().splitlines()[-1].split()]
        frequencies = np.array(frequencies)
        f.close()
    s = float(frequencies.sum())
    cdf = frequencies.cumsum(0)/s
    ccdf = 1 - cdf
    plt.plot(range(len(ccdf)),ccdf, 'bo', label=labels[file], color=colors[file])

plt.yscale('log')
plt.xscale('log')
plt.xlabel('Degree $k$')
plt.ylabel('$P(X>k)$')
plt.legend(loc='lower left')
plt.tight_layout()

plt.savefig('experiments/gab/GabDegDist.png')
plt.show()