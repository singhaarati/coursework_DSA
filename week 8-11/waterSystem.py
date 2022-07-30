# from turtle import color
import networkx as nx
import matplotlib.pyplot as plt
import json

G = nx.DiGraph()


def addNewHouse(house_num, update=True):
    G.add_node(house_num)
    if update:
        appData["nodes"].append(house_num)
        with open(r"C:\Users\Arti\OneDrive\Desktop\project\CourseWork\week 8-11\appData.json", "w") as jsonFile:
            json.dump(appData, jsonFile)


def removeHouse(house_num, update=True):
    G.remove_node(house_num)
    if update:
        appData["nodes"].remove(house_num)
        with open(r"C:\Users\Arti\OneDrive\Desktop\project\CourseWork\week 8-11\appData.json", "w") as jsonFile:
            json.dump(appData, jsonFile)


def addPipeConnection(house1, house2, update=True):
    G.add_edge(house1, house2, weight=1)
    if checkCycle():
        G.remove_edge(house1, house2)
        return False
    if update:
        appData["edges"].append([house1, house2])
        with open(r"C:\Users\Arti\OneDrive\Desktop\project\CourseWork\week 8-11\appData.json", "w") as jsonFile:
            json.dump(appData, jsonFile)
    return True


def displayPipeSystem(plotShortestPath=False, src=0, dest=0):
    printNodes()
    plt.clf()
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color="teal")
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), alpha=0.4)

    if plotShortestPath:
        path = nx.shortest_path(G, source=src, target=dest)
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='r')
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                               edge_color='r', width=5)

    plt.show()


def printNodes():
    for eachNode in G.nodes:
        print(f"House {eachNode}: ", end="")
        for each in nx.all_neighbors(G, eachNode):
            print(each, end=" ")
        print()


def vulnerable_house(house):
    neighbours = list(G.neighbors(house))
    for each in nx.all_neighbors(G, house):
        if each not in neighbours:
            for i in neighbours:
                addPipeConnection(each, i, True)
    removeHouse(house)


def checkCycle():
    try:
        nx.find_cycle(G, orientation="original")
        return True
    except:
        return False


def reset():
    with open(r"C:\Users\Arti\OneDrive\Desktop\project\CourseWork\week 8-11\appData.json", "w") as jsonFile:
        json.dump({"nodes": [], "edges": []}, jsonFile)


f = open(r"C:\Users\Arti\OneDrive\Desktop\project\CourseWork\week 8-11\appData.json")
appData = json.load(f)

for node in appData["nodes"]:
    addNewHouse(node, update=False)

for edge in appData["edges"]:
    addPipeConnection(edge[0], edge[1], update=False)
f.close()
