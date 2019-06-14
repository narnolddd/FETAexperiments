import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime as dt
from collections import defaultdict

fig, ax = plt.subplots(nrows=2, ncols=4, figsize=(20,10))

x_major_lct = mpl.dates.AutoDateLocator(minticks=2,maxticks=10, interval_multiples=True)
x_fmt = mpl.dates.AutoDateFormatter(x_major_lct)

plt.xlabel("Timestamp")
ax[0,0].set_title('Maximum Degree')
ax[0,0].xaxis.set_major_locator(x_major_lct)
ax[0,0].xaxis.set_major_formatter(x_fmt)
ax[0,1].set_title('Average Clustering Coefficient')
ax[0,2].set_title('Mean squared degree')
ax[0,3].set_title('Degree Assortativity')
ax[1,0].set_title('Singleton Nodes')
ax[1,1].set_title('Doubleton Nodes')
ax[1,2].set_title('Number of Triangles')

complinestyle= defaultdict(lambda: '--')
complinestyle['BestMix']='-'
complinestyle['Real']='-'

compthickness=defaultdict(lambda: 1)
compthickness['BestMix'] = 3
compthickness['Real'] = 3
compalpha = 1

experiments = 10
root = "experiments/facebook/averaged/"
models = ['Real','BestMix', 'DP', 'Rand', 'Tri']

def get_dfs(model):
    dfs={}

    for ex in range(experiments):
        if model == 'Real':
            name = root+model+"Measurements.dat"
        else:
            name = root+model+"-"+str(ex)+"-Measurements.dat"
        with open(name,'r') as f:
            rawdata = f.read().splitlines()
            times = [dt.datetime.fromtimestamp(int(l.split()[0])) for l in rawdata]
            print(times)
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

    lineobjects[label]=ax[0,0].plot(times, averages['maxdeg'],label=label, linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[0,1].plot(times, averages['clustercoeff'],label=label, linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[0,2].plot(times, averages['meandegsq'], label=label, linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[0,3].plot(times, averages['assortativity'], label=label, linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[1,0].plot(times, averages['singletons'], label=label, linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[1,1].plot(times, averages['doubletons'], label=label, linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[1,2].plot(times, averages['triangles'], label=label, linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)

for row in range(2):
    for col in range(4):
        if [ row, col ]== [1,3]:
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
