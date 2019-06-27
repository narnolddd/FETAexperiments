import numpy as np
import re
import os
import multiprocessing as mp

likefile = "experiments/enron/changepoint/CPLikelihood.json"
likedata = ""
results= "experiments/enron/changepoint/BruteForceResults.txt"

with open(likefile,'r') as f:
    likedata=f.read()
    f.close()

def likelihood(T):
    Tstring = str(int(T))
    newfile = "experiments/enron/changepoint/CPLikelihood"+str(Tstring)+".tmp"
    likedump = "experiments/enron/changepoint/CPLikeDump"+str(Tstring)+".tmp"
    with open(newfile,'w') as f:
        newlikedata=re.sub("TTT",str(Tstring),likedata)
        f.write(newlikedata)
        f.close()
    os.system("java -jar feta3-1.0.0.jar "+newfile+" > "+likedump)
    with open(likedump,'r') as g:
        likelihood_value=float(g.read().splitlines()[-1].strip())
        g.close()
    os.system("rm "+likedump)
    os.system("rm "+newfile)
    return likelihood_value

tA = 997747200
tB = 1024099200

times = [int(np.round(t)) for t in np.linspace(tA, tB, 21)]

pool = mp.Pool(mp.cpu_count())
likelihoods = pool.map(likelihood, [T for T in times])
pool.close()

with open(results,'w') as f:
    for i in range(21):
        f.write(str(int(times[i]))+" "+str(likelihoods[i])+"\n")
    f.close()