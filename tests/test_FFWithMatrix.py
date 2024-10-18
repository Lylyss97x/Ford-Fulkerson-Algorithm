import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from implementations.FordFulkersonWithMatrix import FordFulkersonMatrix 

class TestFordFulkersonMatrix:
    
    def test_basic_functionality(self):
        # Basic graph with 4 nodes
        graph = [
            [0, 10, 5, 0],
            [0, 0, 15, 10],
            [0, 0, 0, 10],
            [0, 0, 0, 0]
        ]
        ff = FordFulkersonMatrix(graph, 0, 3, 4)
        assert ff.max_flow() == 15

    def test_no_edges(self):
        # Case with no edges
        graph = [
            [0, 0],
            [0, 0]
        ]
        ff = FordFulkersonMatrix(graph, 0, 1, 2)
        assert ff.max_flow() == 0

    def test_single_edge(self):
        # Case with a single edge
        graph = [
            [0, 5],
            [0, 0]
        ]
        ff = FordFulkersonMatrix(graph, 0, 1, 2)
        assert ff.max_flow() == 5

    def test_disconnected_graph(self):
        # Case with disconnected graph
        graph = [
            [0, 10, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        ff = FordFulkersonMatrix(graph, 0, 2, 3)
        assert ff.max_flow() == 0

    def test_multiple_paths(self):
        # Case with multiple paths
        graph = [
            [0, 10, 5, 0],
            [0, 0, 15, 10],
            [0, 0, 0, 10],
            [0, 0, 0, 0]
        ]
        ff = FordFulkersonMatrix(graph, 0, 3, 4)
        assert ff.max_flow() == 15

    def test_circular_graph(self):
        # Case with a circular graph
        graph = [
            [0, 10, 5, 0],
            [0, 0, 15, 10],
            [0, 0, 0, 10],
            [5, 0, 0, 0]  
        ]
        ff = FordFulkersonMatrix(graph, 0, 3, 4)
        assert ff.max_flow() == 15

    def test_zero_capacity_edge(self):
        # Case with edges of zero capacity
        graph = [
            [0, 10, 0, 0],
            [0, 0, 0, 10],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        ff = FordFulkersonMatrix(graph, 0, 3, 4)
        assert ff.max_flow() == 10

    def test_high_capacity_edges(self):
        # Case with high capacity edges
        graph = [
            [0, 1000, 1000, 0],
            [0, 0, 1000, 1000],
            [0, 0, 0, 1000],
            [0, 0, 0, 0]
        ]
        ff = FordFulkersonMatrix(graph, 0, 3, 4)
        assert ff.max_flow() == 2000  
