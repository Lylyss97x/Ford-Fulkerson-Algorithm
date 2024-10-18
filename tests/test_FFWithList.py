
import sys
import os
from collections import defaultdict
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from implementations.FordFulkersonWithList import FordFulkersonList, Edge


class TestFordFulkersonList:
    
    def test_basic_functionality(self):
        # Basic graph with 4 nodes
        ff = FordFulkersonList(defaultdict(list), 0, 3, 4)
        ff.add_edge(0, 1, 10)
        ff.add_edge(0, 2, 5)
        ff.add_edge(1, 2, 15)
        ff.add_edge(1, 3, 10)
        ff.add_edge(2, 3, 10)

        assert ff.max_flow() == 15

    def test_no_edges(self):
        # Case with no edges
        ff = FordFulkersonList(defaultdict(list), 0, 1,2)
        assert ff.max_flow() == 0

    def test_single_edge(self):
        # Case with a single edge
        ff = FordFulkersonList(defaultdict(list),0,1,2)
        ff.add_edge(0, 1, 5)
        assert ff.max_flow() == 5

    def test_disconnected_graph(self):
        # Case with disconnected graph
        ff = FordFulkersonList(defaultdict(list), 0, 2, 3)
        ff.source_node = 0
        ff.sink_node = 2
        ff.add_edge(0, 1, 10)
        assert ff.max_flow() == 0

    def test_multiple_paths(self):
        # Case with multiple paths
        ff = FordFulkersonList(defaultdict(list), 0, 3, 4)
        ff.add_edge(0, 1, 10)
        ff.add_edge(0, 2, 5)
        ff.add_edge(1, 3, 15)
        ff.add_edge(2, 3, 10)

        assert ff.max_flow() == 15

    def test_initialization(self):
        # Test that an edge is initialized correctly
        edge = Edge(1, 10)
        assert edge.to == 1
        assert edge.capacity == 10
        assert edge.flow == 0
        assert edge.latest_capacity() == 10  


