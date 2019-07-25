import networkx as nx
import csv

G = nx.Graph()

with open("facebook.dat",'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = " ")
    line_count = 0

    for row in csv_reader:
        time = int(row[2])
        node1, node2 = row[0], row[1]
        G.add_edge(node1,node2)

print(nx.degree_assortativity_coefficient(G))