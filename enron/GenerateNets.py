import warnings
warnings.filterwarnings("ignore")
import sys
import json
import pandas as pd
#sys.path.insert(1, '/Users/naomiarnold/CODE/NaomiFETA/FETA3.1')
sys.path.insert(1, '/home/ubuntu/FETA3')
import numpy as np
import os
from feta import *

cps = int(sys.argv[1])
root = "experiments/enron/"
start = 896283060
end = 1024089329
experiments = 10

grow = root+"grow-"+str(cps)+".json"
measure = root+"measure-"+str(cps)+".json"

graphname = root+"graphfiles/EN_GRAPH_"+str(cps)+".dat"

for j in range(experiments):
    model_array = []
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
            comps.append(ObjectModelComponent(name_to_model[list(comp.keys())[0]],list(comp.values())[0]))
        model_array.append(ObjectModel(modelstart,modelend,comps))

    act = Grow(start,end,1)
    act = Action(grow=act)
    operation = OperationModel("Clone", start, root+"enron.feta")
    data = DataObject(infile=root+"enron.dat",outfile=graphname)
    fm = FetaObject(data,act,model_array,operation)
    fm = FetaEncoder().encode(fm)

    with open(grow,'w') as f:
        f.write(json.dumps(json.loads(fm), indent = 2))
        f.close()

    os.system("java -jar feta3-1.0.0.jar "+grow)

    meas = Measure(start,end,interval=604800,fname=root+"averaged/Best"+str(cps)+"-"+str(j)+".dat")
    data = DataObject(infile=graphname)
    act = Action(measure=meas)
    fm = FetaObject(data,act)
    fm = FetaEncoder().encode(fm)

    with open(measure,'w') as f:
        f.write(json.dumps(json.loads(fm), indent = 2))
        f.close()

    os.system("java -jar feta3-1.0.0.jar "+measure)
    os.system("rm "+graphname)
