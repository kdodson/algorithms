# Modified Binary Search
# Used to solve problems where the array isn't perfectly sorted like:
    # - Nearly sorted array
    # - Rotated sorted array
    # - List with unknown length
    # - Searching in an array with duplicates
    # - Finding the first or last occurrence of an element in a sorted array
    # - Finding the square root of a number
    # - Finding the peak element in an array

# For example, given a rotated sorted array
# [4,5,6,7,0,1,2], find the index of the target element 0.
# The approach is to use binary search but adjust the mid-point calculation based on the rotation.

def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1 # Target not found

# Leetcode Problem: 33. Search in Rotated Sorted Array (medium)
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Leetcode Problem: 153. Find Minimum in Rotated Sorted Array (medium)
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Leetcode Problem: 240. Search a 2D Matrix II (medium)
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/