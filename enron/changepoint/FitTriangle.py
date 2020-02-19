import warnings
warnings.filterwarnings("ignore")
import os
import re
import pandas as pd

## File for fitting the NoRecents parameter for the triangle model in Enron dataset

trials = range(1,21)

df = pd.DataFrame(columns=['trinumber', 'likelihood', 'BA', 'Rand', 'Tri'])

lf = "experiments/enron/Fit.json"
lt = "experiments/enron/Fit.tmp"
dump = "experiments/enron/likedump.tmp"
results = "experiments/enron/trianglefits.dat"

with open(lf,'r') as f:
    likedata = f.read()
    f.close()

with open(results,'w') as g:
    for t in trials:
        like, BA, Rand, Tri = 0.0, 0.0, 0.0, 0.0
        tmp = re.sub("NNN",str(t),likedata)
        with open(lt,'w') as f:
            f.write(tmp)
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
                    BA = float(parts[0])
                    print(BA)
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
        g.write(str(t)+" "+str(like)+" "+str(BA)+" "+str(Rand)+" "+str(Tri)+"\n")
    g.close()

df.to_csv("experiments/enron/Fits.csv", sep='\t')