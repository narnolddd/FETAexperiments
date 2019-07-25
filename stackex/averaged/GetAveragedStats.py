import os
import re

experiments = 10

root = "experiments/stackex/averaged/"
suff = ".json"
models = ['BestMix', 'BA', 'Rand', 'TriInv25']

measurefile = ''

def grow(model, ex):
    tmp = root+"Grow_"+model+".tmp"
    print(tmp)
    fname = root+"Grow_"+model+suff
    with open(fname,'r') as f:
        growdata = f.read()
        f.close()
    growtmp = re.sub("EXPERIMENT", str(ex), growdata)
    with open(tmp,'w') as f:
        f.write(growtmp)
        f.close()
    os.system("java -jar feta3-1.0.0.jar "+tmp)

def measure(model, ex):
    tmp = root+"Measure"+model+".tmp"
    fname = root+"Measure"+suff

    with open(fname,'r') as f:
        measuredata = f.read()
        f.close()
    measuretmp = re.sub("GRAPHFILE", model+"_"+str(ex),measuredata)
    with open(tmp,'w') as f:
        f.write(measuretmp)
        f.close()
    os.system("java -jar feta3-1.0.0.jar "+tmp)

for ex in range(experiments):
    for model in models:
        grow(model,ex)
        measure(model,ex)