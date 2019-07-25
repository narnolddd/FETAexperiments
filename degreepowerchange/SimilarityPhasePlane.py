import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.colors as colors

file = "SimilarityMatrix.txt"

with open(file,'r') as f:
    matrix = np.array([[float(val) for val in row.split()] for row in f.read().splitlines()])
    f.close()

sim_matrix = pd.DataFrame(matrix, columns = [str(round(par,1)) for par in np.linspace(0.8, 2.0, num=13)])

plt.figure(figsize=(6,7))

class MidpointNormalize(colors.Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))

ax = sns.heatmap(sim_matrix, cmap="YlGnBu", norm=MidpointNormalize(midpoint=0.98),
                 yticklabels=[str(round(par,1)) for par in np.linspace(0.8, 2.0, num=13)],
                 cbar_kws={'label': 'RMS error (number of iterations)',
                           'orientation': 'horizontal'})

# ax = sns.heatmap(sim_matrix, cmap="YlGnBu", norm=colors.LogNorm(vmin=0.6, vmax=1),
#                  yticklabels=[str(round(par,1)) for par in np.linspace(0.8, 2.0, num=13)],
#                  cbar_kws={'label': 'RMS error (number of iterations)',
#                            'orientation': 'horizontal'})

cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=12)
cbar.set_label('Similarity at changepoint', fontsize=16)
ax.set_ylabel('Degree power exponent \n pre-changepoint',fontsize=16, wrap=True)
ax.set_xlabel('Degree power exponent \n post-changepoint',fontsize=16, wrap=True)

plt.tight_layout()
plt.show()