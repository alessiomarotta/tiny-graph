#!/usr/bin/env python

from math import *

class Graph:
    V = []
    E = []
    key = []

    # vertices is the number of vertices of the graph
    # edges is a list of edges in the format (src, dst, weight)
    def __init__(self, vertices, edges):
        self.wl = [w for (u, v, w) in edges]

        self.V = list(range(vertices))
        self.E = [(u, v) for (u, v, w) in edges]
        self.key = [0 for v in range(vertices)]

    # returns the weight associated with the edge (u, v)
    def w(self, u, v):
        if (u, v) in self.E:
            return self.wl[self.E.index((u, v))]

        else:
            return inf

    # returns a list with the vertices adjacent to x
    def adj(self, x):
        return [v for (u, v) in self.E if u == x]


class VertexQueue:
    def __init__(self, g):
        self.queue = [e for e in zip(g.V, g.key)]
        self.graph = g

    def updateQueue(self):
        for (v, k) in self.queue:
            i = self.queue.index((v, k))
            self.queue[i] = v, self.graph.key[v]

    def extractMin(self):
        self.updateQueue()

        e = min(self.queue, key=lambda t: t[1])
        self.queue.remove(e)
        
        return e[0]

    def isEmpty(self):
        return self.queue == []
