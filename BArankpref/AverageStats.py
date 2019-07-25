import numpy as np
BAstats = "BA10000stats.dat"
RPstats = "RP10000stats.dat"



for file in [BAstats, RPstats]:
    maxdeg = []
    cc = []
    meandegsq = []
    assort = []
    with open(file,'r') as f:
        for line in f.readlines():
            parts = line.split()
            maxdeg.append(float(parts[5]))
            cc.append(float(parts[6]))
            meandegsq.append(float(parts[7]))
            assort.append(float(parts[8]))

    print(str(np.mean(maxdeg))+" "+str(np.std(maxdeg)))
    print(str(np.mean(cc))+" "+str(np.std(cc)))
    print(str(np.mean(meandegsq))+" "+str(np.std(meandegsq)))
    print(str(np.mean(assort))+" "+str(np.std(assort)))


BAgammas = [3.05389514413736, \
            2.961057482239264, \
            3.011289537059016, \
            2.9966100688865573, \
            3.0234240726300703, \
            3.06270974228527, \
            3.0687392589755516, \
            3.0903080829190555, \
            3.179602603228184, \
            3.175947987344969]

RPgammas = [3.233190573749609, \
            3.244511062753258, \
            3.263519395494756, \
            3.1909192869879544, \
            3.1790294457750186, \
            3.148107925484534, \
            3.22724539952993, \
            3.205405769315174, \
            3.2103548174474112, \
            3.1865493246091035]

print(np.mean(BAgammas))
print(np.std(BAgammas))
print(np.mean(RPgammas))
print(np.std(RPgammas))