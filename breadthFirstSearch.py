# Breadth-First Search

# A traversal technical that explores nodes level by level in a tree or graph.
# Useful for 
# - finding the shortest path between two nodes in an unweighted graph,
# - printing all nodes of a tree level by level,
# - Finding all connected components in a graph.
# - Finding the shortest transformation sequence from one word to another.

# Leetcode Problem: 102. Binary Tree Level Order Traversal (medium)
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Leetcode Problem: 994. Rotting Oranges (medium)
# Link: https://leetcode.com/problems/rotting-oranges/

# Leetcode Problem: 127. Word Ladder (hard)
# Link: https://leetcode.com/problems/word-ladder/

def bfs(self, start):
    visited = set()
    queue = [start]

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)