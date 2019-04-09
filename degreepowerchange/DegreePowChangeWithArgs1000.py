import os
import re
import numpy as np
import sys

param1 = str(sys.argv[1])
param2 = str(sys.argv[2])
print(param1+" "+param2)


growtemplate = "experiments/degreepowerchange/DegPowGrowTemplate1000.json"
liketemplate = "experiments/degreepowerchange/DegPowLikeTemplate1000.json"
file_grow = "experiments/degreepowerchange/DegreePowGrow1000"+param1+"-"+param2+".json"
grow_tmp = re.sub(".json","tmp.json",file_grow)
file_like= "experiments/degreepowerchange/DegreePowLike1000"+param1+"-"+param2+".json"
like_tmp = re.sub(".json","tmp.json",file_like)
dump = "experiments/degreepowerchange/like1000"+param1+"-"+param2+".json"
results = "experiments/degreepowerchange/degreepower"+param1+"-"+param2+"-1000results.dat"

growdata = ""

with open(growtemplate,'r') as g:
    grow = g.read()
    g.close()

with open(liketemplate,'r') as l:
    like = l.read()
    l.close()

stuff1 = re.sub("PARAM1",param1, grow)
stuff1 = re.sub("PARAM2",param2,stuff1)
stuff2 = re.sub("PARAM1",param1,like)
stuff2 = re.sub("PARAM2",param2,stuff2)

with open(file_grow,'w') as f1:
    f1.write(stuff1)
    f1.close()

with open(file_like,'w') as f2:
    f2.write(stuff2)
    f2.close()

# Generate bunch of networks with changepoints at different times
with open(file_grow,'r') as fgrow:
    growdata = fgrow.read()

times = range(100,1100,100)

for ex in range(10):
    for time in times:
        tmp = re.sub("NAME","DegreePow1000-"+param1+"-"+param2+"-"+str(time),growdata)
        tmp = re.sub("TTT",str(time),tmp)
        with open(grow_tmp,'w') as f:
            f.write(tmp)
            f.close()
        os.system("java -jar feta3-1.0.0.jar "+grow_tmp)

    os.system("rm "+grow_tmp)

    with open(file_like,'r') as flike:
        likedata= flike.read()

    likelihood_curves=[]
    xpoints = range(10,1010,10)
    estimate = np.zeros(len(times))

    num=0
    fres = open(re.sub("results","results"+str(ex),results),'w')
    for time in times:
        print(time)
        tmplike = re.sub("NAME","DegreePow1000-"+param1+"-"+param2+"-"+str(time),likedata)
        curve = np.zeros(100)
        for i in range(1,101):
            tmplike2 = re.sub("TTT",str(10*i),tmplike)
            with open(like_tmp,'w') as f:
                f.write(tmplike2)
                f.close()
            os.system("java -jar feta3-1.0.0.jar "+like_tmp+" > "+dump)
            with open(dump,'r') as f:
                curve[i-1]=float(f.read().strip())
        estimate[num]=max(curve)
        likelihood_curves.append(curve)
        print(curve)
        fres.write(np.array2string(curve,precision=5,separator=" "))
        num+=1
    fres.close()