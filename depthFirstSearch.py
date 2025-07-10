# Depth-First Search (DFS) algorithm
# Used to explore all depths or branches in graphs or trees
# to solve problems like:
#   - finding a path between two nodes
#   - checking for cycles
#   - Finding a topological order in a directed acyclic graph (DAG)
#   - Counting the number of connected components in a graph

# Leetcode Problem: 133 Clone Graph (medium)
# Link: https://leetcode.com/problems/clone-graph/

# Leetcode Problem: 113 Path Sum II (medium)
# Link: https://leetcode.com/problems/path-sum-ii/

# Leetcode Problem: 210 Course Schedule II (medium)
# Link: https://leetcode.com/problems/course-schedule-ii/

def dfs_recursive(self, v, visited):
    """
    Recursive DFS algorithm
    :param v: current vertex
    :param visited: list of visited vertices
    """
    visited.add(v)  # Mark the current node as visited
    print(v, end=' ')

    for neighbor in self.graph[v]:  # Recur for all the vertices adjacent to this vertex
        if neighbor not in visited:
            self.dfs_recursive(neighbor, visited)

def dfs_iterative(self, v):
    visited = set()  # Set to keep track of visited nodes
    stack = [v]  # Stack for DFS

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            for neighbor in reversed(self.graph[vertex]): # Add neighbors to stack in reverse order for correct traversal
                if neighbor not in visited:
                    stack.append(neighbor)