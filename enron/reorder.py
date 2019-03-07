from operator import itemgetter
file = "out.enron"
file2 = "enron.dat"

data=[]

with open(file,'r') as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
        parts=line.strip().split()
        data.append(dict(src=parts[0].strip(),dst=parts[1].strip(),time=int(parts[3].strip())))

reordered = sorted(data, key = itemgetter('time'))

with open(file2,'w') as f2:
    for line in reordered:
        f2.write(line['src']+" "+line['dst']+" "+str(line['time'])+"\n")
    f2.close()