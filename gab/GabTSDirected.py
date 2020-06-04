import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime as dt

fig, ax = plt.subplots(nrows=2, ncols=4, figsize=(15,5))

# Get time axes set up
x_major_lct = mpl.dates.AutoDateLocator(minticks=2,maxticks=10, interval_multiples=True)
x_fmt = mpl.dates.AutoDateFormatter(x_major_lct)

plt.xlabel("Timestamp")
ax[0,0].set_title('Average Degree')
ax[0,1].set_title('Maximum degree')
ax[0,2].set_title('Clustering')
ax[0,3].set_title('Mean squared degree')
ax[1,0].set_title('Degree assortativity')
ax[1,1].set_title('Singletons')
ax[1,2].set_title('Doubletons')
ax[1,3].set_title('Triangles')


# File with all the time series of measurements
file = "experiments/gab/aggregate_measurements_directed.dat"

# Read stats from datafile
with open(file,'r') as f:
    f.readline()
    rawdata = f.read().splitlines()
    times = [dt.datetime.fromtimestamp(int(l.split()[0])) for l in rawdata]
    matrix = np.array([[int(row.split()[0])]+[float(num) for num in row.split()[1:]] for row in rawdata])
    df = pd.DataFrame(matrix)
    f.close()

df.columns = ['timestamp', 'nodes', 'links', 'avgdegin', 'maxdegin', 'maxdegout', 'singin', 'singout', 'doubin',
              'doubout', 'meandegsqin', 'meandegsqout', 'assortinin', 'assortinout', 'assortoutin', 'assortoutout',
              'cluster', 'transtri', 'cyclictri']

ax[0,0].plot(times, df['avgdegin'], color='red', label='In')

ax[0,1].plot(times, df['maxdegin'], color='red', label='In')
ax[0,1].plot(times, df['maxdegout'], color='blue', label='Out')

ax[0,2].plot(times, df['cluster'], color='red', label='Transitivity')

ax[0,3].plot(times, df['meandegsqin'], color='red', label='In')
ax[0,3].plot(times, df['meandegsqout'], color='blue', label='Out')

ax[1,0].plot(times, df['assortinin'], color='red', label='In-in')
ax[1,0].plot(times, df['assortinout'], color='red', label='In-out', linestyle='--')
ax[1,0].plot(times, df['assortoutout'], color='blue', label='Out-out')
ax[1,0].plot(times, df['assortoutin'], color='blue', label='Out-in', linestyle='--')

ax[1,1].plot(times, df['singin'], color='red', label='In')
ax[1,1].plot(times, df['singout'], color='blue', label='Out')

ax[1,2].plot(times, df['doubin'], color='red', label='In')
ax[1,2].plot(times, df['doubout'], color='blue', label='Out')

ax[1,3].plot(times, df['transtri'], color='red', label='Transitive')
ax[1,3].plot(times, df['cyclictri'], color='blue', label='Cyclic')

for row in range(2):
    for col in range(4):
        ax[row,col].legend(loc='lower right')
        ax[row,col].xaxis.set_major_locator(x_major_lct)
        ax[row,col].xaxis.set_major_formatter(x_fmt)
        for label in ax[row,col].get_xmajorticklabels():
            label.set_rotation(30)
        for label in ax[row,col].get_ymajorticklabels():
            label.set_rotation(30)


plt.tight_layout()
fig.savefig("experiments/gab/GabTSDirected.png")
plt.show()