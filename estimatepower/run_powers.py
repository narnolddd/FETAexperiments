import numpy as np
import re
import os
import sys

root = "experiments/estimatepower/"
links = str(sys.argv[1])

with open(root+"grow_power.json",'r') as f:
    grow = f.read()
    f.close()

with open(root+"like_power.json",'r') as f:
    like = f.read()
    f.close()

growtmp = root+"grow_power.tmp"
liketmp = root+"like_power.tmp"
dump = root+"likedump.tmp"

params = np.linspace(0.0,2.0,num=21)
guesses = np.linspace(-0.1,2.1,num=111)

for p in params:
    print(p)
    pstring = str(round(p,2))
    graphname = "DP-"+links+"-"+pstring+".dat"
    tmp1 = re.sub("NAME", graphname, grow)
    tmp2 = re.sub("AAA", pstring, tmp1)
    tmp3 = re.sub("LINKS", links, tmp2)
    param_file = root+"likelihoods/like-1000-"+links+"-"+pstring+".dat"
    for _ in range(10):
        with open(growtmp,'w') as f:
            f.write(tmp3)
            f.close()
        os.system("java -jar feta3-1.0.0.jar "+growtmp)
        tmp4 = re.sub("NAME", graphname, like)
        max_likelihood = 0.0
        max_param = 0
        for g in guesses:
            tmp5 = re.sub("BBB", str(g), tmp4)
            with open(liketmp,'w') as f:
                f.write(tmp5)
                f.close()
            os.system("java -jar feta3-1.0.0.jar "+liketmp+" > "+dump)
            with open(dump,'r') as f:
                likelihood = float(f.read().strip().split()[1])
                f.close()
            if likelihood>max_likelihood:
                max_likelihood=likelihood
                max_param = g
        os.system("rm "+root+"graphfiles/"+graphname)
        with open(param_file,'a+') as f:
            f.write(str(max_param)+"\n")
            f.close()
