from collections import defaultdict
from implementations.FordFulkersonWithList import FordFulkersonList
from implementations.FordFulkersonWithMatrix import FordFulkersonMatrix
from visualisations.visualisations import GraphVisualizer

def main():
    
    #Test Algorith with adjacency matrix
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

    FFMatrix = FordFulkersonMatrix(graph_flux, source, sink, len(graph_flux))
    max_flow_matrix = FFMatrix.max_flow()
    print(f"Flux maximum (Matrice d'adjacence): {max_flow_matrix}")

    #Test Algorith with adjacency list
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

    max_flow_list = FFList.max_flow()
    print(f"Flux maximum (Liste d'adjacence): {max_flow_list}")

    #Visualisation graph
    graph = [
    [0, 10, 5, 0],
    [0, 0, 15, 10],
    [0, 0, 0, 10],
    [0, 0, 0, 0]
    ]
    highlighted_path = [(0, 1), (1, 2), (2, 3)]
    reduction_amount = 3  

    visualizer = GraphVisualizer(graph, source=0, sink=3, highlighted_path=highlighted_path, reduction=reduction_amount)
    visualizer.visualize()


if __name__ == "__main__":
    main()
