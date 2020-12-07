import sys
import os
import numpy as np
import json
#sys.path.insert(1, '/Users/naomiarnold/CODE/NaomiFETA/FETA3.1')
sys.path.insert(1, '/home/ubuntu/FETA3')
from feta import *

root = "experiments/citations/changepoint/"
tmp = root+"tmp.json"
start = 820800000
end = 1015956000

results_file = root+"noChangepoints4.json"
with open(results_file,'w') as f:
    f.write("{\"view\": [ ")
    f.close()

omcs = [{"ComponentName":"DegreeModelComponent"}, {"ComponentName":"RandomAttachment"}, {"ComponentName":"TriangleClosure"}]

fmm = FitMixedModel(start,end,1, debug=True)
act = Action(fmm)
data = DataObject("data/cit-HepPh-new.txt")

max_intervals = 5

for ni in range(4,max_intervals):
    intervals = np.linspace(start,end,num=ni+1)
    obm = []
    for i in range(ni):
        obm.append(ObjectModel(round(intervals[i]),round(intervals[i+1]),omcs))
    fm = FetaObject(data,act,obm)
    with open(tmp,'w') as f:
        fm = FetaEncoder().encode(fm)
        f.write(json.dumps(json.loads(fm), indent = 2))
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
