import os
import re
import numpy as np

file_grow = "experiments/BArankpref/BARankGrow.json"
grow_tmp = re.sub(".json","tmp.json",file_grow)
file_fit= "experiments/BArankpref/BARankFit.json"
fit_tmp = re.sub(".json","tmp.json",file_fit)
dump = "experiments/BArankpref/like.tmp"
results = "experiments/BArankpref/BARank10000results.dat"

numExperiments=10
betas = np.linspace(0.0,1.0,num=11)

with open(file_grow,'r') as fgrow:
    growdata = fgrow.read()

for ex in range(numExperiments):
    for beta in betas:
        beta = round(beta,1)
        tmp = re.sub("NAME","BARank-"+str(beta),growdata)
        tmp = re.sub("AAA",str(beta),tmp)
        tmp = re.sub("BBB",str(1-beta),tmp)
        with open(grow_tmp,'w') as f:
            f.write(tmp)
            f.close()
        os.system("java -jar feta3-1.0.0.jar "+grow_tmp)
        os.system("rm "+grow_tmp)

        with open(file_fit,'r') as ffit:
            fitdata = ffit.read()
        tmp = re.sub("NAME","BARank-"+str(beta),fitdata)
        with open(fit_tmp,'w') as f2:
            f2.write(tmp)
            f2.close()
        os.system("java -jar feta3-1.0.0.jar "+fit_tmp+" > "+dump)
        os.system("rm "+fit_tmp)

        with open(dump,'r') as like:
            fit = like.read().splitlines()
            betaguess = float(fit[1].strip().split(" ")[0])

        fres = open(re.sub("results","results"+str(beta),results), 'a+')
        fres.write(str(beta)+" "+str(betaguess)+"\n")
        fres.close()