def add_node(v1):
    global nc
    if v1 in nodes:
        print("Node already exists")
    else:
        nc += 1
        nodes.append(v1)
        for i in graph:
            i.append(0)
        temp = []
        for i in range(0, nc):
            temp.append(0)
        graph.append(temp)

# def add_edge(v1, v2):
#     if v1 not in nodes:
#         print(v1, " Node does not exist")
#     elif v2 not in nodes:
#         print(v2, " Node does not exist")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = 1
#         graph[index2][index1] = 1

#Weighted
# def add_edge(v1, v2, w):
#     if v1 not in nodes:
#         print(v1, " Node does not exist")
#     elif v2 not in nodes:
#         print(v2, " Node does not exist")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = w
#         graph[index2][index1] = w
        
#directed weighted
def add_edge(v1, v2, w):
    if v1 not in nodes:
        print(v1, " Node does not exist")
    elif v2 not in nodes:
        print(v2, " Node does not exist")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = w

def print_graph():
    for i in range(nc):
        for j in range(nc):
            print(graph[i][j], end = " ")
        print()
        
def delete_node(v1):
    if v1 not in nodes:
        print(v1, " Node does not exist")
    else:
        index1 = nodes.index(v1)
        nodes.remove(v1)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)
        global nc
        nc -= 1
        
def bfs(v1):
    visited = [False] * nc
    queue = []
    queue.append(v1)
    visited[nodes.index(v1)] = True
    while queue:
        v1 = queue.pop(0)
        print(v1, end = " ")
        index1 = nodes.index(v1)
        for i in range(nc):
            if graph[index1][i] == 1 and visited[i] == False:
                queue.append(nodes[i])
                visited[i] = True

# dfs using recursion
def dfs(v1, visited):
    visited[nodes.index(v1)] = True
    print(v1, end = " ")
    index1 = nodes.index(v1)
    for i in range(nc):
        if graph[index1][i] == 1 and visited[i] == False:
            dfs(nodes[i], visited)
    
# dfs of indirected graph using recursion
def dfsIndirected(v1, visited):
    visited[nodes.index(v1)] = True
    print(v1, end = " ")
    index1 = nodes.index(v1)
    for i in range(nc):
        if graph[index1][i] == 1 and visited[i] == False:
            dfs(nodes[i], visited)

nodes = []
graph = []
nc = 0
print("Before Adding:")
print(nodes)
print(graph)
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_edge('A', 'B', 5)
add_edge('A', 'C', 4)
add_edge('A', 'D', 3)
add_edge('B', 'D', 2)
add_edge('C', 'D', 1)
add_edge('B', 'E', 6)
add_edge('D', 'E', 7)
print("After Adding:")
print(nodes)
print(graph)
print_graph()
delete_node('C')
print("After Deleting:")
print(nodes)
print(graph)
print_graph()
bfs('B')
print()
dfs('B', [False] * nc)
print()
in