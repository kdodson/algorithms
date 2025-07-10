# Overlapping Intervals
# Useful for intervals or ranges that overlap, such as time slots or geographical areas.
# e.g. 
# Merging Intervals: Given a collection of intervals, merge all overlapping intervals into one.
# Interval Intersection: Find the intersection between two sets of intervals.
# Insert Interval: Add a new interval to a list of non-overlapping intervals.
# Find minimum number of meeting rooms required to hold all meetings.

# Merge all overlapping intervals problem example:
# Start by sorting the intervals based on their start times.
# Create an empty list to hold the merged intervals.
# Iterate through the sorted intervals and check if it overlaps with the last merged interval.
# If it does, merge them by updating the end time of the last merged interval.

# Leetcode Problem: 56. Merge Intervals (medium)
# Link: https://leetcode.com/problems/merge-intervals/

# Leetcode Problem: 57. Insert Interval (medium)
# Link: https://leetcode.com/problems/insert-interval/

# Leetcode Problem: 435. Non-overlapping Intervals (medium)
# Link: https://leetcode.com/problems/non-overlapping-intervals/

# Merge Intervals Solution:
def merge(intervals: list[list[int]]) -> list[list[int]]:
    # Start by sorting the intervals based on their start times
    intervals.sort(key = lambda x: x[0])
    
    mergedList = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= mergedList[-1][1]:
            mergedList[-1][1] = max(intervals[i][1], mergedList[-1][1])
        else:
            mergedList.append(intervals[i])

    return mergedList

if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print("Merged Intervals:", merge(intervals))  # Output: [[1,6],[8,10],[15,18]]