# Prefix Sum Algorithm
# This algorithm is used to find the sum of elements in a range in an array.
# It preprocesses the array to create a prefix sum array, which allows for O(1) range sum queries.
# The prefix sum array is constructed such that prefix_sum[i] = arr[0] + arr[1] + ... + arr[i].
# This allows us to compute the sum of any subarray arr[l..r] as prefix_sum[r] - prefix_sum[l-1].
# Time Complexity: O(n) for preprocessing, O(1) for each query
# Space Complexity: O(n) for the prefix sum array

# Example usage:
# array = [1, 2, 3, 4, 5]
# prefix_sum = [1, 3, 6, 10, 15]
# sum of subarray from index 1 to 3 (inclusive) = prefix_sum[3] - prefix_sum[1-1] = 10 - 1 = 9

# Leetcode Problem: 303. Range Sum Query - Immutable (easy)
# Link: https://leetcode.com/problems/range-sum-query-immutable/

# Leetcode Problem: 525. Contiguous Array (medium)
# Link: https://leetcode.com/problems/contiguous-array/

# Leetcode Problem: 560. Subarray Sum Equals K (medium)
# Link: https://leetcode.com/problems/subarray-sum-equals-k/

class PrefixSum:
    def __init__(self, nums: list[int]):
        self.prefix_sums = [0]
        for num in nums:
            self.prefix_sums.append(self.prefix_sums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]

def main():
    prefixSum = PrefixSum([-2, 0, 3, -5, 2, -1])
    print(prefixSum.sumRange(0, 2))  # Output: 1
    print(prefixSum.sumRange(2, 5))  # Output: -1
    print(prefixSum.sumRange(0, 5))  # Output: -3

if __name__ == '__main__':
    main()