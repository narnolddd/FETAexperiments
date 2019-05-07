import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import datetime as dt

fig, ax = plt.subplots(nrows=2, ncols=4, figsize=(24,4))

plt.xlabel("Timestamp")

x_major_lct = mpl.dates.AutoDateLocator(minticks=2,maxticks=10, interval_multiples=True)
x_fmt = mpl.dates.AutoDateFormatter(x_major_lct)

ax[0,0].set_title('Maximum Degree')
ax[0,0].xaxis.set_major_locator(x_major_lct)
ax[0,0].xaxis.set_major_formatter(x_fmt)
ax[0,1].set_title('Average Clustering Coefficient')
ax[0,2].set_title('Mean squared degree')
ax[0,3].set_title('Degree Assortativity')
ax[1,0].set_title('Singleton Nodes')
ax[1,1].set_title('Doubleton Nodes')
ax[1,2].set_title('Number of Triangles')

root = "experiments/citations/Citations_Last10_"

realdata = root+"Measurements.dat"

rdthickness = 2
mixthickness = 2
compthickness = 1

rdalpha = 1
mixalpha = 1
compalpha = 0.7

rdlinestyle = '-'
mixlinestyle = '-'
complinestyle = '--'

mixturefiles = ["BATriPFP-0.02_Measurements.dat"]
componentfiles = ["BA_Measurements.dat", "Tri_Measurements.dat"]
mixnames = [m.strip("_Measurements.dat") for m in mixturefiles]
compnames = [c.strip("_Measurements.dat") for c in componentfiles]

mixtures = [root+f for f in mixturefiles]
components = [root+g for g in componentfiles]

lineobjects={}

mixlabel = "0.32 PFP -0.02, 0.67 Tri, 0.01 BA"

with open(realdata,'r') as rd:
    lines = rd.read().splitlines()
    times = [dt.datetime.fromtimestamp(int(l.split()[0])) for l in lines]
    maxdeg = [int(l.split()[5]) for l in lines]
    cc = [float(l.split()[6]) for l in lines]
    meandegsq = [float(l.split()[7]) for l in lines]
    assort = [float(l.split()[8]) for l in lines]
    singles = [int(l.split()[10]) for l in lines]
    doubles = [int(l.split()[11]) for l in lines]
    triangles = [int(l.split()[12]) for l in lines]
    rd.close()

lineobjects["real"]=ax[0,0].plot(times, maxdeg, linewidth=rdthickness, color='black', label='Real Data')
ax[0,1].plot(times, cc, linewidth=rdthickness, color='black', label='Real Data')
ax[0,2].plot(times, meandegsq, linewidth=rdthickness, color='black', label='Real Data')
ax[0,3].plot(times, assort, linewidth=rdthickness, color='black', label='Real Data')
ax[1,0].plot(times, singles, linewidth=rdthickness, color='black', label='Real Data')
ax[1,1].plot(times, doubles, linewidth=rdthickness, color='black', label='Real Data')
ax[1,2].plot(times, triangles, linewidth=rdthickness, color='black', label='Real Data')

for mix in mixtures:
    with open(mix,'r') as m:
        lines = m.read().splitlines()
        times = [dt.datetime.fromtimestamp(int(l.split()[0])) for l in lines]
        maxdeg = [int(l.split()[5]) for l in lines]
        cc = [float(l.split()[6]) for l in lines]
        meandegsq = [float(l.split()[7]) for l in lines]
        assort = [float(l.split()[8]) for l in lines]
        singles = [int(l.split()[10]) for l in lines]
        doubles = [int(l.split()[11]) for l in lines]
        triangles = [int(l.split()[12]) for l in lines]
        m.close()

    lineobjects[mixlabel]=ax[0,0].plot(times, maxdeg,label=mixlabel, linestyle=mixlinestyle, linewidth=mixthickness, alpha=mixalpha)
    ax[0,1].plot(times, cc,label=mixlabel, linestyle=mixlinestyle, linewidth=mixthickness, alpha=mixalpha)
    ax[0,2].plot(times, meandegsq, label=mixlabel, linestyle=mixlinestyle, linewidth=mixthickness, alpha=mixalpha)
    ax[0,3].plot(times, assort, label=mixlabel, linestyle=mixlinestyle, linewidth=mixthickness, alpha=mixalpha)
    ax[1,0].plot(times, singles, label=mixlabel, linestyle=mixlinestyle, linewidth=mixthickness, alpha=mixalpha)
    ax[1,1].plot(times, doubles, label=mixlabel, linestyle=mixlinestyle, linewidth=mixthickness, alpha=mixalpha)
    ax[1,2].plot(times, triangles, label=mixlabel, linestyle=mixlinestyle, linewidth=mixthickness, alpha=mixalpha)

for comp in components:
    label = comp.strip(root).strip("_Measurements.dat")
    with open(comp,'r') as c:
        lines = c.read().splitlines()
        times = [dt.datetime.fromtimestamp(int(l.split()[0])) for l in lines]
        maxdeg = [int(l.split()[5]) for l in lines]
        cc = [float(l.split()[6]) for l in lines]
        meandegsq = [float(l.split()[7]) for l in lines]
        assort = [float(l.split()[8]) for l in lines]
        singles = [int(l.split()[10]) for l in lines]
        doubles = [int(l.split()[11]) for l in lines]
        triangles = [int(l.split()[12]) for l in lines]
        c.close()

    lineobjects[label]=ax[0,0].plot(times, maxdeg,label=label, linestyle=complinestyle, linewidth=compthickness, alpha=compalpha)
    ax[0,1].plot(times, cc,label=label, linestyle=complinestyle, linewidth=compthickness, alpha=compalpha)
    ax[0,2].plot(times, meandegsq, label=label, linestyle=complinestyle, linewidth=compthickness, alpha=compalpha)
    ax[0,3].plot(times, assort, label=label, linestyle=complinestyle, linewidth=compthickness, alpha=compalpha)
    ax[1,0].plot(times, singles, label=label, linestyle=complinestyle, linewidth=compthickness, alpha=compalpha)
    ax[1,1].plot(times, doubles, label=label, linestyle=complinestyle, linewidth=compthickness, alpha=compalpha)
    ax[1,2].plot(times, triangles, label=label, linestyle=complinestyle, linewidth=compthickness, alpha=compalpha)

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
