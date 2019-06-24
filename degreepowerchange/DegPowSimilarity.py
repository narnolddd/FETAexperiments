import networkx as nx
import numpy as np
import math

# read file

params = [str(round(x,1)) for x in np.linspace(0.8,2.0,num=13)]
no_params = 13
similarity_matrix = np.zeros((no_params, no_params), dtype=float)
similarity_file = "SimilarityMatrix.txt"

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

def process_net(p1,p2,file):
    param1, param2 = float(p1), float(p2)
    G = nx.Graph()
    with open(file,'r') as f:
        edgelist = [line.split() for line in f.read().splitlines()]
        f.close()
    for edge in edgelist:
        if int(edge[2]) > 5000:
            break
        G.add_edge(edge[0], edge[1])
    sim = compute_similarity(param1,param2,G)
    return sim

with open(similarity_file,'a') as f:
    for i in range(no_params):
        for j in range(no_params):
            p1, p2 = params[i], params[j]
            file = "PP-100-"+p1+"-"+p2+".dat"
            similarity_matrix[i,j] = process_net(p1, p2, file)
            f.write(str(similarity_matrix[i,j])+" ")
        f.write('\n')
    f.close()
