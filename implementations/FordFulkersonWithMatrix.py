import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .FordFulkerson import FordFulkersonAlgorithm


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