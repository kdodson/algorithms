# Fast and Slow Pointers
# This pattern is used to find cycles in a sequence or linked list.
# It involves using two pointers that move at different speeds (e.g., one moving one step at a time and the other moving two steps at a time).
# This can also be used to find the middle of a linked list in one pass.

# Leetcode Problem: 141. Linked List Cycle (easy)
# Link: https://leetcode.com/problems/linked-list-cycle/

# Leetcode Problem: 202. Happy Number (easy)
# Link: https://leetcode.com/problems/happy-number/

# Leetcode Problem: 287. Find the Duplicate Number (medium)
# Link: https://leetcode.com/problems/find-the-duplicate-number/

if __name__ == '__main__':
    # Example usage of the Fast and Slow Pointers pattern
    class ListNode:
        def __init__(self, value=0, next=None):
            self.value = value
            self.next = next

    # Create a linked list with a cycle for demonstration
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head  # Creating a cycle

    # Detect cycle using Fast and Slow Pointers
    slowPtr = head
    fastPtr = head

    while fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        if slowPtr == fastPtr:
            print("Cycle detected")
            break
    else:
        print("No cycle detected")