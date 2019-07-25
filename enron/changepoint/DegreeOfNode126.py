import networkx as nx

enron = "enron.dat"

G=nx.Graph()
time1 = 1007425780-86400
time2 = time1 + 3*86400
count = 0

with open(enron,'r') as e:
    for line in e.read().splitlines():
        parts = line.split()
        if time2 > int(parts[2])> time1:
            if parts[1]=="126":
                count +=1;
        if int(parts[2]) > time2:
            break
        G.add_edge(parts[0], parts[1])

print(count)
print(G.degree("126"))