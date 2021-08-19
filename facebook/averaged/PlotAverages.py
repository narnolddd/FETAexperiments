import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime as dt
from collections import defaultdict

a4_dims = (8.27,11.69)
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
compcol['DP'] = '#ff7f0e'
compcol['Tri'] = '#2ca02c'
compcol['Rand'] = '#d62728'

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

def get_stds(dfs):
    stds = pd.concat(dfs).groupby(level=1).std()
    stds.columns = ['timestamp', 'nodes', 'links', 'avgdeg', 'density', 'maxdeg', 'clustercoeff', 'meandegsq',
                        'assortativity', 'cutoff', 'singletons', 'doubletons', 'triangles']
    return stds

lineobjects={}


for model in models:
    if model=="BestMix":
        label='$0.61M_{DP}(0.8) + 0.33M_{rand} + 0.06M_{tri}(15)$'
    if model=="DP":
        label="$M_{DP}(0.8)$"
    if model=="Rand":
        label="$M_{rand}$"
    if model=="Tri":
        label="$M_{tri}(15)$"
    if model=="Real":
        label="Real data measurements"
    dfs, times = get_dfs(model)
    averages = get_averages(dfs)
    stds = 0.5* get_stds(dfs)

    lineobjects[label]=ax[0,0].plot(times, averages['maxdeg'], color= compcol[model], label=label, linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[0,0].fill_between(times, averages['maxdeg']-stds['maxdeg'], averages['maxdeg']+stds['maxdeg'], color=compcol[model], alpha=0.2)

    ax[1,0].plot(times, averages['clustercoeff'],label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[1,0].fill_between(times, averages['clustercoeff']-stds['clustercoeff'], averages['clustercoeff']+stds['clustercoeff'], color=compcol[model], alpha=0.2)

    ax[0,1].plot(times, averages['meandegsq'], label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[0,1].fill_between(times, averages['meandegsq']-stds['meandegsq'], averages['meandegsq']+stds['meandegsq'], color=compcol[model], alpha=0.2)

    ax[3,0].plot(times, averages['assortativity'], label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[3,0].fill_between(times, averages['assortativity']-stds['assortativity'], averages['assortativity']+stds['assortativity'], color=compcol[model], alpha=0.2)

    ax[2,0].plot(times, averages['singletons']/10000, label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[2,0].fill_between(times, averages['singletons']/10000-stds['singletons']/10000, averages['singletons']/10000+stds['singletons']/10000, color=compcol[model], alpha=0.2)
    ax[2,1].plot(times, averages['doubletons'], label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[2,1].fill_between(times, averages['doubletons']-stds['doubletons'], averages['doubletons']+stds['doubletons'], color=compcol[model], alpha=0.2)

    ax[1,1].plot(times, averages['triangles']/100000, label=label, color= compcol[model], linestyle=complinestyle[model], linewidth=compthickness[model], alpha=compalpha)
    ax[1,1].fill_between(times, averages['triangles']/100000-stds['triangles']/100000, averages['triangles']/100000+stds['triangles']/100000, color=compcol[model], alpha=0.2)

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
fig.legend([lineobjects[item] for item in lineobjects.keys()], labels=[lineobjects[item][0].get_label() for item in lineobjects.keys()], bbox_to_anchor=(0.75,0.15), loc='center')
plt.xticks(rotation='vertical')
plt.tight_layout()
plt.savefig("/Users/narnolddd/Documents/PhDMAIN/NaomiThesis/plots/fb_comparisons_3.pdf")
plt.show()
