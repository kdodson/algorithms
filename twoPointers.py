"""
The two pointers pattern is a technique commonly used to solve problems involving sorted arrays or linked lists. 
It involves using two pointers, typically starting at different positions (e.g., one at the beginning and the other at the end of the array), 
and moving them towards each other or in a specific direction based on certain conditions.

This pattern is particularly useful for problems such as:
- Finding pairs in a sorted array that satisfy a specific condition (e.g., sum equals a target).
- Removing duplicates from a sorted array.
- Reversing a sequence in place.
- Partitioning problems, such as rearranging elements based on a pivot.

The two pointers approach often reduces the time complexity of problems from O(n^2) to O(n) by avoiding nested loops.
"""

# Leetcode Problem: 11. Container With Most Water (medium)
# Link: https://leetcode.com/problems/container-with-most-water/

# Leetcode Problem: 15. 3Sum (medium)
# Link: https://leetcode.com/problems/3sum/

# Leetcode Problem: 26. Remove Duplicates from Sorted Array (easy)
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Leetcode Problem: 167. Two Sum II - Input Array Is Sorted (medium)
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def removeDuplicates(nums: list[int]) -> int:
    left = 0
    for right in range(1, len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
    return (left + 1)

def main():
    # Remove Duplicates from Sorted Array
    nums = [1, 1, 2]
    length = removeDuplicates(nums)
    print(f"Length of array after removing duplicates: {length}")
    print(f"Array after removing duplicates: {nums[:length]}")

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = removeDuplicates(nums)
    print(f"Length of array after removing duplicates: {length}")
    print(f"Array after removing duplicates: {nums[:length]}")

if __name__ == '__main__':
    main()