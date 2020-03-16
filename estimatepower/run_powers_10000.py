import numpy as np
import re
import os

root = "experiments/estimatepower/"

with open(root+"grow_power10000.json",'r') as f:
    grow = f.read()
    f.close()

with open(root+"like_power10000.json",'r') as f:
    like = f.read()
    f.close()

growtmp = root+"grow_power.tmp2"
liketmp = root+"like_power.tmp2"
dump = root+"likedump.tmp2"

params = np.linspace(2.0,2.0,num=1)
guesses = np.linspace(-0.1,2.1,num=111)

for p in params:
    pstring = str(round(p,2))
    graphname = "DP"+pstring+"10000.dat"
    tmp1 = re.sub("NAME", graphname, grow)
    tmp2 = re.sub("AAA", pstring, tmp1)
    param_file = root+"likelihoods/like-10000-3-test"+pstring+".dat"
    for _ in range(10):
        with open(growtmp,'w') as f:
            f.write(tmp2)
            f.close()
        os.system("java -jar feta3-1.0.0.jar "+growtmp)
        tmp3 = re.sub("NAME", graphname, like)
        max_likelihood = 0.0
        max_param = 0
        for g in guesses:
            tmp4 = re.sub("BBB", str(g), tmp3)
            with open(liketmp,'w') as f:
                f.write(tmp4)
                f.close()
            os.system("java -jar feta3-1.0.0.jar "+liketmp+" > "+dump)
            with open(dump,'r') as f:
                likelihood = float(f.read().strip())
                f.close()
            if likelihood>max_likelihood:
                max_likelihood=likelihood
                max_param = g
        os.system("rm "+root+"graphfiles/"+graphname)
        with open(param_file,'a+') as f:
            f.write(str(max_param)+"\n")
            f.close()
