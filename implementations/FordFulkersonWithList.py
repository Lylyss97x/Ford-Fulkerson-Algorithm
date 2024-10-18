import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .FordFulkerson import FordFulkersonAlgorithm


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
