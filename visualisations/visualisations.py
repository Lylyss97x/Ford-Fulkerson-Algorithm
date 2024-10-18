import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(graph, source, sink, highlighted_path=None, reduction=0):
    # Create a directed graph
    G = nx.DiGraph()

    # Initialize the original graph
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:  # If there is capacity
                G.add_edge(i, j, capacity=graph[i][j])

    # Define the position of the nodes for better visualization
    pos = nx.spring_layout(G)
    
    # Draw the original graph
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    
    # Add edge labels for capacities
    edge_labels = {(i, j): f"Cap: {d['capacity']}" for i, j, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Highlight source and sink nodes
    plt.scatter([pos[source][0]], [pos[source][1]], color='red', s=300, label='Source')
    plt.scatter([pos[sink][0]], [pos[sink][1]], color='green', s=300, label='Sink')

    plt.title("Original Graph for the Ford-Fulkerson Algorithm")
    plt.legend()
    plt.show()

    # Create a new graph for the highlighted path
    G_reduced = nx.DiGraph()

    # Reduce capacities along the highlighted path and set the new graph
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:  # If there is capacity
                capacity = graph[i][j]
                # If the edge is in the highlighted path, reduce its capacity
                if highlighted_path and (i, j) in highlighted_path:
                    capacity -= reduction
                G_reduced.add_edge(i, j, capacity=capacity)

    # Draw the reduced graph
    plt.figure(figsize=(10, 8))
    nx.draw(G_reduced, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')

    # Add edge labels for capacities in the reduced graph
    edge_labels_reduced = {(i, j): f"Cap: {d['capacity']}" for i, j, d in G_reduced.edges(data=True)}
    # Draw edge labels above edges
    nx.draw_networkx_edge_labels(G_reduced, pos, edge_labels=edge_labels_reduced, label_pos=0.5)

    # Highlight the path in red
    if highlighted_path:
        edges_to_highlight = [(i, j) for (i, j) in highlighted_path]
        nx.draw_networkx_edges(G_reduced, pos, edgelist=edges_to_highlight, edge_color='red', width=2.5)

    # Adjust positions of edge labels to be slightly above the edges
    for (i, j), (x, y) in zip(edge_labels_reduced.keys(), pos.items()):
        if (i, j) in edges_to_highlight:
            x_offset = (pos[j][0] - pos[i][0]) * 0.5
            y_offset = (pos[j][1] - pos[i][1]) * 0.5
            label_pos = (pos[i][0] + x_offset, pos[i][1] + y_offset + 0.1)  # Adjust y offset
            plt.text(label_pos[0], label_pos[1], edge_labels_reduced[(i, j)], horizontalalignment='center', fontsize=9, color='black')

    # Highlight source and sink nodes
    plt.scatter([pos[source][0]], [pos[source][1]], color='red', s=300, label='Source')
    plt.scatter([pos[sink][0]], [pos[sink][1]], color='green', s=300, label='Sink')

    plt.title("Graph with Reduced Capacities Along Highlighted Path")
    plt.legend()
    plt.show()

# Define the adjacency matrix (capacities)
graph = [
    [0, 10, 5, 0],
    [0, 0, 15, 10],
    [0, 0, 0, 10],
    [0, 0, 0, 0]
]

# Define the highlighted path as a list of edges (as tuples)
highlighted_path = [(0, 1), (1, 2), (2, 3)]  # Path from 0 -> 1 -> 2 -> 3
reduction_amount = 3  # Amount to reduce capacities along the path

# Visualize the graph
visualize_graph(graph, source=0, sink=3, highlighted_path=highlighted_path, reduction=reduction_amount)
