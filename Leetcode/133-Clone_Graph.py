"""
https://leetcode.com/problems/clone-graph/


Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 
"""


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    """
    DFS
    Stopping condition: return when we have already copied the node (found cycle)
    or when there is no adjacent node

    Need to created a 'visited' map, key: reference to the original node, value: reference to 
    the new node. 'visited' map would be passwed as another parameter

    using the map, if the copy is already visited, then just return the created node. else, create copy of the current
    node and put into visited map..
    Then iterate through adjacent nodes and append to the 'neighbors' list
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.deep_copy_graph(node)
        
        
    def deep_copy_graph(self, graph_node: 'Node', visited = None) -> 'Node':
        if graph_node is None:
            return graph_node

        if visited is None:
            visited = {}

        if graph_node in visited:
            return visited[graph_node]

        visited[graph_node] = Node(graph_node.val, [])

        for node in graph_node.neighbors:
            visited[graph_node].neighbors.append(self.deep_copy_graph(node, visited))

        return visited[graph_node]