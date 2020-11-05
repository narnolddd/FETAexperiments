import warnings
warnings.filterwarnings("ignore")
import sys
import json
import pandas as pd
sys.path.insert(1, '/Users/naomiarnold/CODE/NaomiFETA/FETA3.1')
import numpy as np
import os
from feta import *

root = "experiments/citations/"
grow = root+"grow.json"
measure = root+"measure.json"
start = 747411840
end = 1015956000
model_array = []
cps = int(sys.argv[1])
experiments = 10

graphname = root+"averaged/CIT_GRAPH_"+str(cps)+".dat"

for j in range(experiments):
    print(j)

    with open(root+"changepoint/noChangepoints.json",'r') as f:
        data = json.load(f)
        x = pd.DataFrame(data['view'])
        obm = x.iloc[cps]['intervals']
        f.close()

    times = np.linspace(start,end,num = cps + 2)

    for i, interval in enumerate(obm):
        comps = []
        modelstart = round(times[i])
        modelend = round(times[i+1])
        if i == cps:
            modelend+=1000
        for comp in interval['models']:
            comps.append(ObjectModelComponent(list(comp.keys())[0],list(comp.values())[0]))
        model_array.append(ObjectModel(modelstart,modelend,comps))

    act = Grow(start,end,)
    act = Action(grow=act)
    operation = OperationModel("Clone", start, root+"OpModel.feta")
    data = DataObject(infile="data/cit-HepPh-new.txt",outfile=graphname)
    fm = FetaObject(data,act,model_array,operation)
    fm = FetaEncoder().encode(fm)

    with open(grow,'w') as f:
        f.write(json.dumps(json.loads(fm), indent = 2))
        f.close()

    os.system("java -jar feta3-1.0.0.jar "+grow)

    meas = Measure(start,end,interval=86400,fname=root+"averaged/Best"+str(cps)+"-"+str(j)+".dat")
    data = DataObject(infile=graphname)
    act = Action(measure=meas)
    fm = FetaObject(data,act)
    fm = FetaEncoder().encode(fm)

    with open(measure,'w') as f:
        f.write(json.dumps(json.loads(fm), indent = 2))
        f.close()

    os.system("java -jar feta3-1.0.0.jar "+measure)
    os.system("rm "+graphname)