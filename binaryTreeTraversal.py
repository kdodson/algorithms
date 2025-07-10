# Binary Tree Traversal
# Used to traverse binary trees in different orders:
#     # - Pre-order (Root, Left, Right)
#     # - In-order (Left, Root, Right)
#     # - Post-order (Left, Right, Root)
#     # - Level-order (Breadth-first traversal)

# To retrieve the values of a binary search tree in sorted order, we can use in-order traversal.
# To create a copy of a tree (serialization), use pre-order traversal.
# When you want to process child nodes before the parent, use post-order traversal. (Like deleting a tree)
# When you want to process nodes level by level, use level-order traversal.

# Pre-order Leetcode Problem: 257. Binary Tree Paths (easy)
# Link: https://leetcode.com/problems/binary-tree-paths/

# In-order Leetcode Problem: 230. Kth Smallest Element in a BST (medium)
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Post-order Leetcode Problem: 124. Binary Tree Maximum Path Sum (hard)
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Level-order Leetcode Problem: 107. Binary Tree Level Order Traversal II (medium)
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/ 

def pre_order_traversal(root):
    if root:
        print(root.val, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=' ')
        in_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val, end=' ')

from collections import deque
def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)
    
    return result
