#!/usr/bin/env python
# coding: utf-8

from abc import ABC


class FordFulkersonAlgorithm(ABC):

    """
        Abstract Class to Solve Ford-Fulkerson Algorithm

        Attributes:
            graph ([Int]) : adjency matrix
            source_node (int) : Start node
            sink_node (int) : target node 
            n (int) : number of node in graph
            visited_token (int) : indicator to know last time a node was visited 
            visited [int] : list with the node visited (0 if never visited by default)
            max_flow (method) : launch the algorithm
    
    """


    def __init__(self, graph, source_node, sink_node, n):
        self.graph = graph 
        self.source_node = source_node  
        self.sink_node = sink_node
        self.n = n
        self.visited_token = 1
        self.visited = [0] * self.n


    def max_flow(self):

        """
            Ford-Fulkerson Algorithm 
        
        """
        
        max_flow = 0
        while True:

            flow = self.dfs(self.source_node, self.sink_node, float('Inf'))
            self.visited_token += 1

            if flow == 0:  
                return max_flow

            max_flow += flow

