"""
57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

"""
My first idea is to add the new interval to the list of intervals and sort the list by their start values.

Then, I'll create a new list called `res` to store the merged intervals, starting with the first interval.

I'll iterate through the remaining intervals. For each interval, I'll compare its start with the end of the last interval in `res`.

If the start is less than or equal to the end of the last interval, it means the two intervals overlap or touch. In this case, I'll merge them by updating the right boundary to the maximum of the two end values.

Otherwise, I'll append the current interval to `res`.

The time complexity is **O(n log n)** because of sorting, while merging takes O(n) time.
The space complexity is **O(n)** because we need extra space for the result list.
"""


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:

        intervals.append(newInterval)

        # 1. Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # 2. Initialize the result
        res = [intervals[0]]

        # 3. Merge overlapping intervals
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])

        return res


"""
We can optimize this solution because the intervals are already sorted in ascending order and are non-overlapping. We can take advantage of this property to avoid sorting.

I'll create a new list called `res` to store the results, and use a variable called `pending` to track the interval currently being processed.

Then, I'll iterate through the intervals. For each interval, I'll compare it with `pending`. There are three cases:

1. **No overlap, and the current interval is to the left of `pending`.** I'll append the current interval to `res`.

2. **No overlap, and the current interval is to the right of `pending`.** I'll append `pending` to `res`, then replace `pending` with the current interval and continue processing the remaining intervals.

3. **The two intervals overlap.** I'll merge them by updating the left and right boundaries of `pending`, without appending anything to `res`.

Finally, I'll append the remaining `pending` interval to `res`.

The **time complexity is O(n)** because we only traverse the intervals once.

The **space complexity is O(n)** for storing the result, while the auxiliary space is O(1), excluding the output.
"""


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:

        res = []
        pending = newInterval.copy()
        for start, end in intervals:

            if end < pending[0]:
                res.append([start, end])
            elif start > pending[1]:
                res.append(pending)

                pending = [start, end]
            else:
                pending[0] = min(start, pending[0])
                pending[1] = max(end, pending[1])

        res.append(pending)

        return res
