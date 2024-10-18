import matplotlib.pyplot as plt
import networkx as nx

class GraphVisualizer:
    def __init__(self, graph, source, sink, highlighted_path=None, reduction=0):
        self.graph = graph
        self.source = source
        self.sink = sink
        self.highlighted_path = highlighted_path
        self.reduction = reduction
        self.n = len(graph)
        self.pos = None  

    def _calculate_positions(self):
        G = nx.DiGraph()
        for i in range(self.n):
            for j in range(self.n):
                if self.graph[i][j] > 0:
                    G.add_edge(i, j, capacity=self.graph[i][j])
        self.pos = nx.spring_layout(G)

    def draw_original_graph(self):
        if self.pos is None:
            self._calculate_positions()

        G = nx.DiGraph()
        for i in range(self.n):
            for j in range(self.n):
                if self.graph[i][j] > 0:
                    G.add_edge(i, j, capacity=self.graph[i][j])

        plt.figure(figsize=(10, 8))
        nx.draw(G, self.pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')

        edge_labels = {(i, j): f"Cap: {d['capacity']}" for i, j, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, self.pos, edge_labels=edge_labels)

        plt.scatter([self.pos[self.source][0]], [self.pos[self.source][1]], color='red', s=300, label='Source')
        plt.scatter([self.pos[self.sink][0]], [self.pos[self.sink][1]], color='green', s=300, label='Sink')

        plt.title("Original Graph for the Ford-Fulkerson Algorithm")
        plt.legend()
        plt.show()

    def draw_reduced_graph(self):
        if self.pos is None:
            self._calculate_positions()

        G_reduced = nx.DiGraph()
        edge_labels_reduced = {}

        for i in range(self.n):
            for j in range(self.n):
                if self.graph[i][j] > 0:
                    capacity = self.graph[i][j]
                    if self.highlighted_path and (i, j) in self.highlighted_path:
                        key = f'{i} -> {j}'
                        reduced_capacity = capacity - self.reduction
                        edge_labels_reduced[key] = f'{reduced_capacity} / {capacity}'
                    else:
                        G_reduced.add_edge(i, j, capacity=capacity)

        # Draw the reduced graph
        plt.figure(figsize=(10, 8))
        nx.draw(G_reduced, self.pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(G_reduced, self.pos, label_pos=0.5)

        if self.highlighted_path:
            edges_to_highlight = [(i, j) for (i, j) in self.highlighted_path]
            nx.draw_networkx_edges(G_reduced, self.pos, edgelist=edges_to_highlight, edge_color='red', width=2.5)

        table_data = [[key, value] for key, value in edge_labels_reduced.items()]
        table = plt.table(cellText=table_data, colLabels=['Clé', 'Valeur'], cellLoc='center', loc='upper right', 
                          bbox=[0.75, 0.75, 0.2, 0.2])

        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.0, 1.0)

        plt.title("Graph with Reduced Capacities Along Highlighted Path")
        plt.legend()
        plt.show()

    def draw_goal_graph(self):
        if self.pos is None:
            self._calculate_positions()

        plt.figure(figsize=(10, 8))
        G_third = nx.DiGraph()

        for i in range(self.n):
            for j in range(self.n):
                if self.graph[i][j] > 0:
                    G_third.add_edge(i, j, capacity=self.graph[i][j])  

        # Draw the graph with all edges in red
        nx.draw(G_third, self.pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
        nx.draw_networkx_edges(G_third, self.pos, edge_color='red', width=2)

        edge_labels_third = {(i, j): f"{G_third[i][j]['capacity']} / {G_third[i][j]['capacity']}" for i, j in G_third.edges()}
        nx.draw_networkx_edge_labels(G_third, self.pos, edge_labels=edge_labels_third)

        plt.scatter([self.pos[self.source][0]], [self.pos[self.source][1]], color='red', s=300, label='Source')
        plt.scatter([self.pos[self.sink][0]], [self.pos[self.sink][1]], color='green', s=300, label='Sink')

        plt.title("Graph with Original Capacities and Red Edges")
        plt.legend()
        plt.show()

    def visualize(self):
        self._calculate_positions()  
        self.draw_original_graph()
        self.draw_reduced_graph()
        self.draw_goal_graph()

