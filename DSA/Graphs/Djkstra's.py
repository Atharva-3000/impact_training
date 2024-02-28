#graph algos
# 1. Dijkstra algorithm - this algo is used to find the shortest path between source and destination or we can find the shortest distance between source and destination. In this algo we will take 2 list - first list will represent the visisted nodes and second list will represent the distances. If the node is not visited we have to consider as false. If the node is visited it will become true. For every node, we have to find adjacent nodes. Initially all the distances will be taken as infinity. After calculating the distances, this correspoding list wlil be updated.

def minDistance(V, dist, visited):
    min = 9999
    for v in range(V):
        if dist[v] < min and visited[v] == False:
            min = dist[v]
            min_index = v
    return min_index


def dijkstra(graph, V, src):
    dist = [9999]*V
    dist[src] = 0
    visited = [False]*V
    for count in range(V):
        u = minDistance(V, dist, visited)
        visited[u] = True
        for v in range(V):
            if(graph[u][v] > 0 and visited[v] == False and dist[v] > dist [u] + graph[u][v]):
                dist[v] = dist[u] + graph[u][v]
    print("vertex\tDistance from source")
    for node in range(V):
        print(node, "\t\t", dist[node])
        
        
n = int(input("Enter no of vertices: "))
print("Enter the adjscent matrix: ")
q = []
for i in range(n):
    data = list(map(int, input().split()))
    q.append(data)
s = int(input("Enter the source matrix: "))
dijkstra(q, n, s)