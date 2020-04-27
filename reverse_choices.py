import sys

file = sys.argv[1]
new_file = sys.argv[2]

with open(file,'r') as f:
    lines = f.readlines()
    f.close()

new_lines = []
start = 997747200
currTime = 1
edgeset=[]

for line in lines:
    n1, n2, time = line.split()
    time= int(time)
    if time > currTime:
        if (time <= start):
            new_lines.append(n1+" "+n2+" "+str(time))
            continue
        while len(edgeset)>0:
            new_lines.append(edgeset.pop(-1))
        edgeset=[]
        currTime= time
    edgeset.append(n1+" "+n2+" "+str(time))

with open(new_file,'w') as f:
    for line in new_lines:
        f.write("%s\n" % line)
    f.close()