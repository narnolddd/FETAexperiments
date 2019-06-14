import os
import numpy as np
import re
import powerlaw
import itertools

experiments=10

root="experiments/BArankpref/"

RPstats=root+"RP10000stats.dat"
RPGammas=root+"RP10000gammas.dat"
BAstats=root+"BA10000stats.dat"
BAGammas=root+"BA10000gammas.dat"

grow=root+"Grow.json"
growtmp=root+"Grow.tmp"
growtxt=""

measure=root+"Measure.json"
measuretmp=root+"Measure.tmp"
measuretxt=""

with open(grow,'r') as f:
    growtxt=f.read()
    f.close()

with open(measure,'r') as f:
    measuretxt=f.read()
    f.close()

# Do BA ones
tmp1 = re.sub("NAME", "BA", growtxt)
tmp2 = re.sub("AAA", "1.0", tmp1)
tmp3 = re.sub("BBB", "0.0", tmp2)
with open(growtmp,'w') as f:
    f.write(tmp3)
    f.close()

tmp1 = re.sub("NAME", "BA", measuretxt)
with open(measuretmp, 'w') as f:
    f.write(tmp1)
    f.close()

for ex in range(experiments):
    print("BA "+str(ex))
    os.system("java -jar feta3-1.0.0.jar "+growtmp)
    os.system("java -jar feta3-1.0.0.jar "+measuretmp)

    with open(root+"BA10000Measurements.dat",'r') as f:
        stats = f.read().splitlines()[-1]
        with open(BAstats,'a+') as g:
            g.write(stats+"\n")
            g.close()
        f.close()
    with open(root+"BA10000MeasurementsDeg.dat",'r') as f:
        frequencies = [int(a) for a in f.read().splitlines()[-1].split()]
        degdist = list(itertools.chain.from_iterable([[i] * frequencies[i] for i in range(len(frequencies))]))
        results=powerlaw.Fit(degdist)
        with open(BAGammas,'a+') as g:
            g.write(str(results.power_law.alpha)+"\n")
            g.close()
        f.close()

# Do RP ones
tmp1 = re.sub("NAME", "RP", growtxt)
tmp2 = re.sub("AAA", "0.0", tmp1)
tmp3 = re.sub("BBB", "1.0", tmp2)
with open(growtmp,'w') as f:
    f.write(tmp3)
    f.close()

tmp1 = re.sub("NAME", "RP", measuretxt)
with open(measuretmp, 'w') as f:
    f.write(tmp1)
    f.close()

for ex in range(experiments):
    print("RP "+str(ex))
    os.system("java -jar feta3-1.0.0.jar "+growtmp)
    os.system("java -jar feta3-1.0.0.jar "+measuretmp)

    with open(root+"RP10000Measurements.dat",'r') as f:
        stats = f.read().splitlines()[-1]
        with open(RPstats,'a+') as g:
            g.write(stats+"\n")
            g.close()
        f.close()
    with open(root+"RP10000MeasurementsDeg.dat",'r') as f:
        frequencies = [int(a) for a in f.read().splitlines()[-1].split()]
        degdist = list(itertools.chain.from_iterable([[i] * frequencies[i] for i in range(len(frequencies))]))
        results=powerlaw.Fit(degdist)
        with open(RPGammas,'a+') as g:
            g.write(str(results.power_law.alpha)+"\n")
            g.close()
        f.close()