from collections import defaultdict


def minCostConnectPoints(points):
    distance = [float('inf')]*(len(points))
    distance[0] = 0

    #graph creating
    graph = defaultdict(list)
    for i in range(len(points)):
        for j in range(len(points)):

            # for avoiding loops
            if i == j:
                continue
            x1, x2 = points[i][0], points[j][0]
            y1, y2 = points[i][1], points[j][1]
            graph[i].append([j, abs(x1-x2)+abs(y1-y2)])

    visited = set()

    def findMin():
        mini = -1
        minimum = float('inf')
        for i in range(len(points)):
            if distance[i] < minimum and i not in visited:
                minimum = distance[i]
                mini = i
        return mini

    for i in range(len(points)):

        # findMin returns the vertex that has least distance (i.e., distance[vertex] is least compare to others) and not visited
        v = findMin()
        visited.add(v)

        # neighbors checking
        for nei, edge in graph[v]:

            # prims -> if dist[nei] > edgeWeight then update dist[nei]
            if nei not in visited and distance[nei] > edge:
                distance[nei] = edge

    # returning total cost of spanning tree
    return sum(distance)


print(minCostConnectPoints([[0, 0], [2, 2], [3, 10], [4, 4], [5, 2], [7, 0]]))
