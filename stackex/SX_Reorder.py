import operator

file = "experiments/stackex/sx_no_dup.txt"
new = "experiments/stackex/sx_reordered.txt"

edgelist=[]

with open(file,'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        parts = line.strip().split()
        edgelist.append(dict(src=parts[0],dst=parts[1],unix=int(parts[2].strip())))
    f.close()

ordered = sorted(edgelist,key=operator.itemgetter('unix'))

with open(new,'w') as f:
    for edge in ordered:
        f.write(edge['src']+" "+edge['dst']+" "+str(edge['unix'])+"\n")
    f.close()