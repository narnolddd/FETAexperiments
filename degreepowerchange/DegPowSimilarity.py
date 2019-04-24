import networkx as nx
import numpy as np
import math
import matplotlib.pyplot as plt

# read file

file = "degreepowerchange/growerror.dat"
power1 = 2.0
power2 = 1.0

with open(file,'r') as f:
    edgelist=f.read().splitlines()

def compute_similarity(p1, p2, net):
    degrees = np.array([net.degree(node) for node in net.nodes()])
    numerator = sum(np.power(degrees,p1+p2))/len(degrees)
    denom1 = sum(np.power(degrees,2*p1))/len(degrees)
    denom1 = math.sqrt(denom1)
    denom2 = sum(np.power(degrees,2*p2))/len(degrees)
    denom2 = math.sqrt(denom2)
    final = numerator/(denom1 * denom2)
    return final

G = nx.Graph()
times = range(100,10000,100)
similarities=[]

ct=0
for edge in edgelist:
    if ct == len(times):
        break
    src, dst, time = edge.split()
    time = int(time)
    if time>times[ct]:
        similarities.append(compute_similarity(power1,power2,G))
        ct= ct+1
    G.add_edge(src,dst)

fig = plt.figure()
ax = plt.axes()
plt.xlabel('Network Size')
plt.ylabel('Similarity')
plt.plot(times,similarities, label='Degree Power '+str(power1)+" to "+str(power2))
plt.legend(loc='lower right')
plt.show()