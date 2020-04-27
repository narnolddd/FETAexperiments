import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file = sys.argv[1]

degreeCount={}
degreeSeq = []

with open(file,'r') as f:
    ddist = f.readlines()[-1].split()

for i in range(len(ddist)):
    degreeCount[i]=int(ddist[i])
    degreeSeq += [i for _ in range(degreeCount[i])]

deg, cnt = zip(*degreeCount.items())
deg = np.array(deg)
print(deg)
cnt = np.array(cnt)

cdf = np.array([c for c in cnt]).cumsum(0)
cdf = cdf/float(cdf[-1])
ccdf = 1-cdf

a4_dims = (11.7, 8.27)

fig, ax = plt.subplots(2, figsize=a4_dims,sharex=True)

plt.xscale('log')
plt.xlim(3,1000)
plt.yscale('log')

plt.xlabel('Node degree $k$',fontsize=20)
ax[0].set_ylabel('$P(k)$', fontsize=20)
ax[0].set_yscale('log')
ax[1].set_ylabel('$P(K>k)$',fontsize=20)
ax[0].set_ylim(1,5000)
plt.tick_params(labelsize=20)

ax[0].scatter(0.00001+deg,0.00001+cnt,color='blue')
ax[1].plot(deg,ccdf,linewidth=3,color='blue')

plt.title("Degree distribution",fontsize=20)

plt.show()