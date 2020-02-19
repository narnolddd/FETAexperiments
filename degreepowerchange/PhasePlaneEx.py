import numpy as np
import re
import os

params = [str(round(x,1)) for x in np.linspace(0.0,2.0,num=21)]
experiments = 10

errors = np.array((len(params),len(params)))

growfile = "experiments/degreepowerchange/PhasePlaneGrow.json"
growdata = ""
growtmp = "experiments/degreepowerchange/PhasePlaneGrow.tmp"

likefile = "experiments/degreepowerchange/PhasePlaneLike.json"
likedata = ""
liketmp = "experiments/degreepowerchange/PhasePlaneLike.tmp"

MLEresults = "experiments/degreepowerchange/PhasePlaneMLEs10000-finegrained.txt"

dump = "experiments/degreepowerchange/dump.tmp"

MLES = {}
for p1 in params:
    for p2 in params:
        MLES[p1+"-"+p2]=[]

with open(growfile,'r') as f:
    growdata = f.read()
    f.close()

with open(likefile,'r') as g:
    likedata = g.read()
    g.close()

for ex in range(experiments):
    for p1 in params:
        for p2 in params:
            if float(p1)>=0.8 and float(p2)>=0.8:
                continue
            print(str(ex)+" "+p1+" "+p2)
            tmp1 = re.sub("NAME", "PP-100-"+p1+"-"+p2,growdata)
            tmp2 = re.sub("PARAM1",p1,tmp1)
            tmp3 = re.sub("PARAM2",p2,tmp2)
            with open(growtmp,'w') as f:
                f.write(tmp3)
                f.close()
            os.system("java -jar feta3-1.0.0.jar "+growtmp)
            os.system("rm "+growtmp)

            curve = np.zeros(100)
            curvefile = "experiments/degreepowerchange/LIKELIHOODS-"+p1+"-"+p2+".txt"

            for i in range(1,101):
                tmp1 = re.sub("NAME", "PP-100-"+p1+"-"+p2,likedata)
                tmp2 = re.sub("PARAM1",p1,tmp1)
                tmp3 = re.sub("PARAM2",p2,tmp2)
                tmp4 = re.sub("TTT",str(4500 + 10*i),tmp3)
                with open(liketmp,'w') as f:
                    f.write(tmp4)
                    f.close()
                os.system("java -jar feta3-1.0.0.jar "+liketmp+" > "+dump)
                os.system("rm "+liketmp)

                with open(dump,'r') as f:
                    curve[i-1]=float(f.read().strip())
                    f.close()

                os.system("rm "+dump)

            with open(curvefile,'a') as cf:
                for val in curve:
                    cf.write(str(val)+" ")
                cf.write("\n")
                cf.close()
            max = np.argmax(curve)+1
            MLES[p1+"-"+p2].append(max)


with open(MLEresults,'w') as f:
    for i in range(len(params)):
        for j in range(len(params)):
            f.write(params[i]+" "+params[j]+" "+",".join(list(map(str,MLES[params[i]+"-"+params[j]])))+'\n')
    f.close()