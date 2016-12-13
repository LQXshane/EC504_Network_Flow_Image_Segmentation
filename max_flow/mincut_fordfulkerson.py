# Python 2.7
# Min-cut using Ford-Fulkerson Algorithm
# returns the edges that are from one segment to another in the graph
# and the total values of flows along the max-flow path

# from IPython import embed
# import pandas as pd
# V = 6  # Number of vertices in a graph
# # Define a graph and a residual graph
# # The graph is stored as a matrix
# # values in the matrix are actual flow from one node to another
# graph = [[0 for col in range(V)] for row in range(V)]
# # rgraph = [[0 for col in range(V)] for row in range(V)]
# graph = [
#          [0, 16,13,0, 0, 0 ],
#          [0, 0, 10,12,0, 0 ],
#          [0, 4, 0, 0, 14,0 ],
#          [0, 0, 9, 0, 0, 20],
#          [0, 0, 0, 7, 0, 4 ],
#          [0, 0, 0, 0, 0, 0 ]
#                             ]
# src = 0  # source node
# sink = 5  # sink node
# # embed()
import pandas as pd
import numpy as np
# BFS: returns true if there is a path from source 's' to sink 't'
# in the residual graph
def bfs(rgraph, s, t, parent, V):
    # global V
    visited = [False for i in range(V)]  # create a list to store visited nodes
    visited[s] = True  # mark source node as visited
    parent[s] = -1  # mark parent of s as NIL(-1)
    q = list()  # create an empty queue
    q.insert(0, s)  # push source into the queue

    while len(q) != 0:  # while queue is not empty
        current = q.pop()  # pop from q, give its value to current node
        for adjacent in range(V):  # for each node that is adjacent to current
            # if this node is not visited and it's in the residual graph
            if not visited[adjacent] and rgraph[current][adjacent] > 0:
                q.insert(0, adjacent)  # push this node into the queue
                parent[adjacent] = current  # mark its parent as the current node
                visited[adjacent] = True  # mark the node as visited
    return visited[t]  # return whether sink node is visited


# BFS2: returns the visited nodes if there is a path from source 's' to sink 't'
# in the residual graph
def bfs2(rgraph, s, parent, V):
    # global V
    visited = [False for i in range(V)]  # create a list to store visited nodes
    visited[s] = True  # mark source node as visited
    parent[s] = -1  # mark parent of s as NIL(-1)
    q = list()  # create an empty queue
    q.insert(0, s)  # push source into the queue

    while len(q) != 0:  # while queue is not empty
        current = q.pop()  # pop from q, give its value to current node
        for adjacent in range(V):  # for each node that is adjacent to current
            # if this node is not visited and it's in the residual graph
            if not visited[adjacent] and rgraph[current][adjacent] > 0:
                q.insert(0, adjacent)  # push this node into the queue
                parent[adjacent] = current  # mark its parent as the current node
                visited[adjacent] = True  # mark the node as visited
    return visited  # return the nodes that are visited


# Doing min-cut using Ford-Fulkerson Algorithm,
# and print the edges that are from one segment to another in the graph
def mincut(graph, s, t, V):
    # global V
    rgraph = [[0 for col in range(V)] for row in range(V)]  # initially, f(e)=0 for all edges
    total_flow = 0  # initialize the total flow
    # initialize the residual graph, and let it be the same as the original graph
    for i in range(V):
        for j in range(V):
            rgraph[i][j] = graph[i][j]

    parent = [0 for i in range(V)]
    while bfs(rgraph, s, t, parent, V):  # while there is a s-t path

        # get bottleneck
        flow = float("inf")  # initialize the flow of a path
        v = t  # let v be the node along a simple s-t path, initialize it to sink
        while v != s:  # update the minimum value along the path
            u = parent[v]
            flow = min(flow, rgraph[u][v])
            v = parent[v]
        bottleneck = flow

        # run augument
        v = t
        while v != s:  # for each node in the path
            u = parent[v]
            # update the residual graph
            rgraph[v][u] += bottleneck  # if e is a forward node,  f(e) <- f(e)+b
            rgraph[u][v] -= bottleneck  # if e is a backward node, f(e) <- f(e)-b
            v = parent[v]

        total_flow += bottleneck  # get the total values of flows

    # get all nodes that are visited
    parent = [0 for i in range(V)]
    visited = bfs2(rgraph, s, parent, V)

    # print the edges that are from one segment to another in the graph
    # for i in range(V):
    #     for j in range(V):
    #         if visited[i] and not visited[j] and graph[i][j]:
    #             print "%d - %d" % (i, j)
    print "The total values of flows is: %d" % total_flow
    return visited


# # test
# vis_node = mincut(graph, src, sink,V)