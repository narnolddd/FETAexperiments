import numpy as np
import re
import os

likefile = "experiments/enron/changepoint/CPLikelihood.json"
likedata = ""

with open(likefile,'r') as f:
    likedata=f.read()

gr = (np.sqrt(5) + 1) / 2

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

def find_max():
    tA = 997747200
    tB = 1024099200
    tC = np.floor(tB - (tB - tA)/gr)
    tD = np.ceil(tA + (tB - tA)/gr)

    yC = likelihood(tC)
    yD = likelihood(tD)

    while True:
        if abs(yC-yD) < 0.005:
            return yC, yD, tC, tD
        if yC < yD:
            tA = tC
            tC = tD
            yC = yD
            tD = np.ceil(tA + (tB - tA)/gr)
            yD = likelihood(tD)
            print(yC,yD,tC,tD)
        else:
            tB = tD
            tD = tC
            yD = yC
            tC = np.floor(tB - (tB - tA)/gr)
            yC = likelihood(tC)
            print(yC,yD,tC,tD)

find_max()