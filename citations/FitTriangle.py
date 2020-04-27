import warnings
warnings.filterwarnings("ignore")
import os
import re
import numpy as np

## File for fitting the NoRecents parameter for the triangle model in cit-hep-ph dataset

trials = range(1,21)
powers = np.linspace(0.8,1.5,8)

lf = "experiments/citations/FitNoCP.json"
lt = "experiments/citations/Fit.tmp"
dump = "experiments/citations/likedump.tmp"
results = "experiments/citations/trianglefitsall.dat"

with open(lf,'r') as f:
    likedata = f.read()
    f.close()

with open(results,'w') as g:
    for t in trials:
        for p in powers:
            like, DP, Rand, Tri = 0.0, 0.0, 0.0, 0.0
            tmp = re.sub("NNN",str(t),likedata)
            tmp2 = re.sub("PPP",str(p),tmp)
            with open(lt,'w') as f:
                f.write(tmp2)
                f.close()
            os.system("java -jar feta3-1.0.0.jar "+lt+" > "+dump)

            with open(dump,'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    # Ignore the lines starting with "Processing events as links..."
                    if "Processing" in line:
                        continue
                    if "Max" in line:
                        parts = line.split()
                        like = float(parts[3])
                        continue
                    parts = line.split()
                    if "Degree" in parts[1]:
                        DP = float(parts[0])
                        print(DP)
                        continue
                    if "Random" in parts[1]:
                        Rand = float(parts[0])
                        print(Rand)
                        continue
                    if "Triangle" in parts[1]:
                        Tri = float(parts[0])
                        print(Tri)
                        continue
                f.close()
            g.write(str(t)+" "+str(p)+" "+str(like)+" "+str(DP)+" "+str(Rand)+" "+str(Tri)+"\n")
    g.close()
