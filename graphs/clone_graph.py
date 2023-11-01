"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.old_new_node_mapping = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        ## we can rely on the node memory address or the value itself (constraint of values)
        ## we can use the node memory address itself
        ## in the case that we had non-unique node values
        ## we could still rely on the node memory address being unique
        self.old_new_node_mapping[node] = Node(node.val)

        for neighbor in node.neighbors:
            ## if we have not processed this neighbor or mapped it out, traverse to it and map the clone
            if neighbor not in self.old_new_node_mapping:
                self.old_new_node_mapping[neighbor] = self.cloneGraph(neighbor)
            
            ## add the just cloned or previously cloned neighbor to the list of the new node's neighbors
            self.old_new_node_mapping[node].neighbors.append(self.old_new_node_mapping[neighbor])

        ## return the clone of the current node
        return self.old_new_node_mapping[node]