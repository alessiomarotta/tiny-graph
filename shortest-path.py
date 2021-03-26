#!/usr/bin/env python

from graph import *

G = Graph(5, [(0, 1, 10), (0, 4, 5), (1, 2, 1), (1, 4, 2), (2, 3, 4), (3, 2, 6), (3, 0, 7), (4, 1, 3), (4, 2, 9), (4, 3, 2)])
d = G.key
w = G.w
Adj = G.adj

def Dijkstra(G, s):
    for u in G.V:
        d[u] = inf

    d[s] = 0

    S = []
    Q = VertexQueue(G)

    while not Q.isEmpty():
        u = Q.extractMin()
        S = S + [u]

        for v in Adj(u):
            d[v] = min(d[v], d[u] + w(u, v))

def Bellman_Ford(G, s):
    for u in G.V:
        d[u] = inf

    d[s] = 0

    for i in range(len(G.V) - 1):
        for (u, v) in G.E:
            d[v] = min(d[v], d[u] + w(u, v))

    for (u, v) in G.E:
        if d[v] > d[u] + w(u, v):
            return False

    return True

def printMatrix(M):
    for row in M:
        for n in row:
            print(str(n).ljust(3), end=' ')

        print()

def createMatrix(G):
    m = [[inf for v in G.V] for u in G.V]

    for i in G.V:
        for j in G.V:
            if i == j: m[i][j] = 0
            elif (i, j) in G.E: m[i][j] = w(i, j)

    return m

def Floyd_Warshall(G):
    W = createMatrix(G)
    D = [[[-inf for el in W] for row in W] for m in range(len(W) + 1)]

    n = len(W)
    D[0] = W

    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[k+1][i][j] = min(D[k][i][j], D[k][i][k] + D[k][k][j])

    return D
