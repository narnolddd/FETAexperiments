import os
import re
import numpy as np
import matplotlib.pyplot as plt

file_grow = "experiments/degreepowerchange/DegreePowGrow.json"
grow_tmp = re.sub(".json","tmp.json",file_grow)
file_like= "experiments/degreepowerchange/DegreePowLike.json"
like_tmp = re.sub(".json","tmp.json",file_like)
dump = "experiments/degreepowerchange/like.tmp"
results = "experiments/degreepowerchange/degreepower1.2-1-1000results.dat"

growdata = ""
maxtime = 1000

# Generate bunch of networks with changepoints at different times
with open(file_grow,'r') as fgrow:
    growdata = fgrow.read()

times = range(100,1000,100)

for ex in range(10):
    for time in times:
        tmp = re.sub("NAME","DegreePow-1.2-1-"+str(time),growdata)
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

    plt.style.use('seaborn-darkgrid')
    palette = plt.get_cmap('Set1')

    num=0
    fres = open(re.sub("results","results"+str(ex),results),'w')
    for time in times:
        print(time)
        tmplike = re.sub("NAME","DegreePow-1.2-1-"+str(time),likedata)
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
        plt.plot(xpoints,curve,marker='', color=palette(num),linewidth=1, label="t="+str(time))
        num+=1
    fres.close()

plt.legend()
plt.title("Likelihoods of different changepoint times Degree Power 1.2 -> Degree Power 1.0")
plt.xlabel("Time")
plt.ylabel("C0 Likelihood")
plt.show()