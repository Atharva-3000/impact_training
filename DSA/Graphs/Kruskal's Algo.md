# Kruskal's Algorithm

1. It is used to find minimum spanning tree.

2. Arrange all edges in ascending order based on the cost.

3. Consider least cost weighted edge and include it in the tree, and if the edge forms a cycle just ignore and consider next least cost weighted edge.

4. Repeat `step 2` in such a way that, all vertices are included in the tree, finally you should have *n* vertices and *(n-1)* edges.