import datetime as dt
from collections import defaultdict
import networkx as nx
import operator

papertimes = "data/cit-HepPh-dates.txt"
papers = "data/cit-HepPh.txt"
ordered = {}
seen = defaultdict(lambda: False)
hasdate = defaultdict(lambda: False)

newedgefile = "data/cit-HepPh-new.txt"

with open(papertimes,'r') as pt:
    for _, line in enumerate(pt):
        line = line.strip()
        id, date = line.split()
        id = int(id)
        y,m,d = map(int,date.split("-"))
        newdate = dt.date(y,m,d)
        unix = int((newdate - dt.date(1970, 1, 1)).total_seconds())
        ordered[id]= unix
        hasdate[id]= True
    pt.close()

G = nx.Graph()

with open(papers,'r') as pps:
    for _, line in enumerate(pps):
        line = line.strip()
        src, dst = map(int,line.split())
        G.add_edge(src,dst)
    pps.close()

Gnew = max(nx.connected_component_subgraphs(G), key=len)
print(len(Gnew.nodes()))

finaledgelist=[]

sorted_timelist = sorted(ordered.items(), key=operator.itemgetter(1))

while True:
    if len(sorted_timelist)==0:
        break
    # arbitrarily order the papers which were published on same day so they can be parsed as stars
    arrivals=[r for r in sorted_timelist if r[1]==sorted_timelist[0][1]]
    nexttime = arrivals[0][1]
    narrivals = len(arrivals)
    for c, row in enumerate(arrivals,0):
        src, time = row[0], row[1]+ c*round(86400/narrivals)
        if not Gnew.has_node(src):
            continue
        for node in Gnew.neighbors(src):
            if seen[node]:
                finaledgelist.append([src, node, time])
                continue
            if hasdate[node]:
                if ordered[node] > time:
                    continue
                else:
                    finaledgelist.append([src,node,time])
                    seen[node]=True
                    continue
            else:
                finaledgelist.append([src,node,time])
                seen[node]=True
    del sorted_timelist[:narrivals]
    print(len(sorted_timelist))


with open(newedgefile,'w') as newf:
    for edge in finaledgelist:
        newf.write(str(edge[0])+" "+str(edge[1])+" "+str(edge[2])+"\n")
    newf.close()