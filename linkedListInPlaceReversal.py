# Linked List In Place Reversal
# This pattern is used to reverse a linked list in place without using extra space.
# It involves changing the next pointers of the nodes to reverse the direction of the list.

# Can use this for any problem that asks you to rearrange the links between nodes of a linked list.

# Leetcode Problem: 206. Reverse Linked List (easy)
# Link: https://leetcode.com/problems/reverse-linked-list/

# Leetcode Problem: 92. Reverse Linked List II (medium)
# Link: https://leetcode.com/problems/reverse-linked-list-ii/

# Leetcode Problem: 24. Swap Nodes in Pairs (medium)
# Link: https://leetcode.com/problems/swap-nodes-in-pairs/

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev  # New head of the reversed linked list
