#!/usr/bin/env python
# coding: utf-8

# In[38]:


from abc import ABC
from collections import defaultdict
import time

class Perfo:

    def timeExecution(functionCalled, *args):

        start_time = time.time()
        functionCalled(args)
        elapsed_time = start_time - time.time()
        print (f'Time elapsed : {elapsed_time}')
    
class Edge:

    """
        Define Edge of Graph

        Attributes:
            to(int) : source node of th edge
            capacity(int) : flow maximum of the edge
            flow(int) : current flow (default zero)
            residual(int) : flow available to reversed an edge

    """

    def __init__(self, to, capacity):

        self.to = to               
        self.capacity = capacity  
        self.flow = 0              
        self.residual = None       

    def latest_capacity(self):
        return self.capacity - self.flow

    def augment(self, min_flow):
        self.flow += min_flow
        self.residual.flow -= min_flow
    

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


        



    
class FordFulkersonList(FordFulkersonAlgorithm):


    def __init__(self, graph, source_node, sink_node, n):
        super().__init__(graph, source_node, sink_node, n)
        

    def add_edge(self, from_node, to_node, capacity):

        """
        Add edge into graph for the algorithm

        Params:
            from_node (int): start node of the edge
            to_node (int): end node of the edge 
            capacity (int): edge capacity

        """

        forward_edge = Edge(to_node, capacity)
        backward_edge = Edge(from_node, 0)

        forward_edge.residual = backward_edge
        backward_edge.residual = forward_edge

        self.graph[from_node].append(forward_edge)
        self.graph[to_node].append(backward_edge)


    def dfs(self, node, sink, flow):

        """
            Depth First Search

            Params:
                node (int) : source node
                sink(int) : target node
                flow (int) : flow available

            Returns:
                flow(int) : flow found
        
        """

        if node == sink:
            return flow

        self.visited[node] = self.visited_token

        
        for edge in self.graph[node]:
            if self.visited[edge.to] != self.visited_token and edge.latest_capacity() > 0:

                min_flow = min(flow, edge.latest_capacity())
                dfs_flow = self.dfs(edge.to, sink, min_flow)

                if dfs_flow > 0:
                    edge.augment(dfs_flow)
                    return dfs_flow

        return 0



class FordFulkersonMatrix(FordFulkersonAlgorithm):

    """
        Solve Ford-Fulkerson Algorithm

    
    """

    def __init__(self, graph, source_node, sink_node, n):
        super().__init__(graph, source_node, sink_node, n)


    def dfs(self, node, sink, flow):

        """
            Depth First Search

            Params:
                node (int) : source node
                sink(int) : target node
                flow (int) : flow available

            Returns:
                flow(int) : flow found
        
        """
        
        if node == sink:
            return flow
        
        self.visited[node] = self.visited_token

        for i in range(self.n):

            if self.visited[i] != self.visited_token and  self.graph[node][i] > 0:

                min_flow = min(flow, self.graph[node][i]) 
                dfs_flow = self.dfs(i, sink, min_flow)

                if dfs_flow:
                    self.graph[node][i] -= dfs_flow
                    #Revok flux part used in the flow in order
                    # to find better path if needed
                    self.graph[i][node] += dfs_flow

                    return dfs_flow
                
        return 0
    
