import numpy as np

enron = "enron.dat"

tA = 997747200
tB = 1024099200

times = [int(np.round(t)) for t in np.linspace(tA, tB, 11)]
index = 0
count = 0

with open(enron,'r') as e:
    for line in e.read().splitlines():
        time = int(line.split()[2])
        if time < tA:
            continue
        if time>times[index+1]:
            print(count)
            count=0
            index+=1
            if index>10:
                break
        count +=1



print(count)
print(G.degree("126"))