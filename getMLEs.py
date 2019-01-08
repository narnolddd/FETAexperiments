import numpy as np
import math
import matplotlib.pyplot as plt

MLEtable = np.zeros((9,10),dtype=float)

for ex in range(10):
    file = "results/RankBA1000results"+str(ex)+".dat"
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

means = [sum(row)/10 for row in MLEtable]
sds = [math.sqrt(sum((MLEtable[i,:] - means[i])**2)/10) for i in range(9)]
truevals = range(100,1000,100)

fig, ax = plt.subplots()
ax.errorbar(truevals,means,yerr=sds, fmt='o')
plt.plot(truevals,truevals, linestyle='-', linewidth=1)
ax.set_title('Estimated changepoint times from Rank-preference to BA against true values')

plt.show()
