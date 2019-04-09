import os
import re
import numpy as np

file_grow = "experiments/degreepowerchange/DegreePowGrow0.9-1.json"
grow_tmp = re.sub(".json","tmp.json",file_grow)
file_like= "experiments/degreepowerchange/DegreePowLike0.9-1.json"
like_tmp = re.sub(".json","tmp.json",file_like)
dump = "experiments/degreepowerchange/like0.9-1.tmp"
results = "experiments/degreepowerchange/degreepower0.9-1-10000results.dat"

growdata = ""

# Generate bunch of networks with changepoints at different times
with open(file_grow,'r') as fgrow:
    growdata = fgrow.read()

times = range(9000,10000,100)

for ex in range(10):
    for time in times:
        tmp = re.sub("NAME","DegreePow-0.9-1-"+str(time),growdata)
        tmp = re.sub("TTT",str(time),tmp)
        with open(grow_tmp,'w') as f:
            f.write(tmp)
            f.close()
        os.system("java -jar feta3-1.0.0.jar "+grow_tmp)

    os.system("rm "+grow_tmp)

    with open(file_like,'r') as flike:
        likedata= flike.read()

    likelihood_curves=[]
    xpoints = range(9010,10010,10)
    estimate = np.zeros(len(times))

    num=0
    fres = open(re.sub("results","results"+str(ex),results),'w')
    for time in times:
        print(time)
        tmplike = re.sub("NAME","DegreePow-0.9-1-"+str(time),likedata)
        curve = np.zeros(100)
        for i in range(1,101):
            tmplike2 = re.sub("TTT",str(9000+10*i),tmplike)
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