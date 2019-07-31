import numpy as np
BAstats10000 = "BA10000stats.dat"
RPstats10000 = "RP10000stats.dat"
BAstats1000 = "BA1000stats.dat"
RPstats1000 = "RP1000stats.dat"



for file in [BAstats1000, RPstats1000]:
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

BAgammas1000 = [3.1123800768653913, \
                3.095087978001225, \
                3.160539649542988, \
                3.040319118958632, \
                3.2348597883839036, \
                3.048412976237543, \
                3.142491907826638, \
                3.111203330231423, \
                3.1835266001072378, \
                3.185000045774284]

RPgammas1000 = [3.24599950590404, \
                 3.251608994673376, \
                 3.2781568388766362, \
                 3.370054713203093, \
                 3.214674752342548, \
                 3.566998392803999, \
                 3.573539351619294, \
                 3.214892638535086, \
                 3.2581912933365724, \
                 3.4606165852120054]

BAgammas10000 = [3.05389514413736, \
            2.961057482239264, \
            3.011289537059016, \
            2.9966100688865573, \
            3.0234240726300703, \
            3.06270974228527, \
            3.0687392589755516, \
            3.0903080829190555, \
            3.179602603228184, \
            3.175947987344969]

RPgammas10000 = [3.233190573749609, \
            3.244511062753258, \
            3.263519395494756, \
            3.1909192869879544, \
            3.1790294457750186, \
            3.148107925484534, \
            3.22724539952993, \
            3.205405769315174, \
            3.2103548174474112, \
            3.1865493246091035]

print(np.mean(BAgammas1000))
print(np.std(BAgammas1000))
print(np.mean(RPgammas1000))
print(np.std(RPgammas1000))