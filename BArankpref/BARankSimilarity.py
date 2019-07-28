import networkx as nx
import numpy as np

def getSimilarity(net):
    degrees = [net.degree(node) for node in net.nodes()]
    rankpowers = [np.power(i+1, -0.5) for i in range(len(net.nodes()))]
    numerator = sum([degrees[j]*rankpowers[j] for j in range(len(net.nodes))])
    den1 = np.sqrt(sum([rankpowers[j]*rankpowers[j] for j in range(len(rankpowers))]))
    den2 = np.sqrt(sum([degrees[j]*degrees[j] for j in range(len(degrees))]))
    denominator = den1*den2
    return numerator/denominator

grow

params = [str(round(par,1)) for par in np.linspace(0.0,1.0,11)]

for size in ["1000", "10000"]:
    result = "Similarities-"+size+".txt"
    means = []
    sds = []
    for par in params:
        similarity = 0.0
        for ex in range(10):
            file = "BARank-"+size+"-3-"+par+".dat"
            G = nx.Graph()
            with open(file,'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    n1, n2 = line.split()[0], line.split()[1]
                    G.add_edge(n1,n2)
                f.close()
            similarity = getSimilarity(G)
        print(similarity)
        with open(result,'a') as r:
            r.write(par+" "+str(similarity)+"\n")
            r.close()