from collections import defaultdict
from implementations.FordFulkersonWithList import FordFulkersonList
from implementations.FordFulkersonWithMatrix import FordFulkersonMatrix

def main():
    # Exemple de graphe pour la matrice d'adjacence
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


if __name__ == "__main__":
    main()
