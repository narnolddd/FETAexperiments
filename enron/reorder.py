from operator import itemgetter
from collections import defaultdict
file = "out.enron"
file2 = "enron.dat"

data=[]

link_exists = defaultdict(lambda : False)

with open(file,'r') as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
        parts=line.strip().split()
        src, dst, time = parts[0].strip(), parts[1].strip(), int(parts[3].strip())
        if src == dst:
            continue
        data.append(dict(src=src,dst=dst,time=time))

reordered = sorted(data, key = itemgetter('time'))

with open(file2,'w') as f2:
    for line in reordered:
        src, dst = line['src'], line['dst']
        if link_exists[str([src,dst])] or link_exists[str([dst,src])]:
            continue
        link_exists[str([src,dst])]=True
        f2.write(line['src']+" "+line['dst']+" "+str(line['time'])+"\n")
    f2.close()