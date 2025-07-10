# Monotonic Stack
# Uses a stack to find the next greater or next smaller element in an array.

# Leetcode Problem: 496. Next Greater Element I (easy)
# Link: https://leetcode.com/problems/next-greater-element-i/

# Leetcode Problem: 739. Daily Temperatures (medium)
# Link: https://leetcode.com/problems/daily-temperatures/

# Leetcode Problem: 84. Largest Rectangle in Histogram (hard)
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

# Given an array, find the next greater element for each element in the array.
# The next greater element for an element x is the first greater element on the right side of x in the array.
# If there is no greater element, return -1 for that element.
def next_greater_element(arr):
    n = len(arr)
    stack = []
    result = [-1] * n # Initialize result with -1 for all elements

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]

        stack.append(i)
    
    return result

# Example usage
if __name__ == '__main__':
    arr = [4, 5, 2, 10, 8]
    print(next_greater_element(arr))  # Output: [5, 10, 10, -1, -1]
    # Explanation: The next greater elements are:
    # 4 -> 5, 5 -> 10, 2 -> 10, 10 -> -1, 8 -> -1
    # The stack is used to keep track of the indices of the elements in the array.
    # When we find a greater element, we pop the indices from the stack and update the result array.
    # If there are no greater elements, the result remains -1 for those indices.