import os
import re
import numpy as np
import networkx as nx

nolinks = ['3']

file_grow = "experiments/BArankpref/BARankGrow1000.json"
grow_tmp = re.sub(".json","tmp.json",file_grow)
file_fit= "experiments/BArankpref/BARankFit.json"
fit_tmp = re.sub(".json","tmp.json",file_fit)
dump = "experiments/BArankpref/like.tmp"
results = "experiments/BArankpref/BARank1000-NUM-results.dat"
similarities = "experiments/BArankpref/BARank1000Similarities.dat"

numExperiments=10
betas = np.linspace(0.0,1.0,num=11)

with open(file_grow,'r') as fgrow:
    growdata = fgrow.read()
    fgrow.close()

def getSimilarity(net):
    degrees = [net.degree(node) for node in net.nodes()]
    rankpowers = [np.power(i+1, -0.5) for i in range(len(net.nodes()))]
    numerator = sum([degrees[j]*rankpowers[j] for j in range(len(net.nodes))])
    den1 = np.sqrt(sum([rankpowers[j]*rankpowers[j] for j in range(len(rankpowers))]))
    den2 = np.sqrt(sum([degrees[j]*degrees[j] for j in range(len(degrees))]))
    denominator = den1*den2
    return numerator/denominator

for ex in range(numExperiments):
    for link in nolinks:
        tmp = re.sub("NOLINKS",link, growdata)
        for beta in betas:
            beta = round(beta,1)
            tmp2 = re.sub("NAME","BARank-1000-"+link+"-"+str(beta),tmp)
            tmp2 = re.sub("AAA",str(beta),tmp2)
            tmp2 = re.sub("BBB",str(1-beta),tmp2)
            tmp3 = re.sub("NUM",link,tmp3)

            with open(grow_tmp,'w') as f:
                f.write(tmp3)
                f.close()
            os.system("java -jar feta3-1.0.0.jar "+grow_tmp)
            os.system("rm "+grow_tmp)

            with open(file_fit,'r') as ffit:
                fitdata = ffit.read()

            tmp3 = re.sub("NAME","BARank-1000-"+link+"-"+str(beta),fitdata)
            with open(fit_tmp,'w') as f2:
                f2.write(tmp3)
                f2.close()
            os.system("java -jar feta3-1.0.0.jar "+fit_tmp+" > "+dump)

            file = "experiments/BArankpref/BARank-1000-"+link+"-"+str(beta)+".dat"

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

            with open(similarities,'a+') as sfile:
                sfile.write(str(beta)+" "+str(similarity)+"\n")
                sfile.close()

            os.system("rm "+fit_tmp)

            with open(dump,'r') as like:
                fit = like.read().splitlines()
                betaguess = float(fit[1].strip().split(" ")[0])

            fres = open(re.sub("NUM-results",link+"-results"+str(beta),results), 'a+')
            fres.write(str(beta)+" "+str(betaguess)+"\n")
            fres.close()
