# Sliding Window Algorithm
# Instead of computing the sum of each subarray from scratch, we can maintain a running sum of the current window.
# When we move the window to the right, we subtract the element that is leaving the window and add the new element that is entering the window.
# This reduces the time complexity to O(n) for finding the maximum sum of a subarray of size k.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

# Leetcode Problem: 3. Longest Substring Without Repeating Characters (medium)
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Leetcode Problem: 76. Minimum Window Substring (hard)
# Link: https://leetcode.com/problems/minimum-window-substring/

# Leetcode Problem: 643. Maximum Average Subarray I (easy)
# Link: https://leetcode.com/problems/maximum-average-subarray-i/

# Find subarray of size k with maximum sum
def max_subarray_sum_sliding_window(arr, k) :
    n = len(arr)

    window_sum = sum(arr[:k])

    max_sum = window_sum
    max_start_index = 0

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_start_index = i + 1

    return arr[max_start_index:max_start_index + k], max_sum