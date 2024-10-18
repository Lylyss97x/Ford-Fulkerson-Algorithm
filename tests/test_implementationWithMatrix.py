from collections import defaultdict
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from implementation1 import FordFulkersonMatrix
from implementation1 import FordFulkersonList

graph_flux = [
    [0, 16, 13, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 10, 12, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 14, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 0, 20, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 10, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

source = 0
sink = 9
expected_max_flow = 8  


def test_max_flow_performance_matrix():
    FFMatrix = FordFulkersonMatrix(graph_flux, source, sink, len(graph_flux))

    start_time = time.time()
    
    max_flow = FFMatrix.max_flow()
    
    elapsed_time = time.time() - start_time

    assert max_flow == expected_max_flow, f"Expected {expected_max_flow}, got {max_flow}"
    assert elapsed_time < 1, f"Performance test failed, took {elapsed_time:.6f} seconds"

def test_max_flow_performance_list():
    FFList = FordFulkersonList(defaultdict(list), source, sink, len(graph_flux))

    FFList.add_edge(0, 1, 16)  
    FFList.add_edge(0, 2, 13)  
    FFList.add_edge(1, 2, 10)  
    FFList.add_edge(1, 3, 12)  
    FFList.add_edge(2, 1, 4)   
    FFList.add_edge(2, 4, 14)  
    FFList.add_edge(3, 2, 9)   
    FFList.add_edge(3, 5, 20)  
    FFList.add_edge(4, 3, 7)   
    FFList.add_edge(4, 5, 4)  
    FFList.add_edge(5, 6, 10)
    FFList.add_edge(6, 7, 8)
    FFList.add_edge(7, 9, 10)
    FFList.add_edge(8, 9, 5)

    start_time = time.time()
    
    max_flow = FFList.max_flow()
    
    elapsed_time = time.time() - start_time

    assert max_flow == expected_max_flow, f"Expected {expected_max_flow}, got {max_flow}"
    assert elapsed_time < 1, f"Performance test failed, took {elapsed_time:.6f} seconds"
