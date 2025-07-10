# Top 'K' Elements
# Helps you find the 'K' largest, smallest, or most frequent elements in an array.

# Leetcode Problem: 215. Kth Largest Element in an Array (medium)
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

# Leetcode Problem: 347. Top K Frequent Elements (medium)
# Link: https://leetcode.com/problems/top-k-frequent-elements/

# Leetcode Problem: 373. Find K Pairs with Smallest Sums (medium)
# Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

if __name__ == '__main__':
    import heapq

    # Function to find the Kth largest element in an array
    def kth_largest(nums, k):
        return heapq.nlargest(k, nums)[-1]

    # Example usage
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"The {k}th largest element is: {kth_largest(nums, k)}")  # Output: 5

    # Function to find the top K frequent elements in an array
    def top_k_frequent(nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        return heapq.nlargest(k, count.keys(), key=count.get)

    # Example usage
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"The top {k} frequent elements are: {top_k_frequent(nums, k)}")  # Output: [1, 2]

# Explanation:
# The kth_largest function uses heapq.nlargest to find the Kth largest element in the array.
# It creates a max heap and retrieves the K largest elements, returning the last one.
# The top_k_frequent function counts the frequency of each element and uses heapq.nlargest to find the K most frequent elements.