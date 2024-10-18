# FORD FULKERSON ALGORITHM
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)

# CONCEPT
The Ford-Fulkerson algorithm computes the maximum flow in a flow network. In simple terms, according to the maximum of existing paths possible between a point A and a point B, and their flow capacities (the maximum values that can go through the path), we search for the maximum flow we can reach by trying to add new paths. We repeat the process until all flows are saturated or there are no paths left. The algorithm was published by two mathematicians Delbert Ray Fulkerson and Lester Randolph Ford in 1956.

# Applications
Water distribution: Optimizes the quantity of water delivered through a pipe network, while respecting pipe capacities.
Bipartite matching: Solves matching problems in bipartite graphs (e.g. assigning tasks to workers).
Circulation with demands: Solves more complex flow problems where some nodes have flow requirements, and arcs can have minimum and maximum capacities.

# COMPLEXITY
## First Implementation Complexity  : Adjacency Matrix

### Increasing path search (DFS)
In the case of an adjacency matrix, for each node, all neighboring nodes are traversed.
This means checking connections with all other nodes for each starting node.

### Path search complexity (DFS): O(V2)
V : number of nodes in the graph.
Total number of iterations to find the maximum flow: O(E⋅V2)
In the worst case : O(E⋅V²) 
  E : number of edges 
  C : maximum edge capacity

### Memory : The adjacency matrix requires O(V2) of memory to store capacities between nodes.


## Second Implementation Complexity  : Adjacency List

### Increasing path search (DFS):
In this approach, we scan only the direct neighbors of a node. For each node, we examine only its outgoing edges.
### Path search complexity (DFS): O(E)
  E : number of edges.
  
### Total number of iterations to find the maximum flow:O(C⋅E)
The maximum flow could also require up to O(C) iterations.
The total complexity then becomes : O(C⋅E)

### Memory : The adjacency list requires O(V+E) of memory to store the graph.
