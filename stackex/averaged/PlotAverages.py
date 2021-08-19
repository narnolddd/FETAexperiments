import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime as dt
from collections import defaultdict

a4_dims=(8.27,11.69)
fig, ax = plt.subplots(nrows=4, ncols=2, figsize=a4_dims)

x_major_lct = mpl.dates.AutoDateLocator(minticks=2,maxticks=10, interval_multiples=True)
x_fmt = mpl.dates.AutoDateFormatter(x_major_lct)

plt.xlabel("Timestamp")
ax[0,0].set_title('Maximum Degree')
ax[0,0].xaxis.set_major_locator(x_major_lct)
ax[0,0].xaxis.set_major_formatter(x_fmt)
ax[1,0].set_title('Average Clustering Coefficient')
ax[0,1].set_title('Mean squared degree')
ax[3,0].set_title('Degree Assortativity')
ax[2,0].set_title('Singleton Nodes')
ax[2,1].set_title('Doubleton Nodes')
ax[1,1].set_title('Number of Triangles')

complinestyle= defaultdict(lambda: '--')
complinestyle['BestMix']='-'
complinestyle['Real']='-'

compthickness=defaultdict(lambda: 1)
compthickness['BestMix'] = 3
compthickness['Real'] = 3
compalpha = 1

compcol={}
compcol['Real'] = "black"
compcol['BestMix'] = '#1f77b4'
compcol['BA'] = '#ff7f0e'
compcol['TriInv25'] = '#2ca02c'
compcol['Rand'] = '#d62728'

experiments = 8
root = "experiments/stackex/averaged/"
models = ['Real','BestMix', 'BA', 'Rand', 'TriInv25']

def get_dfs(model):
    dfs={}

    for ex in range(experiments):
        if model == 'Real':
            name = root+"SX_Measurements.dat"
        else:
            name = root+model+"_"+str(ex)+"_Measurements.dat"
        with open(name,'r') as f:
            rawdata = f.read().splitlines()
            times = [dt.datetime.fromtimestamp(int(l.split()[0])) for l in rawdata]
            #print(times)
            matrix = np.array([[int(row.split()[0])]+[float(num) for num in row.split()[1:]] for row in rawdata])
            df = pd.DataFrame(matrix)
            dfs[ex]=df
            f.close()
    return dfs, times


def get_averages(dfs):
    averages=pd.concat(dfs).groupby(level=1).mean()
    averages.columns = ['timestamp', 'nodes', 'links', 'avgdeg', 'density', 'maxdeg', 'clustercoeff', 'meandegsq',
                        'assortativity', 'cutoff', 'singletons', 'doubletons', 'triangles']
    return averages

lineobjects={}


for model in models:
    label = model
    dfs, times = get_dfs(model)
    averages = get_averages(dfs)

    lineobjects[label]=ax[0,0].plot(times, averages['maxdeg'], color= compcol[model], label=label, linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[1,0].plot(times, averages['clustercoeff'],label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[0,1].plot(times, averages['meandegsq'], label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[3,0].plot(times, averages['assortativity'], label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[2,0].plot(times, averages['singletons'], label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[2,1].plot(times, averages['doubletons'], label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[1,1].plot(times, averages['triangles'], label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)

for row in range(4):
    for col in range(2):
        if [ row, col ]== [3,1]:
            continue
        ax[row,col].xaxis.set_major_locator(x_major_lct)
        ax[row,col].xaxis.set_major_formatter(x_fmt)
        for label in ax[row,col].get_xmajorticklabels():
            label.set_rotation(30)
        for label in ax[row,col].get_ymajorticklabels():
            label.set_rotation(30)

ax[-1, -1].axis('off')
fig.legend([lineobjects[item] for item in lineobjects.keys()], labels=[lineobjects[item][0].get_label() for item in lineobjects.keys()], loc="lower right")
plt.xticks(rotation='vertical')
plt.tight_layout()
plt.show()
