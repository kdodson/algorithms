# Matrix Traversal Pattern

# Most Matrix traversal problems can be seen as graph problems
# where nodes are the cells of the matrix and edges are the connections between them.
# (horizontal, vertical, diagonal)

# The best part is you can use most of the graph algorithms like DFS and BFS to solve
# matrix traversal problems. Like finding the shortest path in a grid.

# Leetcode Problem: 733 Flood Fill (easy)
# Link: https://leetcode.com/problems/flood-fill/

# Leetcode Problem: 200 Number of Islands (medium)
# Link: https://leetcode.com/problems/number-of-islands/

# Leetcode Problem: 130 Surrounded Regions (medium)
# Link: https://leetcode.com/problems/surrounded-regions/

# Number of islands Problem:
def count_islands(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
            return
        
        # Mark the cell as visited
        grid[i][j] = '0'

        # Explore all 4 directions
        dfs(i+1, j) # down
        dfs(i-1, j) # up
        dfs(i, j+1) # right
        dfs(i, j-1) # left

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j)
                islands += 1