import sys
import os
import numpy as np
sys.path.insert(1, '/home/ubuntu/FETA3')
from feta import *

root = "experiments/facebook/changepoint/"
tmp = root+"tmp.json"
start = 1165073426
end = 1232593783

results_file = root+"noChangepoints2.json"
with open(results_file,'w') as f:
    f.write("{\"view\": [ ")
    f.close()

omcs = [{"ComponentName":"DegreeModelComponent"}, {"ComponentName":"RandomAttachment"}, {"ComponentName":"TriangleClosure"}]

fmm = FitMixedModel(start,end,1)
act = Action(fmm)
data = DataObject("experiments/facebook/facebook.dat")

max_intervals = 20
for ni in range(1,max_intervals):
    intervals = np.linspace(start,end,num=ni+1)
    obm = []
    for i in range(ni):
        obm.append(ObjectModel(round(intervals[i]),round(intervals[i+1]),omcs))
    fm = FetaObject(data,act,obm)
    with open(tmp,'w') as f:
        f.write(FetaEncoder().encode(fm))
        f.close()
    os.system("java -jar feta3-1.0.0.jar "+tmp+" >> "+results_file)
    with open(results_file,'a') as f:
        if ni != max_intervals-1:
            f.write(',')
        else:
            f.write(']')
        f.close()

with open(results_file,'a') as f:
    f.write("}")
    f.close()
